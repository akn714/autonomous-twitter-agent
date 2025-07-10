# task creation - uses llm to create new tasks

import os
import json
from dotenv import load_dotenv

from utils.llm import llm
from utils.prompts import AVAILABLE_FUNCTIONS, TASK_CREATION_SYSTEM_PROMPT, TASK_CREATION_USER_PROMPT
from utils.parser import Parser

load_dotenv()

class TaskCreationAgent:
    def __init__(self):
        print('[+] Initializing Task Creation Agent')
        self.system_prompt = TASK_CREATION_SYSTEM_PROMPT
        self.user_prompt = TASK_CREATION_USER_PROMPT

        self.parser = Parser()
        self.llm = llm

    def create_tasks(self, objective, tasks_queue, last_task_result):
        print('[crete_tasks] Creating new tasks')

        messages = [
            {
                "role": "system",
                "content": self.system_prompt.format(objective=objective, available_functions=AVAILABLE_FUNCTIONS)
            },
            {
                "role": "user",
                "content": self.user_prompt.format(task_queue=tasks_queue, last_task_result=last_task_result)
            }
        ]

        response = self.llm.get_llm_response(messages)
        print(response)
        response = self.parser.extract_json_from_text(response)

        return response
