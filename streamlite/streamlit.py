# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:02:03 2022

@author: kaustubh.supe_coachh
"""
import pandas as pd
from nlp import Nlp
import streamlit as st

st.title("Verbatins :smile: :pensive: ")

uploaded_file = st.sidebar.file_uploader(label="upload csv", type=['csv','xlsx'])

global df
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

    except Exception as e:

        df = pd.read_excel(uploaded_file)

try:
    st.write(df)
except Exception as e:
    st.write("Please upload file to application")


result = st.button("Click Here")
if result:
    st.write(":smile:")
    #df = pd.read_csv(uploaded_file)
    x=Nlp(df)
