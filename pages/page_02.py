import streamlit as st
import requests

st.write('This is page 2')

st.write(st.secrets.my_secret_key)

image_response = requests.get(url="https://http.cat/200")
st.image(image_response.content)
