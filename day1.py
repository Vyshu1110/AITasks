import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define the chat completion request
response = openai.chat.completions.create(
    model="gpt-4",
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
