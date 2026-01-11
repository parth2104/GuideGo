import streamlit as st
import requests

st.set_page_config(page_title="AI Chatbot",layout= "centered")
st.header("AI Chatbot")
st.title("AI Chatbot Assistant")
st.write("Create and intaract an AI agent")
system_prompt=st.text_area("Define your AI agent",height=70,placeholder="Type your system prompt here")

model_name_groq=["llama-3.1-8b-instant"]
model_name_openai=["gpt-5-mini-2025-08-07"]

provider=st.radio("select provider",("OpenAI","Groq"))

if provider =="Groq":
    selected_model=st.selectbox("Select Groq Model",model_name_groq)
elif provider =="OpenAI":
    selected_model=st.selectbox("select OpeanAI Model",model_name_openai)

query=st.text_area("Ask anything",height=70,placeholder="write your query")

api_url="http://127.0.0.1:8000/chat"

if st.button("Aske Agent"):
    if query.strip():

        payload={
             "model_name":selected_model,
             "model_provider": provider,
             "system_prompt": system_prompt,
             "messages": query

        }
        
        response=requests.post(api_url,json=payload)
        if response.status_code ==200:
            response_data=response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                 st.subheader("Agent rsponse")
                 st.markdown(response_data)
            
            
                    
                    
