# main loop

import os
import json
import asyncio
from dotenv import load_dotenv

from tasks.creation import TaskCreationAgent
from tasks.prioritization import TaskPrioritizationAgent 
from tasks.execution import TaskExecutionAgent

load_dotenv()

AGENT_OBJECTIVE = "Reach 1000 followers on Twitter"
INITIAL_TASK = {
    "task": "Create a tweet based on your purpose",
    "description": "Use the generate_tweet_content function to generate a tweet based on your purpose."
}
class Agent:
    def __init__(self, USERNAME, EMAIL, PASSWORD):
        print('[+] Initializing Main Agent')
        self.tasks_queue = []
        self.last_task_results = []
        self.objective = AGENT_OBJECTIVE
        self.task_creation_agent = TaskCreationAgent()
        self.task_prioritization_agent = TaskPrioritizationAgent()
        self.task_execution_agent = TaskExecutionAgent()

        self.tasks_queue.append(INITIAL_TASK)
        # asyncio.run(self.task_execution_agent.x_login(USERNAME, EMAIL, PASSWORD))

    def add_task(self, task):
        self.tasks_queue.append(task)

    def get_tasks(self):
        return self.tasks_queue
    
    def run(self):
        print('[+] Running agent...\n\n')
        while True:
            new_task = self.task_creation_agent.create_tasks(
                self.objective,
                self.tasks_queue,
                self.last_task_results
            )
            
            # for task in new_tasks:
            self.tasks_queue.append(new_task)

            print("\n\n\n")
            print("[ TASK QUEUE START ]".center(46, "="))
            print(self.tasks_queue)
            print("[ TASK QUEUE END ]".center(46, "="))
            print("\n\n\n")
            # self.task_prioritization_agent.prioritize_tasks(self.tasks_queue, self.objective)
            self.task_execution_agent.execute_tasks(self.tasks_queue)
            self.tasks_queue.clear()

username = os.getenv("TWITTER_USERNAME")
email = os.getenv("TWITTER_EMAIL")
password = os.getenv("TWITTER_PASSWORD")

agent = Agent(username, email, password)
agent.run()
