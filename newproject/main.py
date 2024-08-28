import  streamlit as st
import pandas

st.set_page_config(layout= "wide")

col1, col2= st.columns(2)

with col1 :
    st.image("venv/image/travel-agent-d.jpg")

with col2 :
    st.title("Amit Durugkar")
    content ="""Driven and analytical data analyst with 10+ years of experience in the banking industry. 
    Proficient in SQL, Python, and Power BI, with a strong track record of delivering 
    actionable insights to drive business growth. Proven ability to interpret complex data sets and
    communicate findings effectively. Committed to leveraging data-driven strategies for optimizing 
    operations and enhancing decision-making processes."""

st.info(content)

content2 ="""below you can find some apps i have built in phython. feel free to contact me.."""

st.write(content2)

col3,empty_column,col4 =st.columns([2,.75,2])

df = pandas.read_csv("data.csv",sep=";")

with col3:
      for index ,row in df[:10].iterrows():
         st.header(row["title"])
         st.write(row["description"])
         st.image("venv/image/"+ row["image"])
         st.write( f"[source code]({row['url']})")

with col4:
      for index ,row in df[10:].iterrows():
         st.header(row["title"])
         st.write(row["description"])
         st.image("venv/image/" + row["image"])
         st.write(f"[source code]({row['url']})")



