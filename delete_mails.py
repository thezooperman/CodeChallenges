"""Get a list of Messages from the user's mailbox
   filtered by sender.
   And Delete the mails.
"""
from __future__ import print_function

import math
from apiclient import errors
from googleapiclient.http import BatchHttpRequest
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import client, file, tools

USER_ID = 'me'
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://mail.google.com/'

to_delete_ids = []


def getService():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    return service


def getMailsByFilter(service, user_id, cleanup_list):
    try:
        batch = BatchHttpRequest(callback=getCallback)
        for lookup in cleanup_list:
            batch.add(service.users().messages().list(userId=user_id,
                                                      q=lookup), request_id=lookup)
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

        for i in range(iterations):
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
                messages.extend(response['messages'])
            to_delete_ids.extend(messages)
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
    mail_filter = []
    with open('mail_filter.txt', encoding='utf-8') as fp:
        mail_filter = [line.strip() for line in fp if not line.startswith('#')]

    getMailsByFilter(service, USER_ID, mail_filter)
    print('-' * 55)
    print(f'Total mails to cleanup: {len(to_delete_ids)}')
    print('-' * 55)
    batchDeleteMails(service)
