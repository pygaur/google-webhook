"""
"""
import json
import uuid
import requests

from config import HOST, WATCH_ENDPOINT

################
# HACK #
token = NOT_DEFINED
################


def start_listening(header, body):
    """
    :param header:
    :param body:
    :return:
    """
    r = requests.post(url=WATCH_ENDPOINT,
                      data=json.dumps(body),
                      headers=header)
    print('Webhook Registered Successfully...')
    print(r.text)
    print('###################')


def get_channel_id():
    """
    :return:
    """
    return str(uuid.uuid4())


if __name__ == '__main__':
    channel_id = get_channel_id()

    header = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    body = {
        "kind": "api#channel",
        "id": channel_id,
        "type": "web_hook",
        "address": '{}/notifications/'.format(HOST),
        "token":"target=myApp-AdminActivities",
    }
    start_listening(header, body)

