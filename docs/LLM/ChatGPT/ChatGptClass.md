### Simplified Version

```python
import openai
import os

# Global variables to simulate enums
ROLE_USER = "user"
ROLE_ASSISTANT = "assistant"
ROLE_SYSTEM = "system"

class ChatGPT:
    
    def __init__(self, api_key=None, model="gpt-3.5-turbo", system_prompt='', max_tokens=None, temperature=None):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.token_usage = 0
        self.message_list = [{"role": ROLE_SYSTEM, "content": system_prompt}]
        openai.api_key = self.api_key
    
    @staticmethod
    def mapper(message):
        message_list = []
        if isinstance(message, str):
            message_list.append({"role": ROLE_USER, "content": message})
        elif isinstance(message, list):
            for item in message:
                message_list.append(item)
        return message_list

    def _chat(self, message_list, temperature=None, model=None):
        response = openai.ChatCompletion.create(
            model=self.model if model is None else model,
            messages=message_list,
            temperature=self.temperature if temperature is None else temperature,
            max_tokens=self.max_tokens
        )
        return response

    def chat(self, message=None, response_type="message", system_prompt=None, temperature=None, model=None):
        if message is not None:
            message_list = ChatGPT.mapper(message)
        else:
            message_list = [{"role": ROLE_SYSTEM, "content": ""}]
        
        if system_prompt is not None:
            if message_list[0]["role"] == ROLE_SYSTEM:
                message_list[0]["content"] = system_prompt
            else:
                message_list.insert(0, {"role": ROLE_SYSTEM, "content": system_prompt})

        response = self._chat(message_list=message_list, temperature=temperature, model=model)
        
        reply = {"role": ROLE_ASSISTANT, "content": response.choices[0].message["content"]}
        self.token_usage += response.usage["total_tokens"]

        if self.max_tokens is not None and self.token_usage >= self.max_tokens:
            raise Exception("GPT API response message exceeds token limit")

        if response.choices[0]["finish_reason"] == "length":
            raise Exception("GPT API response message exceeds token limit")

        message_list.append(reply)

        if response_type == "message":
            return reply
        elif response_type == "message_list":
            return message_list
        elif response_type == "completion_obj":
            return response
        elif response_type == "json":
            return [{"role": item["role"], "content": item["content"]} for item in message_list]

    def message_to_str(self, message, role=None):
        result = ""
        roles = [ROLE_USER, ROLE_ASSISTANT]
        for i, item in enumerate(message):
            if role is None:
                result += f"{roles[i % 2]}: {item['content']}\n"
            elif item["role"] == role:
                result += f"{role}: {item['content']}\n"
        return result
    
    def observer(self, message, observer_prompt, role=None, from_last=True):
        if role == ROLE_SYSTEM:
            raise ValueError("Role cannot be 'system' for observer method")
        
        message_list = ChatGPT.mapper(message)
    
        if from_last:
            for item in message_list[::-1]:
                if role is None or item["role"] == role:
                    required_message = item["content"]
                    break
        else:
            required_message = self.message_to_str(message_list, role)

        return self.chat(message=required_message, response_type="message", system_prompt=observer_prompt, temperature=0.0, model="gpt-3.5-turbo")
```

### Middle Version

Now, let's add a bit more structure by introducing type annotations and simplifying some of the complex structures, but we'll avoid using enums and Pydantic.

```python
import openai
from typing import List, Dict, Optional, Union

# Simple role constants
ROLE_USER = "user"
ROLE_ASSISTANT = "assistant"
ROLE_SYSTEM = "system"

class ChatGPT:
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo", system_prompt: str = '', max_tokens: Optional[int] = None, temperature: Optional[float] = None) -> None:
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.token_usage = 0
        self.message_list = [{"role": ROLE_SYSTEM, "content": system_prompt}]
        openai.api_key = self.api_key
    
    @staticmethod
    def mapper(message: Union[str, List[Dict[str, str]]]) -> List[Dict[str, str]]:
        message_list = []
        if isinstance(message, str):
            message_list.append({"role": ROLE_USER, "content": message})
        elif isinstance(message, list):
            for item in message:
                message_list.append(item)
        return message_list

    def _chat(self, message_list: List[Dict[str, str]], temperature: Optional[float] = None, model: Optional[str] = None):
        response = openai.ChatCompletion.create(
            model=self.model if model is None else model,
            messages=message_list,
            temperature=self.temperature if temperature is None else temperature,
            max_tokens=self.max_tokens
        )
        return response

    def chat(self, message: Optional[Union[str, List[Dict[str, str]]]] = None, response_type: str = "message", system_prompt: Optional[str] = None, temperature: Optional[float] = None, model: Optional[str] = None):
        if message is not None:
            message_list = ChatGPT.mapper(message)
        else:
            message_list = [{"role": ROLE_SYSTEM, "content": ""}]
        
        if system_prompt is not None:
            if message_list[0]["role"] == ROLE_SYSTEM:
                message_list[0]["content"] = system_prompt
            else:
                message_list.insert(0, {"role": ROLE_SYSTEM, "content": system_prompt})

        response = self._chat(message_list=message_list, temperature=temperature, model=model)
        
        reply = {"role": ROLE_ASSISTANT, "content": response.choices[0].message["content"]}
        self.token_usage += response.usage["total_tokens"]

        if self.max_tokens is not None and self.token_usage >= self.max_tokens:
            raise Exception("GPT API response message exceeds token limit")

        if response.choices[0]["finish_reason"] == "length":
            raise Exception("GPT API response message exceeds token limit")

        message_list.append(reply)

        if response_type == "message":
            return reply
        elif response_type == "message_list":
            return message_list
        elif response_type == "completion_obj":
            return response
        elif response_type == "json":
            return [{"role": item["role"], "content": item["content"]} for item in message_list]

    def message_to_str(self, message: List[Dict[str, str]], role: Optional[str] = None) -> str:
        result = ""
        roles = [ROLE_USER, ROLE_ASSISTANT]
        for i, item in enumerate(message):
            if role is None:
                result += f"{roles[i % 2]}: {item['content']}\n"
            elif item["role"] == role:
                result += f"{role}: {item['content']}\n"
        return result
    
    def observer(self, message: Union[str, List[Dict[str, str]]], observer_prompt: str, role: Optional[str] = None, from_last: bool = True) -> Dict[str, str]:
        if role == ROLE_SYSTEM:
            raise ValueError("Role cannot be 'system' for observer method")
        
        message_list = ChatGPT.mapper(message)
    
        if from_last:
            for item in message_list[::-1]:
                if role is None or item["role"] == role:
                    required_message = item["content"]
                    break
        else:
            required_message = self.message_to_str(message_list, role)

        return self.chat(message=required_message, response_type="message", system_prompt=observer_prompt, temperature=0.0, model="gpt-3.5-turbo")
```

### Detailed Version 

```python
from enum import Enum
from typing import Literal, Optional
from openai import AsyncOpenAI
from openai.types import Completion
from pydantic import BaseModel

class ResponseType(str, Enum):
    """Enum representing the type of response from the GPT model."""
    message = 'message'
    completion_obj = 'completion_obj'
    message_list = 'message_list'
    json = 'json'

class Role(str, Enum):
    """Enum representing the role of the message sender."""
    system = "system"
    user = "user"
    assistant = "assistant"

class MessageSchema(BaseModel):
    """Schema for a message exchanged with the GPT model."""
    role: Role
    content: str

class GPTTokenLimit(Exception):
    """Exception raised when GPT API response message exceeds

 token limit."""
    finish_reason = 'length'
    def __init__(self, message="GPT API response message exceeds token limit"):
        self.message = message
        super().__init__(self.message)

class ChatGPT:
    """Class for interacting with the OpenAI GPT API."""
    
    def __init__(self, 
                 api_key: str | None = None, 
                 model: str = "gpt-3.5-turbo",
                 system_prompt: str = '',
                 max_tokens: int | None = None,
                 temperature: float | None = None
            ) -> None:
        """Initialize the ChatGPT instance with the specified parameters."""
        self.client: AsyncOpenAI = AsyncOpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.token_usage: int = 0
        self.message_list: list[MessageSchema] = [MessageSchema(role=Role.system, content=system_prompt)]
    
    @staticmethod
    def mapper(message: str | list[MessageSchema] | list[dict]) -> list[MessageSchema]:
        """Map input messages to a list of MessageSchema."""
        message_list: list[MessageSchema] = []
        if isinstance(message, str):
            send: MessageSchema = MessageSchema(role=Role.user, content=message)
            message_list.append(send)
        elif isinstance(message, list):
            for item in message:
                if isinstance(item, MessageSchema):
                    message_list.append(item)
                elif isinstance(item, dict):
                    message_list.append(MessageSchema(role=item.get('role'), content=item.get('content')))
                else:
                    message_list.append(MessageSchema(role=item.role, content=item.content))
        return message_list

    async def _chat(self, 
              message_list: list[MessageSchema], 
              temperature: float | None = None, 
              response_format: dict[str,str] | None = None,
              model: str | None = None) -> Completion:
        """Send a chat request to the OpenAI API."""
        return await self.client.chat.completions.create(
            model=self.model if model is None else model,
            messages=message_list,
            temperature=self.temperature if temperature is None else temperature,
            max_tokens=self.max_tokens,
            response_format=response_format
        )

    async def chat(self,
             message: Optional[str | list[MessageSchema] | list[dict]] = None,
             response_type: ResponseType = ResponseType.message,
             response_format: Optional[dict[Literal["type"], Literal["json_object", "text"]]]= None,
             system_prompt: Optional[str] = None,
             temperature: Optional[float] = None,
             model: Optional[str] = None) -> MessageSchema | list[MessageSchema]:
        """
        Send a chat message and get a response from the GPT model.
        
        Parameters:
            message: The message or list of messages to send.
            response_type: The type of response to return.
            response_format: The format of the response.
            system_prompt: The system prompt to use.
            temperature: The temperature for the model.
            model: The model to use.
        
        Returns:
            The response from the GPT model in the specified format.
        """
        if response_type not in ResponseType.__members__:
            raise ValueError("Invalid response type provided. Must be one of: message, completion_obj, message_list")

        if message is not None:
            message_list: list[MessageSchema] = ChatGPT.mapper(message)
        else:
            message_list: list[MessageSchema] = [MessageSchema(role=Role.system, content="")]  

        if system_prompt is not None:
            if message_list[0].role == Role.system:
                message_list[0].content = system_prompt
            else:
                message_list.insert(0, MessageSchema(role=Role.system, content=system_prompt))

        response: Completion = await self._chat(message_list=message_list, temperature=temperature, response_format=response_format, model=model)
        
        reply: MessageSchema = MessageSchema(role=Role.assistant, content=response.choices[0].message.content)
        self.token_usage += response.usage.total_tokens

        if ((self.max_tokens is not None) and (self.token_usage >= self.max_tokens)):
            raise GPTTokenLimit()

        if response.choices[0].finish_reason == GPTTokenLimit.finish_reason:
            raise GPTTokenLimit()

        message_list.append(reply)

        if response_type == ResponseType.message:
            return reply
        elif response_type == ResponseType.message_list:
            return message_list
        elif response_type == ResponseType.completion_obj:
            return response
        elif response_type == ResponseType.json:
            json_list: list[dict] = [message.model_dump() for message in message_list]
            i: int
            for i, item in enumerate(json_list):
                item['role'] = item['role'].value
                json_list[i] = item 
            return json_list

    @staticmethod    
    def message_to_str(message: list[MessageSchema], 
                    role: Role | None = None) -> str:
        """
        Convert a list of messages to a string format.
        
        Parameters:
            message: The list of messages to convert.
            role: The role to filter by.
        
        Returns:
            A string representation of the messages.
        """
        result: str = ""
        roles: list[Role] = [Role.user, Role.assistant]
        i: int
        item: MessageSchema
        for i, item in enumerate(message):
            if role is None:
                result += f"{roles[i%2].value}: {item.content}\n"
            elif item.role == role:
                result += f"{role}: {item.content}\n"
        return result
    
    async def observer(self,
                 message: str | list[MessageSchema] | list[dict],
                 observer_prompt: str,
                 role: Role | str | None = None,
                 from_last: bool = True,
                ) -> MessageSchema:
        """
        Use an observer to generate a response based on a message and an observer prompt.
        
        Parameters:
            message: The message or list of messages to observe.
            observer_prompt: The prompt to use for the observer.
            role: The role to filter by.
            from_last: Whether to start from the last message.
        
        Returns:
            The observer's response message.
        """
        if role == Role.system or role == Role.system.value:
            raise ValueError("Role cannot be 'system' for observer method")
        
        message_list: list[MessageSchema] = ChatGPT.mapper(message)
    
        required_message: str | list[MessageSchema] 
        if from_last:
            for item in message_list[::-1]:  
                if role is None or item.role == role:
                    required_message = item.content
                    break
        else:
            required_message = ChatGPT.message_to_str(message_list, role)

        return  await self.chat(message=required_message,
                          response_type=ResponseType.message,
                          system_prompt=observer_prompt,
                          temperature=0.0,
                          model="gpt-3.5-turbo")
```