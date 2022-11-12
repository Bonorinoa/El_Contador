# STREAMLIT DASHBOARD [Page 4]
import cohere as co
import streamlit as st
import os
import textwrap
from utils import generate_idea, generate_name, classify_sentiment, wake_up_bot
from cohere.classify import Example

st.title("🧞 The genie")
st.subheader("You get 3 questions! Make them count...")

form = st.form(key="user_settings")
with form:
  st.write("Ask me anything")
  # User input - Industry name
  question = st.text_input("Question", key = "question")

  # Submit button to start generating ideas
  generate_button = form.form_submit_button("Ask.")
  if generate_button:
    if question == "":
      st.error("Sure you don't wan't to ask anything?")
    else:
      my_bar = st.progress(0.05)
      st.subheader("Answers:")
      
      answers = wake_up_bot(question)
      
      st.write(answers)