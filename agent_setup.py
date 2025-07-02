import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from tools import format_tool

# Load environment
load_dotenv()
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=4096,
    api_key=os.getenv("GROQ_API_KEY")
)

agent = initialize_agent(
    tools=[format_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
