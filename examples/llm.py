import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class GroqLLM:
    model = "llama-3.3-70b-versatile"

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def get_llm_response(self, messages):
        print('[+] Groq LLM responding')
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        output = response.choices[0].message.content.strip()

        if output and (output[0] == output[-1]) and output.startswith(("'", '"')):
            output = output[1:-1]

        return output

SYSTEM_PROMPT = """ """.strip()

USER_PROMPT = """
{data}
""".strip()

def generate_response(tweets_data):
    print('[+] Generating updates')
    llm = GroqLLM()

    messages = [
        {
            'role': 'system',
            'content': SYSTEM_PROMPT
        },
        {
            'role': 'user',
            'content': USER_PROMPT.format(data=data)
        }
    ]
    response = llm.get_llm_response(messages)
    response = response.strip().strip('```json').strip()
    print(response)
    return json.loads(response)
