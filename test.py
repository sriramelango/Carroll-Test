import streamlit as st
import numpy as np
import pandas as pd
import math 
import plotly.graph_objects as go
import plotly.express as px

# Set Page Options
st.title("The Carroll Grading Scale")
st.markdown("Success or Failure? She decides")
def grade(score1, score2):
    if score1 <= 60:
        score1 = (1/60) * score1
    elif score1 > 60:
        score1 = .2 * score1 - 11
    grade100 = (((.65 * score1) + (.35 * score2))/(.65 * 9 + .35 * 6)) * 100
    gradeScaled = (((.65 * score1) + (.35 * score2))/(.65 * 9 + .35 * 6)) * 9
    return grade100, gradeScaled

st.header("Grading Rubric Input")
scale1 = st.number_input('Input the number of points gained from the 9 scale (in a scale of 100)', step = 5)
scale2 = st.number_input('Input the number of points gained from the 6 scale', step = .5)

with st.expander("Grade Output"):
    grade100, gradeScaled = grade(scale1, scale2)
    st.success("Grade out of 9: " + str(round(gradeScaled,2)))
    st.info("Grade out of 100: " + str(round(grade100,2)))
    if grade100 > 90:
        st.balloons()

with st.expander("Grade Rubric Multivariable Graph"):

    rubricData = pd.read_csv('data.csv')
    fig = px.scatter_3d(rubricData, x='9-Point-Scale', y='6-Point-Scale', z='Grade', color='Grade', width=400, height=800)

    camera = dict(
        eye=dict(x=-1.5, y=-1.5, z=0.2)
    )
    fig.update_layout(scene_camera=camera)

    st.plotly_chart(fig, use_container_width=True)




