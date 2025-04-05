import streamlit as sl
from streamlit import session_state

def getTodos():
    with open(r'todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

def writeTodos(todos):
    with open(r'todos.txt', 'w') as file:
        file.writelines(todos)

def addTodo():
    todoToAdd = sl.session_state["add"]
    todos.append(f'{todoToAdd} \n')
    writeTodos(todos)

sl.title("My todo app")

todos = getTodos()
for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        writeTodos(todos)
        del session_state[todo]
        sl.rerun()

sl.text_input(label='', placeholder="Add a new todo...", on_change=addTodo, key="add")


