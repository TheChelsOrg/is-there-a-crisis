 # importing modules
import tweepy
import json
import time
import random
import pathlib
import re
import os

# setup
root = pathlib.Path(__file__).parent.parent.resolve()

# secrets 
consumer_key = os.getenv('c_key')
consumer_secret = os.getenv('c_secret')
access_token = os.getenv('a_token')
access_token_secret = os.getenv('a_secret')

# functions
def replace_chunk(content, marker, chunk):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    chunk = "<!-- {} starts -->\n{}\n<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth)

# processing
with open('js/data.json') as data:
 reader = json.loads(data)
 data_item = random.choice(list(reader))
 

if __name__ == "__main__":
    readme = root / "README.md"
    readme_contents = readme.open().read()
    rewritten = replace_chunk(readme_contents, "crisis_item", data_item)
    readme.open("w").write(rewritten)

    api.update_status(status = "#CrisisChelsea Today's crisis at Chelsea is " + data_item)     
