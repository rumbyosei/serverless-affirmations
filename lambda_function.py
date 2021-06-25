import json
from random import randint
import os
import boto3

def sendAffirmations(event, context):
    with open('affirmations.json') as file:
        data = json.load(file)
        quotes = data["quotes"]
        selectQuote = randint(0, len(quotes)-1)
    snsClient = boto3.client('sns')
    response = snsClient.publish(
        TopicArn=os.environ['topicARN'],
        Message=quotes[selectQuote],
        Subject='Good Morning',
    )
    return response
