# main loop

import os
import json
import asyncio
from dotenv import load_dotenv

from task_creation import TaskCreationAgent
from task_prioritization import TaskPrioritizationAgent 
from task_execution import TaskExecutionAgent

load_dotenv()

AGENT_OBJECTIVE = "Reach 1000 followers on Twitter"
INITIAL_TASK = "Create a tweet based on your purpose"

class Agent:
    def __init__(self, USERNAME, EMAIL, PASSWORD):
        print('[+] Initializing Main Agent')
        self.tasks_queue = []
        self.last_task_result = []
        self.objective = AGENT_OBJECTIVE
        self.task_creation_agent = TaskCreationAgent()
        self.task_prioritization_agent = TaskPrioritizationAgent()
        self.task_execution_agent = TaskExecutionAgent()

        # asyncio.run(self.task_execution_agent.x_login(USERNAME, EMAIL, PASSWORD))

    def add_task(self, task):
        self.tasks_queue.append(task)

    def get_tasks(self):
        return self.tasks_queue
    
    def run(self):
        print('[+] Running agent')
        while True:
            new_tasks = self.task_creation_agent.create_tasks(
                self.objective,
                self.tasks_queue,
                self.last_task_result
            )
            
            for task in new_tasks:
                self.tasks_queue.append(task)
            print(self.tasks_queue)
            # self.task_prioritization_agent.prioritize_tasks(self.tasks_queue, self.objective)
            # self.task_execution_agent.execute_tasks(self.tasks_queue, self.objective)

username = os.getenv("TWITTER_USERNAME")
email = os.getenv("TWITTER_EMAIL")
password = os.getenv("TWITTER_PASSWORD")

agent = Agent(username, email, password)
agent.run()
