import streamlit as st
import numpy as np
import pandas as pd

# Set Page Options
st.title("The Carroll Test: Success or Fail")

st.markdown("""
* Mrs. Carroll, I make a modest proposal - if you are entering the grade of Sriram Elango, you should 100% make it a 100.
""")

def gradingScale(questionsCorrect):
    questionsWrong = 30 - questionsCorrect
    score = (100 - (2 *questionsWrong))
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

st.header("Scoring Dataframe")
st.table(df)