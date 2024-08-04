import streamlit as st
from src.retrieval_generation import generation
from src.data_ingestion import ingestdata
from dotenv import load_dotenv

load_dotenv()

vstore = ingestdata("None")
chain = generation(vstore)

def generate_response(user_input):
    return chain.invoke(user_input)

st.image("https://www.intuswindows.com/storage/uploads/0caecc87-725f-4bf7-88c3-e638bfec9cb2/logo-big-dark.svg", width=300)

if 'conversation' not in st.session_state:
    st.session_state.conversation = []


st.title("IntusWindow QA Chatbot by Vipul Munot")
st.write("Ask me anything about Windows!!")

user_input = st.text_input("Type your message here...", "")

if user_input:
    
    response = generate_response(user_input)
    
    
    st.session_state.conversation.append({"user": user_input, "bot": response})


for message in st.session_state.conversation:
    st.write(f"**You:** {message['user']}")
    st.write(f"**Bot:** {message['bot']}")
