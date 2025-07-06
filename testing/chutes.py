# import os
# from dotenv import load_dotenv
# import aiohttp
# import asyncio
# import json

# load_dotenv()

# async def invoke_chute(messages):
#  api_token = os.getenv('CHUTES_AI_API_KEY')  # Replace with your actual API token

#  headers = {
#   "Authorization": "Bearer " + api_token,
#   "Content-Type": "application/json"
#  }
 
#  body =     {
#       "model": "deepseek-ai/DeepSeek-R1",
#       "messages": messages,
#       "stream": True,
#       "max_tokens": 1024,
#       "temperature": 0.7
#     }

#  async with aiohttp.ClientSession() as session:
#     async with session.post(
#         "https://llm.chutes.ai/v1/chat/completions", 
#         headers=headers,
#         json=body
#     ) as response:
#         async for line in response.content:
#             line = line.decode("utf-8").strip()
#             if line.startswith("data: "):
#                 data = line[6:]
#                 if data == "[DONE]":
#                     break
#                 try:
#                     chunk = data.strip()
#                     if chunk:
#                         print(chunk)
#                 except Exception as e:
#                     print(f"Error parsing chunk: {e}")

# asyncio.run(invoke_chute([
#     {
#         "role": "user",
#         "content": "Tell me a 250 word story."
#     }
# ]))

import httpx
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

CHUTES_API_KEY = os.getenv("CHUTES_AI_API_KEY")  # or paste directly (not recommended)
CHUTES_BASE_URL = "https://llm.chutes.ai/v1/chat/completions"  # Confirm actual endpoint

headers = {
    "Authorization": f"Bearer {CHUTES_API_KEY}",
    "Content-Type": "application/json"
}

async def call_chutes_llm(prompt):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                CHUTES_BASE_URL,
                headers=headers,
                json={
                    "model": "chutes-llm",  # Use correct model ID, like "gpt-4", "mistral", etc.
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7
                }
            )

            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]

        except Exception as e:
            print(f"[!] Error calling Chutes LLM: {e}")
            return None

# Example usage
async def main():
    print('[+] Calling Chutes LLM')
    reply = await call_chutes_llm("Explain quantum computing in simple terms.")
    print("🔮 LLM Response:", reply)

asyncio.run(main())
