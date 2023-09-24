import streamlit as st
import pandas as pd
from IPython.display import HTML

st.markdown("# Nfast 📘")

st.header('Nfast')

video_url = 'https://drive.google.com/file/d/1YOC26xKnIQq8hwkc-T00_d4-7jOE6Cim/preview'
video_html = f'<iframe src="{video_url}" width="640" height="360" frameborder="0" allowfullscreen="true"></iframe>'
st.markdown(video_html, unsafe_allow_html=True)

