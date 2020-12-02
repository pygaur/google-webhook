"""
"""
import json
import uuid
import requests

from config import STOP_ENDPOINT

################
# HACK #
token = NOT_DEFINED
################


def stop_listening(header, body):
    """
    :param header:
    :param body:
    :return:
    """
    r = requests.post(url=STOP_ENDPOINT, data=json.dumps(body),
                      headers=header)
    print('Webhook stopped Successfully...')
    print(r.text)
    print('###################')


if __name__ == '__main__':
    header = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    body = {
        "id": "<VALUE>",
        "resourceId": "<VALUE>",
    }
    stop_listening(header, body)

