def cst(country):
    import twitter 
    import pandas as pd
    import tweepy

    consumer_key= ''
    consumer_secret= ''
    access_token= ''
    access_token_secret= ''

    auth = twitter.oauth.OAuth(access_token, access_token_secret,
                           consumer_key, consumer_secret)

    twitter_api = twitter.Twitter(auth=auth) 

    # http://woeid.rosselliot.co.nz/lookup/india
    India = 23424848   
    Canada = 23424803
    Ireland = 23424975 
    Philadelphia = 2471217  

    country_mapping =  {"India":23424848,
             "Canada":23424803, "Ireland":23424975, "Philadelphia":2471217}

    country = str(country_mapping[country])



    # https://developer.twitter.com/en/docs/trends/trends-for-location/api-reference/get-trends-place
    trendsinworld = twitter_api.trends.place(_id=country)
 

    for trending in trendsinworld[0]['trends']:
        print(trending['name'])



