import streamlit as st
import function

todos = function.get_todos()

st.title("My To-Do App")
st.subheader("This is my todo app")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo..")




