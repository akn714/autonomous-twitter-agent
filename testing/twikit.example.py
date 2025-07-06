# all examples of twikit usage

from twikit import Client
# from twikit.utils import get_user_id
import asyncio
import os
from dotenv import load_dotenv
import sys

# load environment variables
load_dotenv()

# create a client
client = Client(language='en-US')

# login to twitter
async def login():
    await client.login(
        auth_info_1=os.getenv('TWITTER_USERNAME'),
        auth_info_2=os.getenv('TWITTER_EMAIL'),
        password=os.getenv('TWITTER_PASSWORD')
    )

# get user by screen name
async def get_user_by_screen_name():
    user = await client.get_user_by_screen_name('akn714')
    print(user)

# get trends
# async def get_trends(name: str = 'tech'):
#     trends = await client.get_trends()
#     print(trends)

async def get_trends():
    trends = await client.get_trends("tech")
    print("Trending Topics:")
    for trend in trends:
        print(f"- {trend.name}")
    return trends

async def search_tweets():
    tweets = await client.search_tweet('latest research on AGI', 'Latest')

    all_tweets_data = {}
    for tweet in tweets:
        print(f"[+] fetched tweet of {tweet.user.name}")
        all_tweets_data[tweet.user.name] = tweet.text
        # print(f"{tweet.user.name}: {tweet.text}")
    print(all_tweets_data)
    # for tweet in tweets:
    #     print(
    #         tweet.user.name,
    #         tweet.text,
    #         tweet.created_at
    #     )
    
    # print("\nTop Tweets for Trending Topic:")
    # for tweet in search:
    #     print(f"- {tweet.text[:100]}...")  # Print first 100 chars

async def main():
    await login()
    await asyncio.gather(get_trends(), search_tweets())

asyncio.run(main())