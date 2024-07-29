""" import anthropic
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the Anthropic API key from environment variables
client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

# Define the chat completion request
try:
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=50,
        temperature=0.8,
        messages=[
            {"role": "user", "content": "Translate the following English text to French: 'Hello, how are you?'"}
        ]
    )

    # Print the response
    print(f"Response: {response.content[0].text}")

except anthropic.APIError as e:
    print(f"An error occurred: {e}") """





""" import gemini
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the Gemini API key from environment variables
client = gemini.Gemini(api_key=os.getenv('GEMINI_API_KEY'))

# Define the chat completion request
try:
    response = client.create(
        model="gemini-model-name",  # Replace with the actual Gemini model name
        max_tokens=50,
        temperature=0.8,
        prompt="Translate the following English text to French: 'Hello, how are you?'"
    )

    # Print the response
    print(f"Response: {response.text}")

except gemini.APIError as e:
    print(f"An error occurred: {e}")
 """


"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""


import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Access the Gemini API key from environment variables
api_key = os.getenv('GEMINI_API_KEY')

# Ensure the API key is available
if not api_key:
    raise ValueError("No GEMINI_API_KEY found in environment variables.")

genai.configure(api_key=api_key)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "what is ai\n",
            ],
        },
        {
            "role": "model",
            "parts": [
                "##  AI: A Simplified Explanation\n\n**AI stands for Artificial Intelligence.**  It's essentially the ability of a computer or machine to perform tasks that typically require human intelligence. Think of it like a robot brain that can learn, adapt, and solve problems just like we do.\n\n**Here's a breakdown of what AI is, in simpler terms:**\n\n* **Learning:**  AI systems can learn from data, just like we learn from experience. They analyze massive amounts of information to identify patterns and make predictions. \n* **Problem-solving:**  AI can solve complex problems by using logic, reasoning, and knowledge. \n* **Adaptation:**  AI systems can adjust and improve their performance over time, becoming more efficient and accurate.\n\n**Examples of AI in action:**\n\n* **Self-driving cars:**  AI powers the navigation, obstacle detection, and driving decisions of autonomous vehicles.\n* **Virtual assistants:**  AI allows devices like Siri, Alexa, and Google Assistant to understand your voice commands and respond intelligently.\n* **Personalized recommendations:**  AI helps platforms like Netflix, Amazon, and Spotify predict what you might enjoy watching, buying, or listening to.\n* **Medical diagnosis:**  AI can analyze medical images and data to help doctors make more accurate diagnoses.\n\n**Important things to remember:**\n\n* **AI is still evolving:**  It's a relatively new field with immense potential, but it's still developing.\n* **AI has its limitations:**  While powerful, AI systems are not perfect. They can make mistakes and sometimes require human intervention.\n\n**In a nutshell, AI is a fascinating and rapidly growing field that is changing the world as we know it.**  It's everywhere, from our smartphones to our cars, and its impact will continue to grow in the future. \n",
            ],
        },
    ]
)

def get_user_input():
    return input("Please enter your input: ")

def generate_response(user_input):
    response = chat_session.send_message(user_input)
    return response.text

def main():
    user_input = get_user_input()
    response_text = generate_response(user_input)
    print(response_text)

if __name__ == "__main__":
    main()

