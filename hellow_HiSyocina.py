# coding: utf-8 

from requests_oauthlib import OAuth1Session
import os
import random
import datetime
import json
from pathlib import Path

def hellowHiSyocina(*env):
    twitter = OAuth1Session(env[0], env[1], env[2], env[3])

    timestamp = datetime.datetime.today()
    timestamp = str(timestamp.strftime("%Y/%m/%d %H:%M"))

    params = {"status": '@_HaLucina' + '\n' + timestamp + '\n' + '秘書シナが起動されました(\';\')'} 
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)

if __name__ == "__main__":

    hellowHiSyocina(os.environ["CONSUMER_KEY"],
	os.environ["CONSUMER_SECRET"],
	os.environ["ACCESS_TOKEN_KEY"],
	os.environ["ACCESS_TOKEN_SECRET"])
