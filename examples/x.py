import os
import httpx
import asyncio
from twikit import Client
from dotenv import load_dotenv
from httpx import Headers, Timeout

load_dotenv()

original_async_client_init = httpx.AsyncClient.__init__

def patched_async_client_init(self, *args, **kwargs):
    headers = kwargs.get("headers", Headers())
    headers["User-Agent"] = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/128.0.0.0 Safari/537.36"
    )
    kwargs["headers"] = headers

    if "timeout" not in kwargs:
        kwargs["timeout"] = Timeout(20.0)

    original_async_client_init(self, *args, **kwargs)

httpx.AsyncClient.__init__ = patched_async_client_init

x_handles = [
  "OpenAI",
  "GoogleAI",
  "DeepMind",
  "NVIDIAAI",
  "AnthropicAI"
]

client = Client(language='en-US')

async def x_login(USERNAME, EMAIL, PASSWORD):
    print('[+] LOGGING IN TO TWITTER')
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD
    )

async def get_tweets_data():
    print('[+] Fetching tweets data')
    tweets_data = {}
    
    for user in x_handles:
        print(f'[+] fetching tweets of {user}')
        try:
            u = await client.get_user_by_screen_name(user)
            tweets = await client.get_user_tweets(user_id=u.id, tweet_type='Tweets', count=5)
            print(len(tweets))
            trending_topics = await client.get_trending_topics(count=5)
            tweets_data[user] = [tweet.text for tweet in tweets[:5]]
        except Exception as e:
            print('[-] Error fetching tweets')
            continue
    return tweets_data

async def list_data():
    data = await get_tweets_data()
    print(data)

# running asyncronous function
asyncio.run(list_data())
