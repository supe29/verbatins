# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:02:03 2022

@author: kaustubh.supe_coachh
"""
import pandas as pd
from nlp import Nlp
import streamlit as st

df=pd.DataFrame(columns=['uuid','name','type','first_name','last_name','finished_at','group_name','label','answer','sentiment'])

st.title("Verbatims :smile: :pensive: ")

uploaded_file = st.sidebar.file_uploader(label="upload csv", type=['csv','xlsx'])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

    except Exception as e:

        df = pd.read_excel(uploaded_file)

try:
    st.write(df)
except Exception as e:
    st.write("Please upload file to application")


st.download_button(
     label="Download data as CSV",
     data=Nlp(df),
     file_name='sentiments.csv',
     mime='text/csv',
 )
