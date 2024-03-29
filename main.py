import streamlit as st
import functions

todos = functions.get_todos()
st.set_page_config(layout="wide")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.get_write_todos("todo.txt", todos)


def delete_item():
    functions.truncate()
    st.write("Deleted successfully")


st.title("Todo App")
st.write("click on boxes to <b>delete item</b>",
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    button = st.button(todo, key=todo)
    if button:
        todos.pop(index)
        functions.get_write_todos("todo.txt", todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add an item",
              on_change=add_todo, key="new_todo")

st.button(label="clear bucket list", on_click=delete_item)