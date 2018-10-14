#!/usr/bin/python
# encoding=utf8

import json
import requests
import base64

def send_SMS(recipient, message):
    """ In 'Mobile' mode of the game send SMS to recipient using ESENDEX
    https://developers.esendex.com/api-reference
    Return status code """

    with open('./config.json', 'r') as file:
        config_file = json.load(file)

    username = config_file['SMS']['username']
    password = config_file['SMS']['password']
    accountReference = config_file['SMS']['accountReference']
    expeditor =config_file['SMS']['expeditor']

    authHeader = 'Basic ' \
                 + base64.b64encode(
                     ("%s:%s" % (
                         username, password)
                      )
                     .encode('utf-8')) \
                     .decode('utf-8')
    headers = { 'Authorization': authHeader }

    data = {'accountreference': accountReference,
            'messages': [
                {"from": expeditor, "to": recipient, "body": message }
                ]
            }

    r = requests.post("http://api.esendex.com/v1.0/messagedispatcher",
                      headers=headers,
                      json=data)

    return r.status_code

def send_Slack(recipient, message):
    """ In 'Slack' mode of the game send Direct Messages to recipient using API
    https://api.slack.com/ """

    todo = True

    return todo