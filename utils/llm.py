import os
import json
from groq import Groq
from dotenv import load_dotenv

from utils.chutes_llm import ChutesLLM, ChutesLLMError

load_dotenv()

class GroqLLM:
    # model = "llama-3.3-70b-versatile"
    model = "gemma2-9b-it"

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def get_llm_response(self, messages):
        # print('[groq] Groq LLM responding')
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        output = response.choices[0].message.content.strip()

        if output and (output[0] == output[-1]) and output.startswith(("'", '"')):
            output = output[1:-1]

        return output


class ChutesAI:
    # model = "chutesai/Mistral-Small-3.1-24B-Instruct-2503"
    # model = "chutesai/Llama-4-Maverick-17B-128E-Instruct-FP8"
    # model = "chutesai/Llama-3.1-405B-FP8"
    model = "deepseek-ai/DeepSeek-V3-0324"

    def __init__(self):
        self.client = ChutesLLM(api_key=os.getenv("CHUTES_AI_API_KEY"))

    def get_llm_response(self, messages):
        response = self.client.chat.completions.create(
            messages = messages,
            model = self.model,
            temperature = 0.7,
            # max_tokens = 1500,
            # json_mode = True
        )

        try:
            output = response['choices'][0]['message']['content'].strip()
            # cprint(json.dumps(json.loads(output), indent=4), color=CYAN)

        except ChutesLLMError as e:
            print(f"=== ChutesLLMError in chat completion ===")            
            print(f"error: {e}")
            print(f"response: {response}")

            # NOTE: send logs to telegram (admins)
            data = IssueReportRequest(response)
            cprint(f"\n{data.issue_report}\n", color=RED)
            send_message(data.issue_report)

            print("==========================================")
            output = ""

        except Exception as e:
            print(f"=== Exception in chat completion error ===")
            print(f"error: {e}")
            print(f"response: {response}")

            # NOTE: send logs to telegram (admins)
            data = IssueReportRequest(response)
            cprint(f"\n{data.issue_report}\n", color=RED)
            send_message(data.issue_report)

            print("===========================================")

            output = ""

        return output


# llm
# llm = ChutesAI()
llm = GroqLLM()

def get_llm_response(messages):
    try:
        return llm.get_llm_response(messages)
    except Exception as e:
        cprint(f"[ERROR in get_llm_response]: {e}", color=RED)
        return ""




