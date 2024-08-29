import streamlit as st
from send_email import Send_email

st.header("Contact Me")

with st.form( key = "email forms"):
    user_email =st.text_input("your email address")
    raw_massage =st.text_area("your massage")
    massage=f"""\
    Subject: New Email from {user_email}
    From : {user_email}
    {raw_massage} """
    button =st.form_submit_button("submit")
    print(button)
    if button:
        Send_email(massage)
        st.info("your Email has been send sucessfully")
