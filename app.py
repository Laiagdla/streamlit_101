import streamlit as st
import requests

st.text('my first app')

st.markdown("""
    # Hello

    ## tiny hello

    **bold** or *italic* text with [links](http://github.com/streamlit) and:
    - bullet points
    - more bullet points

    ---
""")


clicked = st.button('click me')

st.write(clicked)

if clicked:
    st.write('🎊 surprice!!!! 🥳🎉🎉🎉')
else:
    st.write('what you waiting for?')

st.markdown("---")

with st.form(key='params for api'):

    x = st.slider('value for x',1,100, 1)
    y = st.slider('value for y',1,100, 1)

    st.form_submit_button("Submit")

params= {'x':x, 'y':y}
st.write(params)
url="https://dummy-calculator-api-6uynt4qmzq-ew.a.run.app/calc"

response = requests.get(url, params=params)
st.write(response.url)
st.write(response.json())

    # st.write(response.json())
