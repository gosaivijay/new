# Phase 1: Basic Conversational AI
# This will be a simple command-line interface AI

def get_response(user_input):
    """
    Generates a response based on user input.
    """
    user_input = user_input.lower() # Convert to lowercase for easier matching

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! How can I help you today?"
    elif "what is your name" in user_input:
        return "I am a prototype AI, inspired by Jarvis."
    elif "what can you do" in user_input:
        return "Currently, I can understand a few basic commands. We are working on expanding my capabilities!"
    elif "how are you" in user_input:
        return "I am functioning optimally, thank you for asking."
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! It was nice talking to you."
    else:
        return "I'm sorry, I don't understand that yet. I am still learning."

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
