import streamlit as st
import sqlite3
from gpt4allj import Model
from streamlit_option_menu import option_menu

st.set_page_config(layout='wide')

model = Model('ggml-gpt4all-j.bin')

# Function to create the database table if it doesn't exist
def create_table():
    conn = sqlite3.connect('conversation.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert a message into the database
def insert_message(role, content):
    conn = sqlite3.connect('conversation.db')
    c = conn.cursor()
    c.execute('INSERT INTO messages (role, content) VALUES (?, ?)', (role, content))
    conn.commit()
    conn.close()

# Function to retrieve all messages from the database
def get_messages():
    conn = sqlite3.connect('conversation.db')
    c = conn.cursor()
    c.execute('SELECT role, content FROM messages')
    messages = [{'role': role, 'content': content} for role, content in c.fetchall()]
    conn.close()
    return messages

def show_messages():
    messages = get_messages()

    # Display messages in a chat-like format
    for message in messages:
        if message['role'] == 'You':
            st.sidebar.markdown(f'<div style="background-color: "#262730"; padding: 10px; border-radius: 5px;">{message["role"]}: {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f'<div style="background-color: "#262730"; padding: 10px; border-radius: 5px;">{message["role"]}: {message["content"]}</div>', unsafe_allow_html=True)

def main():
    create_table()

    st.title("ConvoGem-alternate to chatgpt")

    with st.sidebar:
        st.sidebar.title("Chat History")
        show_messages()

    st.markdown(""" <style> .font {
                        font-size:30px ; font-family: 'Cooper Black'; color: #02ab21;} 
                        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">GPT4 Playground :</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    new_chat_placeholder = col1.empty()  # Create an empty space to display new chat messages

    with col1:
        prompt = st.text_input("You:", value="")
        if st.button("Send"):
            with st.spinner("Generating response..."):
                insert_message("You", prompt)
                message_response = model.generate(prompt)
                insert_message("AI", message_response)
                show_messages()

                # Display the new chat message below the "Send" button
                new_chat_placeholder.markdown(
                    f'<div style="background-color: "#262730"; padding: 10px; border-radius: 5px;">You: {prompt}</div>', 
                    unsafe_allow_html=True
                )
                new_chat_placeholder.markdown(
                    f'<div style="background-color: "#262730"; padding: 10px; border-radius: 5px;">AI: {message_response}</div>', 
                    unsafe_allow_html=True
                )

    with col2:
        if st.button("Clear"):
            conn = sqlite3.connect('conversation.db')
            c = conn.cursor()
            c.execute('DELETE FROM messages')
            conn.commit()
            conn.close()
            show_messages()

if __name__ == "__main__":
    main()
