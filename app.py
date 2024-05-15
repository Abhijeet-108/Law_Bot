import sys
from configparser import ConfigParser
from namos import ChatBot

def main():
    config = ConfigParser()
    config.read('credentials.ini')
    api_key = config['gemini_ai']['API_KEY']

    chatbot = ChatBot(api_key=api_key)
    chatbot.start_conversation()
    #chatbot.clear_conversation()

    print("Welcome to Legal Assistant => Namos. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            #print("Satak Rahe Shawdhan Rahe.....")
            sys.exit('Satak Rahe Shawdhan Rahe.....')

        try:
            response = chatbot.send_prompt(user_input)
            print(f"{chatbot.CHATBOT_NAME}: {response}")
        except Exception as e:
            print(f"Error: {e}") 

main()