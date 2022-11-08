# STREAMLIT DASHBOARD [Page 2]
import cohere
import streamlit as st
import os
import textwrap
from utils import generate_idea, generate_name

st.title("🚀 Brainstorm Boiler Room")

form = st.form(key="user_settings")
with form:
  st.write("Enter a topic [Example: Technology, Economics, AI, ML] ")
  # User input - Industry name
  topic_input = st.text_input("Topic", key = "topic_input")

  # Create a two-column view
  col1, col2 = st.columns(2)
  with col1:
      # User input - The number of ideas to generate
      num_input = st.slider(
        "Number of ideas", 
        value = 3, 
        key = "num_input", 
        min_value=1, 
        max_value=10,
        help="Choose to generate between 1 to 10 ideas")
  with col2:
      # User input - The 'temperature' value representing the level of creativity
      creativity_input = st.slider(
        "Creativity", value = 0.5, 
        key = "creativity_input", 
        min_value=0.1, 
        max_value=0.9,
        help="Lower values generate more “predictable” output, higher values generate more “creative” output")  
  # Submit button to start generating ideas
  generate_button = form.form_submit_button("Generate Idea")

  if generate_button:
    if topic_input == "":
      st.error("Don't forget to specify a topic!")
    else:
      my_bar = st.progress(0.05)
      st.subheader("Blog Ideas:")

      for i in range(num_input):
          st.markdown("""---""")
          blog_idea = generate_idea(topic_input, creativity_input)
          blog_name = generate_name(blog_idea, creativity_input)
          st.markdown("##### " + blog_name)
          st.write(blog_idea)
          my_bar.progress((i+1)/num_input)