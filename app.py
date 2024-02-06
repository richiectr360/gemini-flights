import streamlit as st

# Create a list to store chat messages
chat_history = []

# Streamlit app layout
def main():
    st.title("Gemini Flights Streamlit App")

    # Initialize session state
    if "enter_pressed" not in st.session_state:
        st.session_state.enter_pressed = False

    # Sidebar for creating new chats
    with st.sidebar:
        st.header("Create New Chat")
        new_chat_button = st.button("New Chat")

    # Display chat messages
    display_chat()

    # Empty container for positioning chat textbox at the bottom
    chat_textbox_container = st.empty()

    # User input for sending messages
    user_input = chat_textbox_container.text_input("Your Message:", key="user_input", value="", help="Press Enter to send")
    if st.button("Send") or st.session_state.enter_pressed:
        send_message(user_input)

    # Handle new chat creation
    if new_chat_button:
        chat_history.clear()
        st.text("New chat created.")

# Function to display chat messages
def display_chat():
    if len(chat_history) > 0:
        st.markdown("---")
        for message in chat_history:
            if message["sender"] == "user":
                st.text_input("You:", value=message["text"], key=message["timestamp"], disabled=True)
            else:
                st.text_area("Gemini Flights:", value=message["text"], key=message["timestamp"], disabled=True)
        st.markdown("---")

# Function to send user messages and get Gemini Flights responses
def send_message(user_input):
    if user_input:
        # Add user message to chat history
        chat_history.append({"sender": "user", "text": user_input, "timestamp": st.timestamp()})

        # Simulate Gemini Flights response (replace this with actual backend interaction)
        chatbot_response = "Hello! I'm Gemini Flights. You said: " + user_input

        # Add Gemini Flights response to chat history
        chat_history.append({"sender": "chatbot", "text": chatbot_response, "timestamp": st.timestamp()})

        # Clear user input field
        st.session_state.user_input = ""

        # Update the display
        display_chat()

if __name__ == "__main__":
    main()


