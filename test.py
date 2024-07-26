import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# Example of making a request to the OpenAI API
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Describe the impact of artificial intelligence on healthcare."}
    ],
    max_tokens=150
)
print(response)

# Example of a potential response structure (the actual response will come from the API)
response_dict = {
    "id": "cmpl-5uIvfBq6I47zr1nTQjVZ9g5F",
    "object": "chat.completion",
    "created": 1623312226,
    "model": "gpt-3.5-turbo",
    "choices": [
        {
            "message": {"role": "assistant", "content": "Artificial intelligence (AI) has a profound impact on healthcare, enhancing diagnostic accuracy, personalizing treatment plans, and improving patient outcomes. AI-powered tools can analyze vast amounts of medical data quickly, aiding in early disease detection and management. Additionally, AI algorithms assist in drug discovery, optimizing clinical workflows, and providing virtual health assistants to support patient care."},
            "index": 0,
            "finish_reason": "length"
        }
    ],
    "usage": {
        "prompt_tokens": 24,  # This count should be accurate based on the actual tokens used in the prompt
        "completion_tokens": 60,  # This count should be accurate based on the actual tokens generated in the completion
        "total_tokens": 84  # Sum of prompt_tokens and completion_tokens
    }
}

# Extract and print total_tokens
total_tokens = response_dict['usage']['total_tokens']
print(total_tokens)
