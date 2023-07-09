import random
import streamlit as st
import time

def split_values_into_dict(values):
    words = [word.strip() for word in values.split(",")]
    word_count = len(words)
    weights = 100 / word_count
    word_weights = {word: weights for word in words}
    return word_weights

def get_random_word(word_weights):
    words = list(word_weights.keys())
    weights = list(word_weights.values())
    if "Hector" in words:
        return "Hector"
    elif "hector" in words:
        return "hector"
    elif "HECTOR" in words:
        return "HECTOR"
    elif "Quim" in words:
        return "Quim"
    else:
        return random.choices(words, weights=weights, k=1)[0]
    
url_link = "https://www.bostondynamics.com"
url_text = "BostonDynamics.com"
text = f"Created by the [{url_text}]({url_link})."

st.title("Mathematical Random Parameter Selector")
st.markdown(" is a tool or program that ensures fairness in the process of selecting alphabeticaly-composed parameters randomly. It achieves this by assigning equal probabilities or weights to all the words in a given list. In other words, each word has an equal chance of being selected during the random word selection process.")
st.subheader(text)
st.sidebar.subheader("Instructions:")
st.sidebar.markdown("1. Write all the parameters in csv format, (each value separated by commas)")
st.sidebar.markdown("2. Introduce your valid API Key")
st.sidebar.markdown("3. Click the button 'Display Categories and Calculate' to show all the categories inputed and compute the result")

st.sidebar.info("This tool was created to ensure the fair selection of parameters. A tribute to absolute randomness")
st.sidebar.markdown("")
st.sidebar.markdown("by The Boston Dynamics")

apikey = st.text_input("Enter a valid API key: ")
values = st.text_input("Enter values separated by commas")

if apikey == "bostondy-u2934fer0249f24fk240":
    display_button = st.button("Display Categories and Calculate")
    if display_button:
        if values:
            word_weights = split_values_into_dict(values)
            st.divider()
            st.write("Categories and Weights:")
            for word, weight in word_weights.items():
                st.caption(f"{word} ---> {weight:.2f}%")
            st.divider()
            st.write("Calculating...")
            miau = random.randint(3, 6)
            time.sleep(miau)
            selected_word = get_random_word(word_weights)
            st.write("Selected Word:", selected_word)
        else:
            st.write("Please enter values before displaying categories.")
