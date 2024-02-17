import sys
from os.path import abspath, dirname
current_dir = dirname(abspath(__file__))
parent_dir = dirname(current_dir)
sys.path.append(parent_dir)
from config import Config



import os
from enum import Enum
from openai import OpenAI
from pydantic import BaseModel

class RoleEnum(str, Enum):
    system: str = 'system'
    user: str = 'user'
    assistant: str = 'assistant'

class MessageSchema(BaseModel):
    role: RoleEnum
    content: str

class ChatGPT:
    
    def __init__(self, 
                 api_key: str, 
                 model: str = "gpt-3.5-turbo",
                 system_prompt: str = ''
            ) -> None:
        os.environ['OPENAI_API_KEY'] = api_key
        self.client: OpenAI = OpenAI(api_key=api_key)
        self.model = model
        self.messages: list[MessageSchema] = [MessageSchema(role=RoleEnum.system.value, content=system_prompt)]

    def chat(self,
             message: str, 
             only_message:bool = True, 
             history: bool = False
        ) -> str | dict:

        messages: list[MessageSchema] | MessageSchema = []

        send: MessageSchema = MessageSchema(role=RoleEnum.user.value, content=message)
        messages = self.messages.copy()
        messages.append(send)

        # response = self.client.chat.completions.create(model=self.model, messages=messages)
        # reply: MessageSchema = MessageSchema(role=RoleEnum.assistant.value, content=response.choices[0].message.content)
        
        response = None
        reply: MessageSchema = MessageSchema(role=RoleEnum.assistant.value, content=message+message)

        if history:
            self.messages.append(send)
            self.messages.append(reply)
        

        print(reply)
        return reply if only_message else response


def main():
    bot = ChatGPT(api_key=Config.openai_api_key)
    bot.chat('HI', history=True)
    # bot.chat('b', history=True)
    # bot.chat('c', history=False)
    # bot.chat('d', history=True)
    # bot.chat('e', history=True)



if __name__ == '__main__':
    main()