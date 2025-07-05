import schedule
import time

def daily_tweet():
    client.create_tweet("Another day, another AI thread ☀️🧵")

schedule.every().day.at("10:00").do(daily_tweet)

while True:
    schedule.run_pending()
    time.sleep(60)
