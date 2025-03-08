import streamlit as st
import random

# Initialize session state variables if not already set
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Apply custom CSS for background and styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #A1C4FD, #C2E9FB);  /* Light Blue to Light Purple */
        }
        .main {
            background: rgba(255, 255, 255, 0.9); /* White with Transparency */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
        }
        .stButton>button {
            background-color: #90EE90 !important;  /* Light Green */
            color: black !important;  /* Dark Text for Visibility */
            border-radius: 8px;
            padding: 12px 25px;
            font-size: 16px;
            font-weight: bold;
            border: none;
        }
        h1 {
            color: darkblue !important;
            text-align: center;
        }
        .stNumberInput label, .stTextInput label, .stMarkdown {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)


# st.markdown('<div class="main">', unsafe_allow_html=True)

st.title("🎯 Number Guessing Game")

st.write("Guess a number between 1 and 100")

guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

if st.button("Submit") and not st.session_state.game_over:
    st.session_state.attempts += 1
    
    if guess < st.session_state.random_number:
        st.write("🔼 Too low! Try again.")
    elif guess > st.session_state.random_number:
        st.write("🔽 Too high! Try again.")
    else:
        st.write(f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
        st.session_state.game_over = True

st.write(f"Attempts: {st.session_state.attempts}")

if st.button("🔄 Reset", key="reset_button"):

    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.markdown('</div>', unsafe_allow_html=True)
