"""Get a list of Messages from the user's mailbox
   filtered by sender.
   And Delete the mails.
"""
from __future__ import print_function

import math

import pickle
import os.path
from googleapiclient.http import BatchHttpRequest
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import errors

USER_ID = 'me'
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://mail.google.com/'

to_delete_ids = []


def getService():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service


def getMailsByFilter(service, user_id, cleanup_list):
    try:
        batch = BatchHttpRequest(callback=getCallback)
        for lookup in cleanup_list:
            batch.add(service.users().messages().list(userId=user_id,
                                                      q=lookup),
                      request_id=lookup)
        batch.execute()
        return 0
    except errors.HttpError as ex:
        print(f'Exception:{ex}')
        return 1


def batchDeleteMails(service):
    if not to_delete_ids:
        return 1
    print('Deleting e-mails...')
    try:
        # batch delete messages as 1000 msg limit for regular users
        batch_limit = 1000
        iterations = math.ceil(len(to_delete_ids) / batch_limit)
        skip, take = 0, batch_limit
        print(
            f'Total Messages: {len(to_delete_ids)},\
            Target Iterations: {iterations}')

        batch = BatchHttpRequest(callback=deleteCallback)

        for _ in range(iterations):
            payload = {'ids': []}
            payload['ids'].extend([str(d['id'])
                                   for d in to_delete_ids[skip: take]])
            batch.add(service.users().messages().batchDelete(
                userId=USER_ID,
                body=payload
            ))
            skip = take
            take = len(to_delete_ids) if (take + batch_limit >=
                                          len(to_delete_ids))\
                else take + batch_limit

        batch.execute()
    except errors.HttpError as ex:
        print(f'Exception:{ex}')
        return 1


def getCallback(request_id, response, exception):
    if exception:
        print(f'Error:{exception}')
    else:
        try:
            messages = []
            if 'messages' in response:
                messages.extend(response['messages'])

            while 'nextPageToken' in response:
                page_token = response['nextPageToken']
                response = service.users().messages().list(
                    userId=USER_ID,
                    q=request_id,
                    pageToken=page_token).execute()
                try:
                    messages.extend(response['messages'])
                except KeyError:
                    print(f"{request_id}: {response}")
            to_delete_ids.extend(messages)
            if len(messages) > 0:
                print(f'{request_id} --> fetched messages: {len(messages)}')
        except errors.HttpError as ex:
            print(f'Exception:{ex}')
            return 1


def deleteCallback(request_id, response, exception):
    if exception:
        print(f'Error: {exception}')
    else:
        print(f'Request Id: {request_id}')


service = getService()

if __name__ == '__main__':
    mail_filter = set()
    with open('mail_filter.txt', encoding='utf-8') as fp:
        mail_filter = {line.strip() for line in fp if not line.startswith('#')}

    getMailsByFilter(service, USER_ID, mail_filter)
    print('-' * 85)
    print(f'Total mails to cleanup: {len(to_delete_ids)}')
    print('-' * 85)
    batchDeleteMails(service)
