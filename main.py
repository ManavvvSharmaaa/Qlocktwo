def get_response(user_input):
    # Define a dictionary of responses
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm just a computer program, but I'm doing well. How about you?",
        "what is your name": "I'm a simple chatbot created to help you.",
        "bye": "Goodbye! Have a great day!",
    }

    # Convert user input to lowercase
    user_input = user_input.lower()

    # Check if the user input matches any of the predefined responses
    response = responses.get(user_input, "Sorry, I don't understand that.")

    return response


def chatbot():
    print("Hello! I'm your chatbot. Type 'bye' to end the conversation.")

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit the chat if the user types 'bye'
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Get response from the chatbot
        response = get_response(user_input)

        # Print the chatbot's response
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chatbot()
