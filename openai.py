import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class OpenAIWrapper:
    def __init__(self):
        # Access the OpenAI API key from environment variables
        self.api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = self.api_key

    def create_chat_completion(self, model, messages, temperature=0.8, max_tokens=50):
        # Define the chat completion request
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response

# Usage of the wrapper class
openai_wrapper = OpenAIWrapper()

# Define the chat completion request using the wrapper class
response = openai_wrapper.create_chat_completion(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Translate the following English text to French: 'Hello, how are you?'"},
    ],
    temperature=0.8,
    max_tokens=50
)

# Print the response and the tokens used
print(f"Response: {response.choices[0].message.content}")
print(f"total_tokens: {response.usage.total_tokens}")
