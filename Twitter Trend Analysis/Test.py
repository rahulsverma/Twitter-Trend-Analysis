def tta(search_words):
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
    search_words = str(search_words)
    print(search_words)

    # Collect tweets
    tweets = tw.Cursor(api.search,
                        q=search_words,
                        lang="en").items(100)

        
    users_locs = [[tweet.user.screen_name, tweet.text, tweet.user.location, tweet.created_at] for tweet in tweets]
    users_locs

    tweet_text = pd.DataFrame(data=users_locs, 
                        columns=['User',"Tweet", "Location", "Date"])
    print(tweet_text)
    import dfgui as df
    df.show(tweet_text)