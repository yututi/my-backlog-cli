import urllib.request
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")
SPACE = os.environ.get("SPACE")

BASE_URL = "https://{}.backlog.com/api/v2/".format(SPACE)

HEADER = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

def get(url, params):
    params["apiKey"] = API_KEY
    req = urllib.request.Request('{}?{}'.format(
        BASE_URL + url, urllib.parse.urlencode(params)), None, headers=HEADER, method="GET")
    try:
        with urllib.request.urlopen(req) as res:
            body = json.load(res)
        return body
    except urllib.error.URLError as e:
        data = e.read().decode("utf8", 'ignore')
        print(data)


def post(url, data):
    params = {}
    params["apiKey"] = API_KEY
    data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request('{}?{}'.format(
        BASE_URL + url, urllib.parse.urlencode(params)), data, headers=HEADER, method="POST")
    try:
        with urllib.request.urlopen(req) as res:
            body = json.load(res)
        return body
    except urllib.error.URLError as e:
        data = e.read().decode("utf8", 'ignore')
        print(data)
        return {}


def patch(url, data):
    params = {}
    params["apiKey"] = API_KEY
    data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request('{}?{}'.format(
        BASE_URL + url, urllib.parse.urlencode(params)), data, headers=HEADER, method="PATCH")
    try:
        with urllib.request.urlopen(req) as res:
            body = json.load(res)
        return body
    except urllib.error.URLError as e:
        data = e.read().decode("utf8", 'ignore')
        print(data)
        return {}
