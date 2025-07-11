import os
import json
import asyncio
from dotenv import load_dotenv

from utils.llm import llm
from utils.parser import Parser

load_dotenv()

class Twitter:
    def __init__(self):
        print('[+] Initializing Twitter...')
        self.parser = Parser()
        self.llm = llm
    
    # Utility functions
    def generate_reply(self, tweet_text) -> dict:
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
    def generate_tweet_content(self, topic) -> dict:
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
    def get_user_tweets(self, handle="unknown", count=5) -> list[dict]:
        try:
            print('[get_user_tweets] username:', handle)
            tweets = [
                {
                    "id": 829342,
                    "text": "tweet 1"
                },
                {
                    "id": 984523,
                    "text": "tweet 2"
                }
            ]
            return tweets
        except Exception as e:
            print(f"[!] Failed to fetch tweets for '{handle}': {e}")
            return { "error": f"Failed to fetch tweets for '{handle}': {e}" }
    def search_tweets_by_query(self, query) -> list[dict]:
        try:
            print('[search_tweets_by_query] query:', query)
            tweets = [
                {
                    "id": 289347,
                    "text": "tweet 1"
                },
                {
                    "id": 798723,
                    "text": "tweet 2"
                }
            ]
            return tweets
        except Exception as e:
            print(f"[!] Failed to search tweets with query '{query}': {e}")
            return { "error": f"Failed to search tweets with query '{query}': {e}" }
    def get_trending_topics(self, count=10) -> dict[str, list[str]]:
        try:
            print('[get_trending_topics] count:', count)
            trends = {
                "topics":["AGI", "Cognitive Architecture", "AI", "Autonomous Agents"]
            }
            return trends
        except Exception as e:
            print(f"[!] Failed to get trending topics: {e}")
            return { "error": f"Failed to get trending topics: {e}" }
    def get_user_followers(self, user_id) -> list[dict]:
        try:
            print('[get_user_followers] user_id:', user_id)
            followers = [
                {
                    "id": 829342,
                    "name": "user1"
                },
                {
                    "id": 984523,
                    "name": "user2"
                }
            ]
            return followers
        except Exception as e:
            print(f"[!] Failed to get followers of user {user_id}: {e}")
            return { "error": f"Failed to get followers of user {user_id}: {e}" }

    # Functions to interact with multiple tweets
    def like_tweets(self, tweets) -> dict[str, str]:
        print('[like_tweets]')
        for tweet in tweets:
            self.like_tweet(tweet['id'])
        return {"status": "success"}
    def comment_on_tweets(self, tweets) -> dict[str, str]:
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
    def retweet_tweets(self, tweets) -> dict[str, str]:
        print('[retweet_tweets]')
        for tweet in tweets:
            self.retweet_tweet(tweet['id'])
        return {"status": "success"}
    def follow_users(self, users) -> dict[str, str]:
        print('[follow_users]')
        for user in users:
            self.follow_user(user['id'])
        return {"status": "success"}
    def unfollow_users(self, users) -> dict[str, str]:
        print('[unfollow_users]')
        for user in users:
            self.unfollow_user(user['id'])
        return {"status": "success"}
    def generate_replies(self, tweets) -> dict[str, str]:
        print('[generate_replies]')
        for tweet in tweets:
            reply_text = self.generate_reply(tweet['text'])
            print(f"[generate_replies] replying {tweet['id']}: {reply_text}")
        return {"status": "success"}

    # Functions to interact with single tweet
    def create_tweet(self, tweet_text) -> dict[str, str]:
        try:
            tweet_content = self.generate_tweet_content(tweet_text)
            print(f"[create_tweet] tweet posted: {tweet_content}")
        except Exception as e:
            print(f"[!] Failed to create tweet: {e}")
            return { "error": f"Failed to create tweet: {e}" }
    def like_tweet(self, tweet_id) -> dict[str, str]:
        try:
            print(f"[like_tweet] Liked tweet {tweet_id}")
        except Exception as e:
            print(f"[!] Failed to like tweet {tweet_id}: {e}")
            return { "error": f"Failed to like tweet {tweet_id}: {e}" }
    def retweet_tweet(self, tweet_id) -> dict[str, str]:
        try:
            print(f"[retweet_tweet] Retweeted tweet {tweet_id}")
        except Exception as e:
            print(f"[!] Failed to retweet tweet {tweet_id}: {e}")
            return { "error": f"Failed to retweet tweet {tweet_id}: {e}" }
    def comment_on_tweet(self, tweet_id, comment_text) -> dict[str, str]:
        try:
            comment_text = self.generate_reply(comment_text)
            print(f'[comment_on_tweet] tweet.id:{tweet_id} reply: {comment_text["tweet_content"]}')
        except Exception as e:
            print(f"[!] Failed to comment on tweet {tweet_id}: {e}")
            return { "error": f"Failed to comment on tweet {tweet_id}: {e}" }

    # User interactions
    def follow_user(self, user_id) -> dict[str, str]:
        try:
            print(f"[follow_user] Followed user {user_id}")
            return {"status": "success"}
        except Exception as e:
            print(f"[!] Failed to follow user {user_id}: {e}")
            return { "error": f"Failed to follow user {user_id}: {e}" }
    def unfollow_user(self, user_id) -> dict[str, str]:
        try:
            print(f"[unfollow_user] Unfollowed user {user_id}")
            return {"status": "success"}
        except Exception as e:
            print(f"[!] Failed to unfollow user {user_id}: {e}")
            return { "error": f"Failed to unfollow user {user_id}: {e}" }