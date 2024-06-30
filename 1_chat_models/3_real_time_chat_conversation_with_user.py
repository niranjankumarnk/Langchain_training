from dotenv import load_dotenv
from langchain_core.messages import AIMessage,HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

#Load environment variables from .env
load_dotenv()

#create a model 
model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

# create a list to store messages

chat_history = []

#set an iitial system message (optional)
system_message = SystemMessage(content = "Welcome to the chat. How can I help you today?")
chat_history.append(system_message)

#chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content = query))
    
    #Get AI response using history
    result =model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content = response))
    
    print(f"AI: {response}")
    
print("----Message History ----")
print(chat_history)
    