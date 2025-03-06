import requests
import streamlit as st
import random

response = None
query= st.text_input("Enter your search query")

base_url="https://api.giphy.com/v1/gifs/search"
api_key= st.secrets.giphy.api_key

@st.cache
def get_giphy(query):
    params= {"q":query,
            "limit":10,
            "api_key":api_key
            }
    response=requests.get(base_url, params=params)
    return response

if query:
    response = get_giphy(query)

if response != None:
    for _ in range(9):
        image = response.json()["data"][_]["images"]["original"]["url"]
        st.image(image)
