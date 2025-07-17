import os
import json
import asyncio
from dotenv import load_dotenv

from utils.llm import llm
from utils.parser import Parser

load_dotenv()

class Twitter:
    def __init__(self):
        print('[+] Initializing Twitter')
        self.parser = Parser()

    # def __init__(self, username, password, client):
    #     self.username = username
    #     self.password = password
    #     self.client = client
    
    def like_tweets(self, tweets):
        for tweet in tweets:
            self.like_tweet(tweet.id)
    
    async def comment_on_tweets(self, tweets):
        """
        tweets -> list[tweet]
        tweet -> {
            id: str,
            text: str
        }
        """
        for tweet in tweets:
            comment_text = self.generate_reply(tweet.text)
            await self.comment_on_tweet(tweet.id, comment_text)
        return {"status": "success"}

    def generate_reply(self, tweet_text):
        try:
            messages = [
                {
                    "role": "user",
                    "content": """
                        Reply to this tweet:

                        tweet_text: {tweet_text}

                        The reponse should only contain a JSON with the following key:
                        example:
                        ```json
                        {{
                            "tweet_content": "Tweet content"
                        }}
                        ```
                    """
                }
            ]
            response = llm.get_llm_response(messages)

            return self.parser.extract_json_from_text(response)
        except Exception as e:
            pritn(f"[!] Failed to generate reply: {e}")

    def generate_tweet_content(self, topic):
        try:
            messages = [
                {
                    "role": "user",
                    "content": """
                        Write a tweet that sounds like it comes from a mind untethered by reality. The tone should be a mix of maverick rebellion, transcendent wisdom, esoteric symbolism, and paracosmic imagination.
                        Avoid cliches and hashtags. Embrace poetic ambiguity, surreal metaphors, and cryptic truths that spark thought.
                        # The tweet should feel like a coded message from another verse — like a whisper from a dimension only a few can hear.
                        Limit: 280 characters.
                        Style inspirations: Jungian dreams, Blade Runner monologues, quantum mysticism, ancient myths warped through a futuristic lens.
                    """
                }
            ]
            response = llm.get_llm_response(messages)
            print(response)
            return response
        except Exception as e:
            print(f"[!] Failed to generate tweet content: {e}")
            return { "error": f"Failed to generate tweet content: {e}" }

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
            response = []
            for tweet in tweets:
                response.append({
                    "id": tweet.id,
                    "text": tweet.text
                })
            return response
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
            trends = await self.client.get_trends("trending", retry=True)
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
