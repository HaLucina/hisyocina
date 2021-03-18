# coding: utf-8 

from requests_oauthlib import OAuth1Session
import os
import random
import datetime
import json
from pathlib import Path



def upload(envs):
    twitter = OAuth1Session(envs[0], envs[1], envs[2], envs[3])

    tweets = []
    with open('contentsList.txt', mode='r', encoding='utf-8') as f:
        links = [line.strip() for line in f.readlines()]
    
    randomtweet = links[random.randrange(len(links))]
    timestamp = datetime.datetime.today()
    timestamp = str(timestamp.strftime("%Y/%m/%d %H:%M"))

    params = {"status": timestamp + '\n' + 'https://hackheatharu.xyz/' + randomtweet + '/'} 
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)

if __name__ == "__main__":
    print('done blogTweet.py')
