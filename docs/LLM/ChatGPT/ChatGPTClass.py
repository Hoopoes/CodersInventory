from enum import Enum
from openai import OpenAI
from openai.types import Completion
from pydantic import BaseModel


class ResponseType(str, Enum):
    message = 'message'
    completion_obj = 'completion_obj'
    message_list = 'message_list'

class Role(str, Enum):
    system = "system"
    user = "user"
    assistant = "assistant"

class MessageSchema(BaseModel):
    role: Role
    content: str

class GPTTokenLimit(Exception):
    """Exception raised when GPT API response message exceeds token limit."""
    finish_reason = 'length'
    def __init__(self, message="GPT API response message exceeds token limit"):
        self.message = message
        super().__init__(self.message)

class ChatGPT:
    
    def __init__(self, 
                 api_key: str, 
                 model: str = "gpt-3.5-turbo",
                 system_prompt: str = '',
                 max_tokens: int | None = None,
                 temperature: float | None = None
            ) -> None:
        
        self.client: OpenAI = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.token_usage: int = 0
        self.message_list: list[MessageSchema] = [MessageSchema(role=Role.system, content=system_prompt)]


    def _chat(self, message_list: list[MessageSchema]) -> Completion:
        return self.client.chat.completions.create(
            model=self.model, 
            messages=message_list,
            temperature=self.temperature,
            max_tokens=self.max_tokens
            )

    def chat(self,
             message: str | list[MessageSchema] | list[dict],
             response_type: ResponseType = ResponseType.message,
             history: bool = False,
             system_prompt: str | None = None
        ) -> MessageSchema | list[MessageSchema]:

        if response_type not in ResponseType.__members__:
            raise ValueError("Invalid response type provided. Must be one of: message, completion_obj, message_list")

        message_list: list[MessageSchema] 

        if isinstance(message, str):
            send: MessageSchema = MessageSchema(role=Role.user, content=message)
            message_list = self.message_list.copy()
            message_list.append(send)
        elif isinstance(message, list):
            try:
                message_list = [MessageSchema(role=item.role, content=item.content) for item in message]
            except AttributeError:
                message_list = [MessageSchema.model_validate(item) for item in message]

               

        if system_prompt is not None:
            if message_list[0].role == Role.system:
                message_list[0].content = system_prompt

        response: Completion = self._chat(message_list=message_list)
        
        reply: MessageSchema = MessageSchema(role=Role.assistant, content=response.choices[0].message.content)
        self.token_usage += response.usage.total_tokens

        if ((self.max_tokens is not None) and (self.token_usage >= self.max_tokens)):
            raise GPTTokenLimit()

        if response.choices[0].finish_reason == GPTTokenLimit.finish_reason:
            raise GPTTokenLimit()

        message_list.append(reply)

        if history:
            self.message_list = message_list.copy()
            self.message_list.append(reply)

        if response_type == ResponseType.message:
            return reply
        elif response_type == ResponseType.message_list:
            return message_list
        elif response_type == ResponseType.completion_obj:
            return response