"""Get a list of Messages from the user's mailbox
   filtered by sender.
   And Delete the mails.
"""
from __future__ import print_function

import math
import random
import time

import pickle
import os.path
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


def getMailsByFilter(user_id, cleanup_list):
    try:
        # batch = BatchHttpRequest(callback=getCallback)
        batch = service.new_batch_http_request(callback=getCallback)

        # use filter_count to limit search to 100 requests
        # at a time
        LIMIT = 100
        skip, take = 0, LIMIT
        cleanup_list = list(cleanup_list)

        iterations = math.ceil(len(cleanup_list) / LIMIT)

        for _ in range(iterations):
            for lookup in cleanup_list[skip: take]:
                batch.add(service.users().messages().list(
                    userId=user_id,
                    q=lookup),
                    request_id=lookup)

            batch.execute()
            skip = take
            take = len(cleanup_list) if (take + LIMIT) >= len(cleanup_list) \
                else (take + LIMIT)
            batch = service.new_batch_http_request(callback=getCallback)

        return 0
    except errors.HttpError as ex:
        print(f'Error:{ex}')
        return 1


def batchDeleteMails():
    if not to_delete_ids:
        return 1
    print('Deleting e-mails...')
    try:
        # batch delete messages as 10 msg limit for regular users
        batch_limit = 10
        iterations = math.ceil(len(to_delete_ids) / batch_limit)
        skip, take = 0, batch_limit
        print(
            f'Total Messages: {len(to_delete_ids)},\
            Target Iterations: {iterations}')

        # batch = BatchHttpRequest(callback=deleteCallback)
        batch = service.new_batch_http_request(callback=deleteCallback)

        for _ in range(iterations):
            for del_id in to_delete_ids[skip:take]:
                batch.add(service.users().messages().trash(userId=USER_ID, id=del_id))

            batch.execute()
            # time.sleep(random.randint(1, 3))
            skip = take
            take = len(to_delete_ids) if (take + batch_limit >=
                                          len(to_delete_ids)) \
                else take + batch_limit
            batch = service.new_batch_http_request(callback=deleteCallback)
    except errors.HttpError as ex:
        print(f'Error:{ex}')
        return 1


def getCallback(request_id, response, exception):
    if exception:
        print(f'Error:{exception}, Request_id: {request_id}')
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
            if len(messages) > 0:
                for msg in messages:
                    to_delete_ids.append(str(msg['id']))
                print(f'{request_id} --> fetched messages: {len(messages)}')
        except errors.HttpError as ex:
            print(f'Error:{ex}, Request_id: {request_id}')
            return 1


def deleteCallback(request_id, response, exception):
    if exception:
        print(flush=True)
        print(f'Error: {exception}, Request_id: {request_id}')
    else:
        print(f'Request Id: {request_id}', end=' ', sep='-')


service = getService()

if __name__ == '__main__':
    mail_filter = set()
    with open('mail_filter.txt', encoding='utf-8') as fp:
        mail_filter = {line.strip() for line in fp if not line.startswith('#')}

    getMailsByFilter(USER_ID, mail_filter)
    print('-' * 85)
    print(f'Total mails to cleanup: {len(to_delete_ids)}')
    print('-' * 85)
    batchDeleteMails()
