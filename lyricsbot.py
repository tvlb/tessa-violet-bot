

'''tessa violet lyrics bot'''

import time
import random
import tweepy

from confidential import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

lyricfile = open("lyrics.txt", "r")
lyrics=lyricfile.read()
lyrics = lyrics.split(",")

x = 1
while x < 2:
    try:
        while x < 2:
            y = random.randint(0,len(lyrics))
            print(lyrics[y])
            api.update_status(lyrics[y])
            time.sleep(1800)
    except:
        pass
