from Utils.config_loader import load_config
from pydantic import BaseModel,Field
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from typing import Literal
import os
from dotenv import load_dotenv
load_dotenv()




class Config_loader:

    def __init__(self):
        self.config=load_config()
    
    def __getitem__(self,key):
        return self.config[key]
    

class ModelLoader(BaseModel):
    model_provider: Literal["OpenAI","Groq"] = "OpenAI"
    config: Config_loader = None  

    def model_post_init(self, __context):
        self.config = Config_loader() 


    class Config:
        arbitrary_types_allowed=True

    def llm_loader(self):
        
        if self.model_provider =="OpenAI":
            print("openai model")
            api_key=os.getenv("api_key")
            model_name=self.config["LLM"]["OpenAI"]["model_name"]
            base_api=os.getenv("endpoint")
            llm=ChatOpenAI(model=model_name,api_key=api_key,openai_api_base=base_api)
        elif self.model_provider =="Groq":
            print("groq")
            apikey=os.getenv("groq_api")
            model_name=self.config["LLM"]["Groq"]["model_name"]
            llm=ChatGroq(model=model_name,api_key=apikey)
        return llm

        

