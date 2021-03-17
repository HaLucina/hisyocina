import tweepy
from requests_oauthlib import OAuth1Session
import os

def main(*env):
    auth = tweepy.OAuthHandler(env[0], env[1])
    auth.set_access_token(env[2], env[3])
    
    api = tweepy.API(auth)
    
    public_tweets = api.home_timeline()
    
    for tweet in public_tweets:
        print('-------------------------')
        print(tweet.text)

if __name__ == "__main__":
    main(os.environ["CONSUMER_KEY"],
	os.environ["CONSUMER_SECRET"],
	os.environ["ACCESS_TOKEN_KEY"],
	os.environ["ACCESS_TOKEN_SECRET"])
