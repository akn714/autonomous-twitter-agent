## Autonomous Twitter Agent
- An autonomous agent that interacts autonomously with Twitter.
- [resources](https://www.perplexity.ai/search/explain-the-working-of-autonom-Dlf8v61NRwSg4IINbpNs.Q?0=r)

### Todo
- [ ] Check for notifications to fetch mentions every 10 minutes in background
- [ ] Tweets based on trending topics of twitter

### Agents Involved
1. Task Creation Agent - Makes llm request with objective and returns the task, 
2. Task Prioritization Agent - Makes llm request with tasks queue and objective, and returns the prioritized tasks
3. Task Execution Agent - Uses llm and functions to perform a perticular task

**Task Execution Agent**<br>
- Use the twitter api to:
    - get the tweets of the users
    - post the tweets
    - like the tweets
    - retweet the tweets
    - comment on the tweets
    - follow and unfollow the users
- Workflow:
    - Gets a task from the queue
    - Generate a list of functions to be performed to accomplish the task using llm call
    - Calls the functions in the list one by one
    - Stores the results in the last_task_result array

### Workflow of Autonomous Agents ([source](https://resources.parcha.com/deep-dive-part-2-how-does-babyagi/))
1. Give an Objective to the Agent with an initial task
2. Agent will store the initial task in the queue and pass the queue to the Execution Agent
3. Execution Agent will execute the task and store the result in the database for future reference
4. Now the task results and the Objective will be passed to the task creation agent to create new tasks
5. The task creation agent will create new tasks based on the objective and the results of the previous tasks
6. The task creation agent will pass the new tasks to the main agent
7. The main agent will pass the new tasks to the task prioritization agent
8. The task prioritization agent will prioritize the tasks and pass the prioritized tasks to the task execution agent
9. The task execution agent will execute the prioritized tasks and store the results in the database
10. and this will continue until the objective is met

