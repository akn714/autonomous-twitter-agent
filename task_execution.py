# task execution - use twikit to perform tasks related to twitter

import os
import json
from dotenv import load_dotenv
from twikit import Client
# from twikit.errors import TwiException

from llm import llm
from prompts import TASK_EXECUTION_SYSTEM_PROMPT, TASK_EXECUTION_USER_PROMPT
from  parser import Parser

load_dotenv()

class TaskExecutionAgent:
    def __init__(self):
        print('[+] Initializing Task Execution Agent')
        self.system_prompt = TASK_EXECUTION_SYSTEM_PROMPT
        self.user_prompt = TASK_EXECUTION_USER_PROMPT

        self.client = Client(language='en-US')
        self.parser = Parser()
        self.llm = llm
    
    async def x_login(self, USERNAME, EMAIL, PASSWORD):
        print('[+] LOGGING IN TO TWITTER')
        self.client.login(
            auth_info_1=USERNAME,
            auth_info_2=EMAIL,
            password=PASSWORD
        )
    
    async def get_tweets_data(self):
        pass
    
    async def search_tweets_by_topic(self, topic):
        pass

    async def create_tweet(self, tweet_text):
        pass

    async def like_tweet(self, tweet_id):
        pass

    async def retweet_tweet(self, tweet_id):
        pass

    async def comment_on_tweet(self, tweet_id, comment_text):
        pass

    async def get_trending_topics(self, count):
        pass

    async def follow_user(self, user_id):
        pass
    
    async def unfollow_user(self, user_id):
        pass
    
    async def get_user_followers(self, user_id):
        pass
    
    async def search_tweets():
        tweets = await client.search_tweet('python', 'Latest')

        # for tweet in tweets:
        #     print(
        #         tweet.user.name,
        #         tweet.text,
        #         tweet.created_at
        #     )

        return tweets
