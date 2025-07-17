import os
import json
import asyncio
from dotenv import load_dotenv

from utils.llm import llm
from utils.parser import Parser

load_dotenv()

class Twitter:
    def __init__(self, client):
        print('[+] Initializing Twitter...')
        self.parser = Parser()
        self.llm = llm
        # self.client = Client(language='en-US')
        self.client = client
    
    # Utility functions
    def generate_reply(self, tweet_text) -> dict: # done
        try:
            print('[generate_reply] tweet_text:', tweet_text)
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
            response = self.llm.get_llm_response(messages)

            return self.parser.extract_json_from_text(response)
        except Exception as e:
            print(f"[!] Failed to generate reply: {e}")
            return { "error": f"Failed to generate reply: {e}" }
    def generate_tweet_content(self, topic) -> dict: # done
        try:
            print('[generate_tweet_content] topic:', topic)
            messages = [
                {
                    "role": "user",
                    "content": """
                        Write a tweet that sounds like it comes from a mind untethered by reality. The tone should be a mix of maverick rebellion, transcendent wisdom, esoteric symbolism, and paracosmic imagination.
                        Avoid cliches and hashtags. Embrace poetic ambiguity, surreal metaphors, and cryptic truths that spark thought.
                        # The tweet should feel like a coded message from another verse — like a whisper from a dimension only a few can hear.
                        Limit: 280 characters.
                        Style inspirations: Jungian dreams, Blade Runner monologues, quantum mysticism, ancient myths warped through a futuristic lens.

                        The reponse should only contain a JSON with the following key:
                        example:
                        ```json
                        {{
                            "tweet_content": "Tweet content"
                        }}
                    """
                }
            ]
            response = self.parser.extract_json_from_text(self.llm.get_llm_response(messages))
            # print(response)
            return response
        except Exception as e:
            print(f"[!] Failed to generate tweet content: {e}")
            return { "error": f"Failed to generate tweet content: {e}" }

    # Data retrieval funtions
    def get_user_tweets(self, handle="unknown", count=5) -> list[dict]: # done
        try:
            user = await self.client.get_user_by_screen_name(handle)
            print('[get_user_tweets] username:', handle)
            tweets = await user.get_tweets(count=count)
            return tweets
        except Exception as e:
            print(f"[!] Failed to fetch tweets for '{handle}': {e}")
            return { "error": f"Failed to fetch tweets for '{handle}': {e}" }
    def search_tweets_by_query(self, query) -> list[dict]: # done
        try:
            response = await self.client.search_tweet(query, 'Latest')
            tweets = []
            print('[search_tweets_by_query] query:', query)
            for tweet in response:
                tweets.append({
                    "id": tweet.id,
                    "text": tweet.text
                })
            return tweets
        except Exception as e:
            print(f"[!] Failed to search tweets with query '{query}': {e}")
            return { "error": f"Failed to search tweets with query '{query}': {e}" }
    def get_trending_topics(self, count=10) -> dict[str, list[str]]: # done
        try:
            print('[get_trending_topics] count:', count)
            trends = await self.client.get_trends("trending", retry=True)
            return trends
        except Exception as e:
            print(f"[!] Failed to get trending topics: {e}")
            return { "error": f"Failed to get trending topics: {e}" }
    def get_user_followers(self, user_id) -> list[dict]: # done
        try:
            print('[get_user_followers] user_id:', user_id)
            user = await self.client.get_user_by_id(user_id)
            followers = await user.get_followers()
            return followers
        except Exception as e:
            print(f"[!] Failed to get followers of user {user_id}: {e}")
            return { "error": f"Failed to get followers of user {user_id}: {e}" }

    # Functions to interact with multiple tweets
    def like_tweets(self, tweets) -> dict[str, str]: # done
        print('[like_tweets]')
        for tweet in tweets:
            self.like_tweet(tweet['id'])
        return {"status": "success"}
    def comment_on_tweets(self, tweets) -> dict[str, str]: # done
        """
        tweets -> list[tweet]
        tweet -> {
            id: str,
            text: str
        }
        """
        print('[comment_on_tweets]')
        for tweet in tweets:
            self.comment_on_tweet(tweet['id'], tweet['text'])
        return {"status": "success"}
    def retweet_tweets(self, tweets) -> dict[str, str]: # done
        print('[retweet_tweets]')
        for tweet in tweets:
            self.retweet_tweet(tweet['id'])
        return {"status": "success"}
    def follow_users(self, users) -> dict[str, str]: # done
        print('[follow_users]')
        for user in users:
            self.follow_user(user['id'])
        return {"status": "success"}
    def unfollow_users(self, users) -> dict[str, str]: # done
        print('[unfollow_users]')
        for user in users:
            self.unfollow_user(user['id'])
        return {"status": "success"}
    def generate_replies(self, tweets) -> dict[str, str]: # done
        print('[generate_replies]')
        for tweet in tweets:
            reply_text = self.generate_reply(tweet['text'])
            print(f"[generate_replies] replying {tweet['id']}: {reply_text}")
        return {"status": "success"}

    # Functions to interact with single tweet
    def create_tweet(self, tweet_text) -> dict[str, str]: # done
        # todo: rename this func to post_tweet and also createing post_tweets function
        try:
            tweet_content = self.generate_tweet_content(tweet_text)
            tweet = await self.client.create_tweet(text=tweet_content)
            print(f"[create_tweet] tweet posted: {tweet}")
            return tweet
        except Exception as e:
            print(f"[!] Failed to create tweet: {e}")
            return { "error": f"Failed to create tweet: {e}" }
    def like_tweet(self, tweet_id) -> dict[str, str]: # done
        try:
            await self.client.like_tweet(tweet_id)
            print(f"[like_tweet] Liked tweet {tweet_id}")
        except Exception as e:
            print(f"[!] Failed to like tweet {tweet_id}: {e}")
            return { "error": f"Failed to like tweet {tweet_id}: {e}" }
    def retweet_tweet(self, tweet_id) -> dict[str, str]: # done
        try:
            await self.client.retweet(tweet_id)
            print(f"[retweet_tweet] Retweeted tweet {tweet_id}")
        except Exception as e:
            print(f"[!] Failed to retweet tweet {tweet_id}: {e}")
            return { "error": f"Failed to retweet tweet {tweet_id}: {e}" }
    def comment_on_tweet(self, tweet_id, tweet_text) -> dict[str, str]: # done
        try:
            comment_text = self.generate_reply(tweet_text)
            await self.client.create_tweet(
                text=comment_text,
                in_reply_to_tweet_id=tweet_id
            )
            print(f'[comment_on_tweet] tweet.id:{tweet_id} reply: {comment_text["tweet_content"]}')
        except Exception as e:
            print(f"[!] Failed to comment on tweet {tweet_id}: {e}")
            return { "error": f"Failed to comment on tweet {tweet_id}: {e}" }

    # User interactions
    def follow_user(self, user_id) -> dict[str, str]: # done
        try:
            await self.client.follow_user(user_id)
            print(f"[follow_user] Followed user {user_id}")
            return {"status": "success"}
        except Exception as e:
            print(f"[!] Failed to follow user {user_id}: {e}")
            return { "error": f"Failed to follow user {user_id}: {e}" }
    def unfollow_user(self, user_id) -> dict[str, str]: # done
        try:
            await self.client.unfollow_user(user_id)
            print(f"[unfollow_user] Unfollowed user {user_id}")
            return {"status": "success"}
        except Exception as e:
            print(f"[!] Failed to unfollow user {user_id}: {e}")
            return { "error": f"Failed to unfollow user {user_id}: {e}" }