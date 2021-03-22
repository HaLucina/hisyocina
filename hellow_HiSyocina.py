# coding: utf-8 

from requests_oauthlib import OAuth1Session
import os
import random
import datetime
import json
from pathlib import Path

def activate(envs):
    twitter = OAuth1Session(envs[0], envs[1], envs[2], envs[3])

    timestamp = datetime.datetime.today()
    timestamp = str(timestamp.strftime("%Y/%m/%d %H:%M"))

    params = {"status": timestamp + ' Githubへのアップロード成功' + '\n' + '秘書シナを起動します(\';\')'} 
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)

if __name__ == "__main__":

    activate(os.environ["CONSUMER_KEY"],
	os.environ["CONSUMER_SECRET"],
	os.environ["ACCESS_TOKEN_KEY"],
	os.environ["ACCESS_TOKEN_SECRET"])
