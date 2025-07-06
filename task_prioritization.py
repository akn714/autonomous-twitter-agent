# task prioritization - uses llm to prioritize tasks

import os
import json
from dotenv import load_dotenv

from llm import llm
from prompts import TASK_PRIORITIZATION_SYSTEM_PROMPT, TASK_PRIORITIZATION_USER_PROMPT
from parser import Parser

load_dotenv()

class TaskPrioritizationAgent:
    def __init__(self):
        print('[+] Initializing Task Prioritization Agent')
        self.system_prompt = TASK_PRIORITIZATION_SYSTEM_PROMPT
        self.user_prompt = TASK_PRIORITIZATION_USER_PROMPT

        self.parser = Parser()
        self.llm = llm

    def prioritize_tasks(self, tasks_queue, objective):
        print('[+] Prioritizing tasks')
        
        messsages = [
            {
                'role': 'system',
                'content': self.system_prompt.format(objective=objective)
            },
            {
                'role': 'user',
                'content': self.user_prompt.format(task_queue=tasks_queue, last_task_result=last_task_result)
            }
        ]

        response = llm.get_llm_response(messages)
        response = parser.extract_json_from_text(response)

        return response