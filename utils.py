import cohere
import streamlit as st
import os
import textwrap

from qa.bot import GroundedQaBot

# Serp API key
# https://serpapi.com/manage-api-key
serp_key = "99bdacc49c981c56debcd24eb068f5eebed6a273e37c1410584599a6fbf4155c"

# Cohere API key
cohere_key = "ehhm4nYOW8PfuTANFLVhC2Ea9wLpy69CAB89jv9T"

# Set up Cohere client
co = cohere.Client(cohere_key)


def generate_idea(topic, temperature, model='xlarge'):
  """
  Generate blog idea given a topic and temperature
  Arguments:
    industry(str): the blog's topic
    temperature(str): the Generate model `temperature` value
    model(str): The size of model {small, medium, large, xlarge}
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
    model=model, 
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

def generate_name(idea, temperature, model='xlarge'):
  """
  Generate blog title given a blog idea
  Arguments:
    idea(str): the startup idea
    temperature(str): the Generate model `temperature` value
    model(str): The size of model {small, medium, large, xlarge}
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
    model=model, 
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

def classify_sentiment(inputs, examples, model='medium'):
  ''' 
  Classify the sentiment of a given text
  Inputs:
    inputs(str|[str]): Pieces of text to classife
    examples(str|[str]|[cohere.Example]): A few examples to teach the learner
    model(str): The size of model {small, medium, large, xlarge}
    show_k(int): The number of classifications to show
  Returns:
    res(cohere.Classify.classifications): The predictions of the model
  '''
  response = co.classify(
        model=model,
        inputs=inputs,
        examples=examples,
      )
  
  
  res = response.classifications
  
 #labels = []
 # for label in res[0].labels.keys():
 #   labels.append(label)
    
 # scores = []
 # for confidence in res.confidence:
 #   score = confidence.confidence
 #   scores.append(score)
    
  return res


def wake_up_bot(question):
  '''
  Call bot and google possible answers to the given question
  Inputs:
    question(str): The question to answer
  Returns:
    answer
  '''
  # Set up QA Bot
  bot = GroundedQaBot(cohere_key, serp_key)
  
  answer = bot.answer(question)
  
  return answer


def scan_invoices(propmt, max_tokens=15, temperature=0.3, 
                  model='xlarge',
                  k=0, 
                  p=1, 
                  frequency_penalty=0, 
                  presence_penalty=0, 
                  stop_sequences=["--"], 
                  return_likelihoods='NONE'):
  
  '''
  Text2Text generator that given a prompt string that contains a task and 
  a few example scans generates text that achieves the given task.
  prompt(str): The prompt string
  ...
  '''
  response = co.generate(
    model=model,
    prompt=propmt,
    max_tokens=max_tokens, 
    temperature=temperature, 
    k=k, 
    p=p, 
    frequency_penalty=frequency_penalty, 
    presence_penalty=presence_penalty, 
    stop_sequences=["--"], 
    return_likelihoods='NONE'
    )
  
  text = response.generations[0].text
  
  return text