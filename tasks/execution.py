# task execution - use twikit to perform tasks related to twitter

from twikit import Client
# from twikit.errors import TwiException

from utils.llm import llm
from utils.prompts import AVAILABLE_FUNCTIONS, TASK_EXECUTION_SYSTEM_PROMPT, TASK_EXECUTION_USER_PROMPT
from utils.parser import Parser
from twitter.x import Twitter

class TaskExecutionAgent:
    def __init__(self):
        print('[+] Initializing Task Execution Agent...')
        self.system_prompt = TASK_EXECUTION_SYSTEM_PROMPT
        self.user_prompt = TASK_EXECUTION_USER_PROMPT
        self.available_functions = AVAILABLE_FUNCTIONS

        self.client = Client(language='en-US')
        self.parser = Parser()
        self.llm = llm
        self.x = Twitter()

        self.functions = {
            # Utility functions
            'generate_tweet_content': self.x.generate_tweet_content,
            # 'generate_reply': self.x.generate_reply,
            
            # Data retrieval functions
            'get_user_tweets': self.x.get_user_tweets,
            'search_tweets_by_query': self.x.search_tweets_by_query,
            'get_trending_topics': self.x.get_trending_topics,
            'get_user_followers': self.x.get_user_followers,
            
            # Fucntions to interact with multiple tweets
            'like_tweets': self.x.like_tweets,
            'comment_on_tweets': self.x.comment_on_tweets,
            'retweet_tweets': self.x.retweet_tweets,
            'follow_users': self.x.follow_users,
            'unfollow_users': self.x.unfollow_users,
            'generate_replies': self.x.generate_replies,

            # Functions to interact with single tweet
            'create_tweet': self.x.create_tweet
        }
    
    async def x_login(self, USERNAME, EMAIL, PASSWORD):
        print('[twitter_login] LOGGING IN TO TWITTER')
        await self.client.login(
            auth_info_1=USERNAME,
            auth_info_2=EMAIL,
            password=PASSWORD
        )
    
    # MAIN ENTER POINT OF TASK
    # todo: change to async
    def execute_tasks(self, tasks):
        task_results = []
        for task in tasks:
            try:
                self.execution_loop(task)
                task_results.append({
                    "task": task,
                    "result": "Task executed successfully"
                })
            except Exception as e:
                print(f"[!] Error in execution loop: {e}")
                task_results.append({
                    "task": task,
                    "result": f"Field to execute task: {e}"
                })
        return task_results
    
    # todo: change to async
    def execution_loop(self, task):
        try:
            print("\n\n\n")
            print("[ Execution Loop START ]".center(46, "="))
            print(f'[TASK] {task}\n')
            messages = [
                {"role": "system", "content": self.system_prompt.format(available_functions=self.available_functions)},
                {"role": "user", "content": self.user_prompt.format(task=task)}
            ]
            functions_list = self.parser.extract_json_from_text(self.llm.get_llm_response(messages))
            print(f"[agent_response] {functions_list['functions']}")
            new_messages = [
                {"role": "assistant", "content": f"""```json{functions_list}```"""},
                {"role": "user","content": f"""START_EXECUTION"""}
                # first function: {functions_list['functions'][0]}
                # according to the conversation history, give me this complete function with all parameters:
            ]
            print('[user] START_EXECUTION')
            for message in new_messages:
                messages.append(message)

            for i in range(len(functions_list['functions'])):
                print(f'[iteration] [{i}]: {functions_list["functions"][i]}')
                response = self.llm.get_llm_response(messages)
                parsed = self.parser.extract_json_from_text(response)
                print(f'[agent_response] {parsed}')
                if 'error' in parsed:
                    print(f"[error] {parsed['error']}")
                    break
                function_response = self.execute_function(response)
                print(f'[function_response] {function_response}')
                messages.append({"role": "assistant", "content": f"""```json{response}```"""})
                messages.append({"role": "user", "content": f"""
                    function {functions_list['functions'][i]} executed successfully.
                    {functions_list['functions'][i]} response:
                    {function_response}

                    Okay, now let's execute the next function in the provided list.
                    """})

            print("\n")
            print("[ Execution Loop END ]".center(46, "="))
            print("\n\n\n")
        except Exception as e:
            print(f"[!] Error in execution loop: {e}")
            raise

    
    def execute_function(self, function):
        try:
            function = self.parser.extract_json_from_text(function)
            func_name = function.get('function')
            print(f'[---------] calling function: {func_name} [---------]')
            f = self.functions.get(func_name)
            params = function.get('params', {})
            if f is None:
                # return { "error": f"Invalid function '{function}'" }
                raise ValueError(f"Invalid function '{function}'")
            return f(**params)
        except Exception as e:
            # return { "error": f"Execution failed: {str(e)}" }
            raise

