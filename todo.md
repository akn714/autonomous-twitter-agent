### Todo
- [ ] Check for notifications to fetch mentions every 10 minutes in background
- [ ] Tweets based on trending topics of twitter
- [ ] In every task first fetch the data from twitter and then perform further tasks (fetching should be included in the task)
- [ ] Make a generate_replies function to generate replies to a tweet
```py
def generate_replies(tweets: list[dict], topic: str) -> list[str]:
    """
    params -> tweets -> [
        {
            "id": "1234567890",
            "text": "Tweet text"
        },
        {
            "id": "1234567891",
            "text": "Tweet text"
        }
    ]

    result -> [
        {
            "id": "1234567890",
            "reply": "Reply text"
        },
        {
            "id": "1234567891",
            "reply": "Reply text"
        }
    ]
    """
    pass
```
