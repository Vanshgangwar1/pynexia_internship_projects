import re
import string
import random

def preprocess_input(text: str) -> str:
    """
    Cleans raw user input by converting to lowercase, 
    stripping leading/trailing spaces, and removing punctuation.
    """
    text = text.lower().strip()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Define Intent Rules using Regular Expressions and associated responses
INTENT_RULES = {
    "greeting": {
        "patterns": [r"\b(hello|hi|hey|greetings|good morning|good evening)\b"],
        "responses": [
            "Hello! How can I assist you today?",
            "Hi there! What's on your mind?",
            "Hey! How can I help you?"
        ]
    },
    "identity": {
        "patterns": [r"\b(who are you|what is your name|your name)\b"],
        "responses": [
            "I am PyBot, a simple rule-based chatbot designed to assist you.",
            "You can call me PyBot! I'm a rule-based AI assistant."
        ]
    },
    "status": {
        "patterns": [r"\b(how are you|how is it going|how do you do)\b"],
        "responses": [
            "I'm functioning perfectly! How about you?",
            "Doing great! Ready to help you with your queries."
        ]
    },
    "help": {
        "patterns": [r"\b(help|support|assist|what can you do)\b"],
        "responses": [
            "I can answer basic questions, talk about my capabilities, or chat! Try asking me who I am or how I work.",
            "I am a rule-based bot. Ask me greetings, my name, or say goodbye!"
        ]
    },
    "creator": {
        "patterns": [r"\b(who created you|who made you|who built you)\b"],
        "responses": [
            "I was created using Python and basic regular expression pattern matching!"
        ]
    },
    "farewell": {
        "patterns": [r"\b(bye|goodbye|exit|quit|see you)\b"],
        "responses": [
            "Goodbye! Have a great day ahead.",
            "Farewell! Feel free to reach out anytime.",
            "Bye! Happy coding!"
        ]
    }
}

# Default response when no rules match
FALLBACK_RESPONSES = [
    "I'm sorry, I didn't quite understand that. Could you rephrase?",
    "I'm not trained for that specific query yet. Try asking for 'help'!",
    "Can you clarify your question? I'm still learning new pattern rules."
]

def get_response(user_input: str) -> tuple[str, bool]:
    """
    Evaluates input against rules and returns a tuple (response_text, should_exit).
    """
    cleaned_input = preprocess_input(user_input)

    # Empty input check
    if not cleaned_input:
        return "It looks like you didn't say anything!", False

    # Check input against intent patterns
    for intent, data in INTENT_RULES.items():
        for pattern in data["patterns"]:
            if re.search(pattern, cleaned_input):
                response = random.choice(data["responses"])
                is_exit = intent == "farewell"
                return response, is_exit

    # Return random fallback if no pattern matched
    return random.choice(FALLBACK_RESPONSES), False

def start_chat():
    """Runs the continuous terminal chatbot session."""
    print("=" * 60)
    print("🤖 Welcome to PyBot - Rule-Based Chatbot")
    print("Type 'exit' or 'bye' at any time to end the conversation.")
    print("=" * 60)

    while True:
        try:
            user_input = input("\nYou: ")
            response, is_exit = get_response(user_input)
            print(f"PyBot: {response}")

            if is_exit:
                break
        except (KeyboardInterrupt, EOFError):
            print("\nPyBot: Session terminated. Goodbye!")
            break

if __name__ == "__main__":
    start_chat()