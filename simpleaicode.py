simple code--
# Simple AI Chatbot
print("AI Chatbot: Hello! I'm your AI assistant. Type 'exit' to end the chat.")

while True:
    # Get user input
    user_input = input("You: ").strip().lower()

    # Check for exit condition
    if user_input == "exit":
        print("AI Chatbot: Goodbye! Have a great day!")
        break

    # Respond to greetings
    elif user_input in ["hello", "hi", "hey"]:
        print("AI Chatbot: Hi there! How can I help you today?")
    
    # Respond to "how are you?"
    elif user_input in ["how are you?", "how are you"]:
        print("AI Chatbot: I'm just a bunch of code, but I'm doing great! How about you?")
    
    # Respond to "what is your name?"
    elif user_input in ["what is your name?", "who are you?"]:
        print("AI Chatbot: I'm a simple AI chatbot created to chat with you!")
    
    # Fallback response
    else:
        print("AI Chatbot: I'm not sure how to respond to that. Could you rephrase?")
