
import tweepy



consumer_key = 'TDzEfcM7thNcDUloJTnWHyE8N'
consumer_secret = 'G5O02oFMWxXnU6u0bEE42omZngPH6jHqCpmZ11jMYeFPmyvBbt' 
access_key = '1268005692188868610-sXF1lyWV2GJrUVxKa1JzzSFVXLlrCO' 
access_secret = 'E8n3se4oDzVp01LASmKiAPZxcU6Q1wkKHGb1zlZ1bOuHK' 



def oauth_login(consumer_key, consumer_secret):

    """Authenticate with twitter using OAuth"""

    

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth_url = auth.get_authorization_url()

    

    verify_code = raw_input("Authenticate at %s and then enter you verification code here > " % auth_url) 

    auth.get_access_token(verify_code)

    

    return tweepy.API(auth)



def batch_delete(api):

    for status in tweepy.Cursor(api.user_timeline).items():

       try:

           #api.destroy_status(status.id)

           #print "Deleted:", status.id

           thread.start_new_thread( deleteThread, (api, status.id, ) )

       except:

           print ("Failed to delete:", status.id)



if __name__ == "__main__":

    #authorize twitter, initialize tweepy

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)

    print ("Authenticated as: %s" % api.me().screen_name)

    

    batch_delete(api)
