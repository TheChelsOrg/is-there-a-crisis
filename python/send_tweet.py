 # importing modules
import tweepy
import os
import json
import time
import random

# secrets 
consumer_key = os.getenv('c_key')
consumer_secret = os.getenv('c_secret')
access_token = os.getenv('a_token')
access_token_secret = os.getenv('a_secret')

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth)

# processing
with open('js/data.json') as data:
 reader = json.loads(data)
 row = random.choice(list(reader))
 api.update_status(status = "#CrisisChelsea Today's crisis at Chelsea is " + row)     
