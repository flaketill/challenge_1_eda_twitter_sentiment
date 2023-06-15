#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*


import os
import pandas as pd
import tweepy
from textblob import TextBlob
import logging, time
from dotenv import load_dotenv # Persistent Virtualenv Environment Variables with python-dotenv


# Step 1 - Authenticate
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)


# Step 2 - Instantiate the tweepy API
api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')