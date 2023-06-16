#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*

import os
import pandas as pd
import tweepy
from textblob import TextBlob
import logging, time
from dotenv import load_dotenv # Persistent Virtualenv Environment Variables with python-dotenv

load_dotenv()  # take environment variables from .env file

# Configure the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Step 1 - Authenticate
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET_KEY")

access_token = os.getenv("ACCESS_TOKEN") 
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

# Step 2 - Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

# Step 3 - Username

# https://twitter.com/TwitterMexico
username = os.getenv("USERNAME")
no_of_tweets = 100

def run():

	logging.debug('Run a simple text - using Tweepy')

	try:

		##Step 3 - Retrieve Tweets: The number of tweets we want to retrieved from the user
	    tweets = api.user_timeline(screen_name=username, count=no_of_tweets)

	    # Get attributes from the tweet
	    # created_at, favorite_count, source and text
	    attributes_tweet = [[tweet.created_at, tweet.favorite_count, tweet.source, tweet.text] for tweet in tweets]

	    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]

	    #Creation of Dataframe with attributes from the tweet
	    tweets_df = pd.DataFrame(attributes_tweet, columns=columns)

	except BaseException as e:
		logging.debug(f'Invalid or expired token: {e}')
		time.sleep(2)
