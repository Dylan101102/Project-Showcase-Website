import streamlit as st
import pandas
from PIL import Image

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    image = Image.open("images\profile.jpeg")
    new_image = image.resize((600, 600))
    st.image(new_image)

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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

dataframe = pandas.read_csv("data.csv", sep=";")
#print(dataframe)
with col3:
    for index, row in dataframe[:10].iterrows(): # [:10] means the first 10.
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in dataframe[10:].iterrows(): # [:10] means everything after the tenth.
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")