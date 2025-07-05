# all examples of twikit usage

from twikit import Client
from twikit.utils import get_user_id
import asyncio
import os
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
async def get_trends(name: str = 'tech'):
    trends = await client.get_trends()
    print(trends)