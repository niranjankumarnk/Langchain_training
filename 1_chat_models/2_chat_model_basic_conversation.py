from dotenv import load_dotenv
from langchain_core.messages import AIMessage,HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

#Load environment variables from .env
load_dotenv()

#create a chatopenAI model

model = ChatOpenAI(model = "gpt-3.5-turbo")
model_1 = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

# SystemMessage:
#   Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
# HumanMessagse:
#   Message from a human to the AI model.
# messages = [
#     SystemMessage(content="Solve the following math problems"),
#     HumanMessage(content="What is 81 divided by 9?"),
# ]

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content = "81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?"),
]


#Invoke the model with message
result = model_1.invoke(messages)
print(f"Answer from AI: {result.content}")

