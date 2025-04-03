import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/profile.jpeg", width=600)

with col2:
    st.title("Dylan Roach")
    content = """
    Hi there, my name is Dylan. I'm an FSU graduate with a bachelor's in meteorology and minor in programming. Currently, I work for
    the state of Florida as a Systems Project Consultant with the Department of Health. In my spare time, 
    I generally like to learn programming (currently learning Python) and hang out with my friends.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)