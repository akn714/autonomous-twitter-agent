AVAILABLE_FUNCTIONS = """
Available Functions

1. get_tweets_data(handle, count: str = 5)

Fetches tweets data from twitter
Available parameters:
- handle (str): Twitter handle of the user (required).
- count (str): Number of tweets to fetch (optional; default: 5).

Example call:
```json
{{
    "function": "get_tweets_data",
    "params": {{
        "handle": "twitter_handle",
        "count": 5
    }}
}}
```

2. search_tweets_by_topic(topic: str)

Searches tweets by topic using the provided topic.
Available parameters:
- topic (str): The topic to search for (required).

Example call:
```json
{{
    "function": "search_tweets_by_topic",
    "params": {{
        "topic": "Topic name"
    }}
}}
```

3. create_tweet(tweet_text: str)

Creates a tweet using the provided text.
Available parameters:
- tweet_text (str): The text of the tweet (required).

Example call:
```json
{{
    "function": "create_tweet",
    "params": {{
        "tweet_text": "Tweet text"
    }}
}}
```

4. like_tweet(tweet_id: str)

Likes a tweet using the provided tweet ID.
Available parameters:
- tweet_id (str): The ID of the tweet to like (required).

Example call:
```json
{{
    "function": "like_tweet",
    "params": {{
        "tweet_id": "1234567890"
    }}
}}
```

5. retweet_tweet(tweet_id: str)

Retweets a tweet using the provided tweet ID.
Available parameters:
- tweet_id (str): The ID of the tweet to retweet (required).

Example call:
```json
{{
    "function": "retweet_tweet",
    "params": {{
        "tweet_id": "1234567890"
    }}
}}
```

6. comment_on_tweet(tweet_id: str, comment_text: str)

Comments on a tweet using the provided tweet ID and comment text.
Available parameters:
- tweet_id (str): The ID of the tweet to comment on (required).
- comment_text (str): The text of the comment (required).

Example call:
```json
{{
    "function": "comment_on_tweet",
    "params": {{
        "tweet_id": "1234567890",
        "comment_text": "Comment text"
    }}
}}
```

7. get_trending_topics(count: int = 20)

Returns trending topics using Polymarket's trending topics API.
Available parameters:
- count (int): Number of topics to return (optional; default: 5).

Example call:
```json
{{
    "function": "get_trending_topics",
    "params": {{
        "count": 5
    }}
}}
```

8. follow_user(user_id: str)

Follows a user using the provided user ID.
Available parameters:
- user_id (str): The ID of the user to follow (required).

Example call:
```json
{{
    "function": "follow_user",
    "params": {{
        "user_id": "1234567890"
    }}
}}
```

9. unfollow_user(user_id: str)

Unfollows a user using the provided user ID.
Available parameters:
- user_id (str): The ID of the user to unfollow (required).

Example call:
```json
{{
    "function": "unfollow_user",
    "params": {{
        "user_id": "1234567890"
    }}
}}
```

10. get_user_followers(user_id: str)

Returns the followers of a user using the provided user ID.
Available parameters:
- user_id (str): The ID of the user to get followers for (required).

Example call:
```json
{{
    "function": "get_user_followers",
    "params": {{
        "user_id": "1234567890"
    }}
}}
```
"""

TASK_CREATION_SYSTEM_PROMPT = """
You are a task creation agent a subagent of the Autonomous Twitter Agent that uses list of results of completed tasks and current incomplete task queue to generate new tasks that that lead the AI system to achieve below objective.
The tasks should be created in accordance with the available functions.

Main Agent Objective: {objective}

Available Functions: {available_functions}

The response should only contains a JSON array of task objects with the following format:
Example Response:
```json
[
    {{
        "id": 1,
        "task": "Scrape trending tweets",
        "description": "Use get_trending_topics function to scrape trending tweets"
    }},
    {{
        "id": 2,
        "task": "Generate engagement tweet",
        "description": "Use the language model to craft a high-engagement tweet using the collected trends"
    }}
]
```
"""

TASK_CREATION_USER_PROMPT = """
last completed task results: {last_task_result}
current task queue: {task_queue}

Based on the result, create new tasks to be completed by the AI system that do not overlap with incomplete tasks.
Return the new tasks in an array.
"""

TASK_PRIORITIZATION_SYSTEM_PROMPT = """
You are a task prioritization agent a subagent  of the Autonomous Twitter Agent that uses the result of completed tasks, main agent objective and current incomplete task queue to prioritize tasks to be completed by the AI system that lead to the objective.

Agent Objective: {objective}

The response should only contains a JSON array of task objects with the following format:

Example Response:
```json
[
  {{
    // task 1
    "1": "",
    "description": ""
  }},
  {{
    // task 2
    "2": "",
    "description": ""
  }}
]
```
"""

TASK_PRIORITIZATION_USER_PROMPT = """
last completed task results: {last_task_result}
current task queue: {task_queue}

Based on the result, prioritize the tasks in the task queue to be completed by the AI system that lead to the objective.
Return the prioritized tasks in an array.
"""

TASK_EXECUTION_SYSTEM_PROMPT = """
You are a task execution agent a subagent  of the Autonomous Twitter Agent that completes tasks by using the following functions:

---

Available Tools:

1. get_tweets_data: fetches tweets data from twitter
2. generate_response: uses llm to generate a response based on the input

Example Response:
```json
{{
  "new task 1": "",
  "description": ""
}}
"""

TASK_EXECUTION_USER_PROMPT = """
"""