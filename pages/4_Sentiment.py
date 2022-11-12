# STREAMLIT DASHBOARD [Page 3]
import cohere as co
import pandas as pd
import streamlit as st
import os
import textwrap
from utils import generate_idea, generate_name, classify_sentiment
from cohere.classify import Example

st.title("HAS ERRORS DO NOT USE - 11/09/2022")

# What do I want this bot be good at answering? -> Reviews, tweets,...?
examples=[
  Example("The order came 5 days early", "positive"), 
  Example("The item exceeded my expectations", "positive"), 
  Example("I ordered more for my friends", "positive"), 
  Example("I would buy this again", "positive"), 
  Example("I would recommend this to others", "positive"), 
  Example("The package was damaged", "negative"), 
  Example("The order is 5 days late", "negative"), 
  Example("The order was incorrect", "negative"), 
  Example("I want to return my item", "negative"), 
  Example("The item\'s material feels low quality", "negative"), 
  Example("The product was okay", "neutral"), 
  Example("I received five items in total", "neutral"), 
  Example("I bought it from the website", "neutral"), 
  Example("I used the product this morning", "neutral"), 
  Example("The product arrived yesterday", "neutral"),
]

inputs=[
  "This item was broken when it arrived",
  "The product is amazing",
  "The product was not too bad",
]

st.title("🔮 The shrink")
st.subheader("Give the shrink a prompt and it will tell you its sentiment! Good for tweets, emails and checking overall sentiment of a market for instance.")

form = st.form(key="user_settings")
with form:
  st.write("Enter a sentence, word or other text.")
  # User input - Industry name
  text_input = st.text_input("Input", key = "text_input")

  # Submit button to start generating ideas
  generate_button = form.form_submit_button("Shake the magic ball")
  if generate_button:
    if text_input == "":
      st.error("Don't forget to give a prompt!")
    else:
      my_bar = st.progress(0.5)
      st.subheader("Predictions:")

      res = classify_sentiment([text_input], examples)
      
      st.write("Look, I'm no genie but this is how I would classify it")
      #st.write(pd.DataFrame({"Labels": labels, "Scores": scores}))
      st.write(res)
