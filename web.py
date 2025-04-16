import streamlit as st
import function
from function import get_todos

todos = function.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    function.write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my todo app")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo..",
              on_change= add_todo, key= 'new_todo')




