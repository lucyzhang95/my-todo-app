import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout='wide')


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app. 这是一款记录事情的App。")
st.write("This app is to increase your <b>productivity</b>."
         "它可以帮助你提升工作的效率！",
         unsafe_allow_html=True)

st.text_input(label="", placeholder="Add a new todo.../加入一个新的事情",
              on_change=add_todo, key='new_todo')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# Each user session is separate from other user sessions
# (cpu of the webserver is going to handle the requests)
# (It is important to have sufficient hardware ram and cpus.)
