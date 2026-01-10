from Utils.model_loader import ModelLoader
from langchain_tavily import TavilySearch
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import warnings
warnings.filterwarnings("ignore")

load_dotenv()
llm = ModelLoader().llm_loader()


def get_response_from_ai_agents(model_name,model_provider,prompt,query):
        
        if model_provider =="OpenAI":
                llm=ChatOpenAI(model=model_name,api_key=os.getenv("api_key"),openai_base_url=os.getenv("endpoint"))
        elif model_provider == "Groq":
                llm=ChatGroq(model=model_name,api_key=os.getenv("groq_api"))
        

        tavily = TavilySearch(
            max_results=3,
            tavily_api_key=os.getenv("tavily")
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a smart and friendly AI assistant. Use the search results to answer accurately."),
            ("human", """ Question:{question} Search Results:{search_results}""")])

        chain = (
            {
                "question": lambda x: x["question"],
                "search_results": lambda x: tavily.invoke(x["question"])
            } | prompt | llm | StrOutputParser())

        response= chain.invoke({
            "question": query
        })
        return response

    
