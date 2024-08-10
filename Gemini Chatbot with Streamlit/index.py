import streamlit as st
from dotenv import load_dotenv
import os
from groq import Groq
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit app layout
st.title("Llama 3 Chatbot")

st.write("This chatbot uses a large language model (LLM) to generate responses.")

# Display the conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box for user to ask a question
if user_input := st.chat_input("Ask a question..."):
    # Add the user's message to the chat history
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Generating response..."):
    # Generate a response using the OpenAI API
        response = client.chat.completions.create(
            messages=st.session_state.messages,
            model="llama3-8b-8192",
        )
    # Extract the assistant's reply
    assistant_message = response.choices[0].message.content

    # Add the assistant's reply to the chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})


    # Display the assistant's reply
    with st.chat_message("assistant"):
        st.markdown(assistant_message)
