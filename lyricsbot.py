
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
lyrics = lyrics.split("\n")

x = 1
while x < 2:
    y = random.randint(0,len(lyrics))
    print(lyrics[y])
    api.update_status(lyrics[y])
    time.sleep(1800)

new_followers = API.followers(user)

for i in new_followers:
    newDM = raw_input (i.from_user + "send follower DM?" + "Y/N" )
    if newDM.lower() == "n":
        print i.from_user + " was not messaged"
        print "Now returning to the Main Menu."
else:
    api.send_direct_message(user_id = i.from_user, text = "Hi there! I'm a new bot on twitter and I was wondering if you'd take the time to share my account around! Maybe that would make the 4 hours of code worth it :)")
    print "You messaged " + i.from_user
