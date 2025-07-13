### Todo
- [ ] Check for notifications to fetch mentions every 10 minutes in background
- [ ] Tweets based on trending topics of twitter
- [ ] In every task first fetch the data from twitter and then perform further tasks (fetching should be included in the task)
- [ ] The tasks should be structured as follows:
    - Fetch data from twitter (choose atleast one function from data retrieval functions)
    - Generate content (optional - choose atleast one function from content generation functions only when needed)
    - Perform actions (choose atleast one function from action functions)
    - Content generation (optional - choose atleast one function from content generation functions only when needed)
- [ ] setting chat history of main agent

### Tasks
#### Utility functions
- generate_tweet_content

#### Data retrieval functions
- get_user_tweets
- search_tweets_by_query
- get_trending_topics
- get_user_followers

#### Content generation functions
- generate_tweet_content

#### Action functions
- like_tweets
- comment_on_tweets
- retweet_tweets
- follow_users
- unfollow_users
- generate_replies


