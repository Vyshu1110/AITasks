import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file (create this file and add your API key there)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize conversation history
conversation_history = []

def chat_with_openai(user_input):
    # Add user input to conversation history
    conversation_history.append({"role": "user", "content": user_input})
    
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=conversation_history,
        temperature=0.7,
        max_tokens=150,
        top_p=1.0
    )
    
    # Get the assistant's response and add it to the conversation history
    assistant_message = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": assistant_message})
    
    return assistant_message

def main():
    print("Chatbot is running. Type 'exit' to end the conversation.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        response = chat_with_openai(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()
