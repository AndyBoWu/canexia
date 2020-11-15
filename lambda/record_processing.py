# Purpose: potential solution of the Canexia Technial Quiz
#
# DESC: make sure this lambda subscribed to a dynamodb table, once a new record
#       inserted, or existing record modified/removed, lambda function then inv-
#       oke aws ses to send out an eamil to the email address defined in the msg
#
# Author: Andy Bo Wu
#
# Date: Nov 14, 2020


import json
import boto3
from botocore.exceptions import ClientError

SENDER = "Andy Wu <bwu2sfu@gmail.com>"
AWS_REION = "us-west-2"
CHARSET = "UTF-8"

print('Loading Lambda Function')


def lambda_handler(event, context):
    print('-------------------------------------------------------------------')
    try:
        for record in event['Records']:
            # 1/ handle event type
            if record['eventName'] == 'INSERT':
                handle_insert(record)
            elif record['eventName'] == 'MODIFY':
                handle_modify(record)
            elif record['eventName'] == 'REMOVE':
                handle_remove(record)
        print('---------------------------------------------------------------')
    except Exception as e:
        print(e)
        print('---------------------------------------------------------------')
        return "Something bad just happened, Andy, read the stacktrace!"


def handle_insert(record):
    print('Handling INSERT event')
    newImage = record['dynamodb']['NewImage']

    recipient = newImage['email']['S']
    name = newImage['name']['S']
    msg = newImage['message']['S']

    # send msg to the recipient
    subject = 'New Account Created'
    ses_client = boto3.client('ses', region_name=AWS_REION)
    try:
        # Provide the contents of the email.
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': msg,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': subject,
                },
            },
            Source=SENDER,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def handle_modify(r):
    print('Handling MODIFY event')
    # TO-DO
    pass


def handle_remove(r):
    print('Handling REMOVE event')
    # TO-DO
    pass


def handle_ses():
    # if code refacotring is necessary later
    pass
