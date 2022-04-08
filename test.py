import streamlit as st
import numpy as np
import pandas as pd
import math 
import matplotlib.pyplot as plt

# Set Page Options
st.title("The Carroll Test: Success or Fail")

st.markdown("""
* Mrs. Carroll, I make a modest proposal - if you are entering the grade of Sriram Elango, you should 100% make it a 100.
""")

def gradingScale(questionsCorrect):
    score = math.sqrt(questionsCorrect/30) * 100
    return score 

x = []
y = []
for i in range(30):
    x.append(i+1)
    y.append(gradingScale(i+1))

df = pd.DataFrame({'Questions Correct':x, 'Final Score':y})
st.header("Grading Rubric Input")
number = st.number_input('Input the number of questions correct:')
if st.button("Get Score"):
    with st.spinner("Wait for it..."):
        st.info(gradingScale(number))

        if gradingScale(number) > 80:

            st.balloons()
        
        else:

            st.error("Student beware - You are in for a scare")

st.header("Scoring Dataframe")
st.table(df)
st.header("Final Score Plotting")
st.line_chart(df['Final Score'])
