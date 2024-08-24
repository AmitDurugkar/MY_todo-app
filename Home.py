import streamlit as st
import function

todos = function.get_todos()

st.set_page_config (layout="wide")

def add_todos():
    todo = st.session_state["new todo"] +"\n"
    todos.append(todo)
    function.write_todos(todos)

st.title(" My Todo App ")
st.subheader("this is my todo app.")
st.write("<h1>This app is to be increase your <b> productivity </b> <h1> ", unsafe_allow_html= True)

st.text_input( label ="",placeholder="add a new todo... ",
               on_change=add_todos, key="new todo")



for index,todo in enumerate(todos):
    checkbox= st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


