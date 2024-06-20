from nltk.chat.util import Chat, reflections
import time

Data = [
    [r"how are you?", ["I'm doing well, thank you!"]],
    [r"can I ask you any question?", ["Feel free to ask me anything."]],
    [r"what is your name?", ["My name is Chatbot."]],
    [r"what is your function?", ["I'm here to provide any help to you."]],
    [r"who developed you?", ["I was developed by a Python developer known as Ahmed Medhat."]],
    [r"can you be my best friend?", ["Yes, I can be your best friend."]],
    [r"thank you for being my friend", ["Don't mention it, I'm here to help you feel better."]],
    [r"quit", ["Goodbye!"]]
]

def ChatbotRun():
    WelcomeInp = input("Enter your name: ")
    print(f"Hi {WelcomeInp}, How can I help you today?")
    time.sleep(1.5)
    chatbot = Chat(Data, reflections)
    while True:
        request = input("Enter your request: ")
        if request.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(request)
        print("Chatbot:", response)
ChatbotRun()
