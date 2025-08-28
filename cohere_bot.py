

import cohere

# Initialize Cohere client (store API key in environment variable instead of hardcoding)
co = cohere.Client("
# YOUR COHERE GENERATED API KEY
                   "
)

def chat_with_cohere(prompt):
    response = co.chat(
        model="command-r-plus",  # Cohere's conversational model
        message=prompt
    )
    return response.text.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_cohere(user_input)
        print("Chatbot:", response)

