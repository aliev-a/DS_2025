import streamlit as st
import pandas as pd

st.title('🤖 MY FIRST PROJECT')

st.write('Lets do it!')

with st.expander("DATA"):
  st.write('**OUR DATA**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

with st.expander("Visualization"):
  st.scatter_chart(data=df, x='bill_lenght_mm', y='bill_depth_mm', color='species')
