# task execution - use twikit to perform tasks related to twitter

from twikit import Client
# from twikit.errors import TwiException

from llm import llm
from prompts import TASK_EXECUTION_SYSTEM_PROMPT, TASK_EXECUTION_USER_PROMPT
from  parser import Parser

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
    
    async def get_tweets_data(self, username):
        try:
            user = await self.client.get_user_by_screen_name(username)
            tweets = await self.client.get_user_tweets(user_id=user.id, tweet_type='Tweets', count=5)
            return tweets
        except Exception as e:
            print(f"[!] Failed to fetch tweets for '{username}': {e}")
            return { "error": f"Failed to fetch tweets for '{username}': {e}" }
    
    async def search_tweets_by_query(self, query):
        try:
            tweets = await self.client.search_tweet(query, 'Latest')
            return tweets
        except Exception as e:
            print(f"[!] Failed to search tweets with query '{query}': {e}")
            return { "error": f"Failed to search tweets with query '{query}': {e}" }

    async def create_tweet(self, tweet_text):
        try:
            tweet = await self.client.create_tweet(text=tweet_text)
            return tweet
        except Exception as e:
            print(f"[!] Failed to create tweet: {e}")
            return { "error": f"Failed to create tweet: {e}" }

    async def like_tweet(self, tweet_id):
        try:
            return await self.client.like_tweet(tweet_id)
        except Exception as e:
            print(f"[!] Failed to like tweet {tweet_id}: {e}")
            return { "error": f"Failed to like tweet {tweet_id}: {e}" }

    async def retweet_tweet(self, tweet_id):
        try:
            return await self.client.retweet(tweet_id)
        except Exception as e:
            print(f"[!] Failed to retweet tweet {tweet_id}: {e}")
            return { "error": f"Failed to retweet tweet {tweet_id}: {e}" }

    async def comment_on_tweet(self, tweet_id, comment_text):
        try:
            return await self.client.create_tweet(
                text=comment_text,
                in_reply_to_tweet_id=tweet_id
            )
        except Exception as e:
            print(f"[!] Failed to comment on tweet {tweet_id}: {e}")
            return { "error": f"Failed to comment on tweet {tweet_id}: {e}" }

    async def get_trending_topics(self, count=10):
        try:
            trends = await self.client.get_trends("Worldwide")
            return trends[:count]
        except Exception as e:
            print(f"[!] Failed to get trending topics: {e}")
            return { "error": f"Failed to get trending topics: {e}" }

    async def follow_user(self, user_id):
        try:
            return await self.client.follow_user(user_id)
        except Exception as e:
            print(f"[!] Failed to follow user {user_id}: {e}")
            return { "error": f"Failed to follow user {user_id}: {e}" }

    async def unfollow_user(self, user_id):
        try:
            return await self.client.unfollow_user(user_id)
        except Exception as e:
            print(f"[!] Failed to unfollow user {user_id}: {e}")
            return { "error": f"Failed to unfollow user {user_id}: {e}" }

    async def get_user_followers(self, user_id):
        try:
            user = await self.client.get_user_by_id(user_id)
            followers = await user.get_followers()
            return followers
        except Exception as e:
            print(f"[!] Failed to get followers of user {user_id}: {e}")
            return { "error": f"Failed to get followers of user {user_id}: {e}" }

    async def search_tweets():
        tweets = await client.search_tweet('python', 'Latest')

        # for tweet in tweets:
        #     print(
        #         tweet.user.name,
        #         tweet.text,
        #         tweet.created_at
        #     )

        return tweets
