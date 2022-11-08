import cohere
import streamlit as st
import os
import textwrap

# Cohere API key
#api_key = os.environ["gkskuLP90nd6kNRkpwfMkQQ1ckW5u5GdJP0gQIIV"]

# Set up Cohere client
co = cohere.Client('ehhm4nYOW8PfuTANFLVhC2Ea9wLpy69CAB89jv9T')

def generate_idea(topic, temperature):
  """
  Generate blog idea given a topic and temperature
  Arguments:
    industry(str): the blog's topic
    temperature(str): the Generate model `temperature` value
  Returns:
    response(str): the blog idea
  """
  base_idea_prompt = textwrap.dedent("""
    This program generates a blog idea given the topic.
    Topic: Technology
    Blog Idea: A hands-on tutorial on running XGBoost with Python
    --
    Topic: Technology
    Blog Idea: What are the most promising emerging technologies?
    --
    Topic: Economics
    Blog Idea: The role of Reinforcement Learning in decision theory
    --
    Topic: Economics
    Blog Idea: Exploring Nash Equilibria
    --
    Topic: ML
    Blog Idea: Implementing RNN with Pytorch
    --
    Topic: Economics and ML
    Blog Idea: Machine learning models for economists
    --
    Topic:""")

  # Call the Cohere Generate endpoint
  response = co.generate( 
    model='xlarge', 
    prompt = base_idea_prompt + " " + topic + "\Blog Idea: ",
    max_tokens=50, 
    temperature=temperature,
    k=0, 
    p=0.7, 
    frequency_penalty=0.1, 
    presence_penalty=0, 
    stop_sequences=["--"])
  startup_idea = response.generations[0].text
  startup_idea = startup_idea.replace("\n\n--","").replace("\n--","").strip()

  return startup_idea

def generate_name(idea, temperature):
  """
  Generate blog title given a blog idea
  Arguments:
    idea(str): the startup idea
    temperature(str): the Generate model `temperature` value
  Returns:
    response(str): the startup name
  """
  base_name_prompt= textwrap.dedent("""
    This program generates a blog title given the blog idea and temperature.
    Blog Idea: The role of Reinforcement Learning in decision theory and usage within Economics
    Blog Name: Reinforced Economics
    --
    Blog Idea: Hands-on tutorial on single-qubit quantum computing to explain code and concepts.
    Blog Name: Single-Qubit Quantum Computing 
    --
    Blog Idea: Understanding the importance of understanding causality and incorporating CausalML tools in economics.
    Blog Name: Hey Siri, tell me why...
    --
    Blog Idea: A hands-on tutorial on implementing RNNs in python 
    Blog Name: RNN: An introduction with Python
    --
    Blog Idea:
    """)

  # Call the Cohere Generate endpoint
  response = co.generate( 
    model='xlarge', 
    prompt = base_name_prompt + " " + idea + "\Blog title:",
    max_tokens=10, 
    temperature=temperature,
    k=0, 
    p=0.7, 
    frequency_penalty=0, 
    presence_penalty=0, 
    stop_sequences=["--"])
  
  blog_name = response.generations[0].text
  blog_name = blog_name.replace("\n\n--","").replace("\n--","").strip()

  return blog_name

# The front end code starts here
