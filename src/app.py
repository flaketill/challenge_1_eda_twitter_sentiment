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
