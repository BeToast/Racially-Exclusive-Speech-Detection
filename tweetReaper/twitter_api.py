import tweepy
import configparser
import requests

import pandas as pd

# read config

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

bearer_token = config['twitter']['bearer_token']

#print('Keys and tokens:\n'+api_key+'\n'+api_key_secret+'\n'+access_token+'\n'+access_token_secret+'\n')



# auth
# auth = tweepy.OAuthHandler(api_key, api_key_secret)
# auth.set_access_token(access_token, access_token_secret)

# # api
# api = tweepy.API(auth)

client = tweepy.Client( bearer_token=bearer_token,
                        consumer_key=api_key,
                        consumer_secret=api_key_secret,
                        access_token=access_token,
                        access_token_secret=access_token_secret,
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

# Define query
query = '(Blue Gums) lang:en'

tweets = client.search_recent_tweets(query=query, max_results=20)

# Save data as dictionary
tweets_dict = tweets.json() 

# Extract "data" value from dictionary
tweets_data = tweets_dict['data'] 
# Transform to pandas Dataframe
df = pd.json_normalize(tweets_data) 
df.to_csv("tweets-maybe-racist.csv")

