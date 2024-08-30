import streamlit as st
from Send_email import send_email
import pandas

df=pandas.read_csv("topic.csv")

with st.form(key ="email form"):
    user_email=st.text_input("Enter your email address")
    option=st.selectbox(
        'What topic do you want to discuss',
        df["topic"])
    raw_massage=st.text_area("Text")
    massage = f"""\
    Subject:New email from {user_email}
    from:{user_email}
    topic{option}
    {raw_massage}
    """
    button=st.form_submit_button("submit")
    if button:
        send_email(massage)
        st.info("your email was send sucessfully")