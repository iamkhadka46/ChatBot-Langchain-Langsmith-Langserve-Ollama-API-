from fastapi import FastAPI
#from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os 
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="LangChain Server",
    description="LangChain Serve using FastAPI",
    version="0.1.0",
)
'''
add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
model=ChatOpenAI()
'''
##ollama llama2
llm=Ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("Write me an summary about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(
    app,
    prompt1|llm,
    path = "/summary"
)

add_routes(
    app,
    prompt2|llm,
    path = "/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)