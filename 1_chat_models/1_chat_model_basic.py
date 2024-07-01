# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

#Load environment variables from .env
load_dotenv()

#create a chatopenAI model

model = ChatOpenAI(model = "gpt-3.5-turbo")
model_1 = ChatGoogleGenerativeAI(model = "gemini-pro")

#Invoke the model with message

response = model.invoke("Write a ballad about LangChain")
print("Full response: ", response)
print("Content only: ", response.content)