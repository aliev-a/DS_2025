import streamlit as st

st.title('🤖 MY FIRST PROJECT')

st.write('Lets do it!')

with st.expander("DATA"):
  st.write('**OUR DATA**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
