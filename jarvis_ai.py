# Phase 2a: Enhanced Conversational AI with basic NLP-like features
# This will be a simple command-line interface AI

import re
import datetime
import random

def get_response(user_input):
    """
    Generates a response based on user input using more flexible matching.
    """
    user_input_lower = user_input.lower()

    # Greeting
    if re.search(r"\b(hello|hi|hey|greetings)\b", user_input_lower):
        return "Hello there! How can I help you today?"

    # Name inquiry
    elif re.search(r"\b(what is|what's|tell me)\s+(your name)\b", user_input_lower) or \
         re.search(r"\b(who are you)\b", user_input_lower):
        return "I am a prototype AI, inspired by Jarvis. You can call me Jules."

    # Capability inquiry
    elif re.search(r"\b(what can you do|what are your capabilities|help|tell me what you can do)\b", user_input_lower): # Added "tell me what you can do"
        return "I can currently understand some basic questions and commands. For example, you can ask my name, how I am, the time, or tell me a joke. We are working on expanding my capabilities!"

    # Well-being inquiry
    elif re.search(r"\b(how are you|how's it going|how do you feel)\b", user_input_lower):
        return "I am functioning optimally, thank you for asking."

    # Time inquiry
    elif re.search(r"\b(what time is it|tell me the time|current time)\b", user_input_lower):
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."

    # Joke request
    elif re.search(r"\b(tell me\s+(a\s+)?joke|say something funny|joke|tell me something funny)\b", user_input_lower): # Made "a" optional and added "tell me something funny"
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call fake spaghetti? An impasta!",
            "Why did the bicycle fall over? Because it was two tired!"
        ]
        return random.choice(jokes)

    # Farewell
    elif re.search(r"\b(bye|exit|quit|goodbye|see you)\b", user_input_lower):
        return "Goodbye! It was nice talking to you."

    # Default
    else:
        return "I'm sorry, I don't quite understand that yet. I am still learning."

def main():
    """
    Main function to run the AI's conversational loop.
    """
    print("AI: Hello! I'm your AI assistant. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print(f"AI: {get_response(user_input)}")
            break

        ai_response = get_response(user_input)
        print(f"AI: {ai_response}")

if __name__ == "__main__":
    main()
