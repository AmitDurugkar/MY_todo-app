import streamlit as st
import pandas

st.set_page_config(layout='wide')


col1,col2 =st.columns(2)

with col1:
 st.title("The Best company")
content = """Content marketing examples include media like newsletters, podcasts, social media posts, and videos.
  All of these forms of content are meant to provide useful and relevant information that delights users and Python, and Power BI, with a strong track record of delivering 
    actionable insights to drive business growth. Proven ability to interpret complex data sets and
    communicate findings effectively. Committed to leveraging data-driven strategies for optimizing 
    operations and enhancing decision-making processes."""
st.info(content)

with col2 :
   content1= """ o help you use content marketing to your company's advantage, here are some of my favorite content marketing examples of 2022."""
st.info(content1)

st.title("Our team")


col3,col4,col5= st.columns(3)

df=pandas.read_csv("data.csv")


with col3:

    for index,row in df[:4].iterrows():
        st.header(row['first name'].title()+ ' ' + row['last name'].title())
        st.subheader(row['role'])
        st.image("images/" + row["image"])

with col4:
    for index,row in df[4:8].iterrows():
     st.header(row['first name'].title() + ' ' + row['last name'].title())
     st.subheader (row['role'])
     st.image("images/" + row["image"])


with col5:
    for index,row in df[8:12].iterrows():
     st.header(row['first name'].title() + ' ' + row['last name'].title())
     st.subheader (row['role'])
     st.image("images/" + row["image"])



