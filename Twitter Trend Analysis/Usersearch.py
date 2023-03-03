def usf(search_user):
    import os
    import tweepy as tw
    import pandas as pd


    consumer_key= ''
    consumer_secret= ''
    access_token= ''
    access_token_secret= ''

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)


    # Define the search term as variable

    search_user = str(search_user)
    print(search_user) 

    result = api.get_user(search_user)
    
    global x
    global y
    global z
    x = ('Name: ' + result.name)
    y = ('Location: ' + result.location)
    z = ('Friends: ' + str(result.friends_count))

    def pr():
        print(x)
        print(y)
        print(z)

    return pr


        
 
