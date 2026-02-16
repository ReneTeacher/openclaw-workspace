"""
To-Do List App - Streamlit
靚靚待辦事項清單
"""

import streamlit as st
import json
from pathlib import Path
from datetime import datetime

# ======== 設定 ========
st.set_page_config(
    page_title="To-Do List",
    page_icon="✅",
    layout="centered"
)

TODO_FILE = "todos.json"

# ======== CSS - 靚靚介面 ========
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
    }
    .todo-item {
        background: white;
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .todo-item.done {
        background: #f0f0f0;
        text-decoration: line-through;
        opacity: 0.7;
    }
    .add-btn {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        border: none;
        border-radius: 25px;
        padding: 15px 30px;
        color: white;
        font-weight: bold;
    }
    h1 {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .stats {
        background: white;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ======== Functions ========
def load_todos():
    if Path(TODO_FILE).exists():
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

# ======== Main App ========
st.title("✅ To-Do List")
st.markdown("**待辦事項清單**")

# Load todos
todos = load_todos()

# Show stats
pending = sum(1 for t in todos if not t.get('done', False))
done = sum(1 for t in todos if t.get('done', False))

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<div class="stats"><h2>{pending}</h2><p>緊要</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="stats"><h2>{done}</h2><p>已完成</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="stats"><h2>{len(todos)}</h2><p>總共</p></div>', unsafe_allow_html=True)

st.markdown("---")

# Add new todo
with st.form("add_form", clear_on_submit=True):
    col1, col2 = st.columns([4, 1])
    with col1:
        new_todo = st.text_input("加新項目 / Add new task:", placeholder="Enter task...")
    with col2:
        submitted = st.form_submit_button("➕ Add")
    if submitted and new_todo.strip():
        todos.append({
            "id": len(todos) + 1,
            "text": new_todo.strip(),
            "done": False,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        save_todos(todos)
        st.rerun()

st.markdown("---")

# Show todos
st.markdown("### 📋 你的項目 / Your Tasks")

if not todos:
    st.info("暫時未有項目 / No tasks yet")
else:
    for i, todo in enumerate(todos):
        col1, col2, col3 = st.columns([1, 6, 1])
        
        with col1:
            done = st.checkbox("", value=todo.get('done', False), key=f"cb_{i}")
            if done != todo.get('done', False):
                todo['done'] = done
                save_todos(todos)
                st.rerun()
        
        with col2:
            if todo.get('done', False):
                st.markdown(f"~~{todo['text']}~~")
                st.caption(f"✅ 已完成 / Completed: {todo.get('completed', '')}")
            else:
                st.markdown(f"**{todo['text']}**")
                st.caption(f"🕐 {todo.get('created', '')}")
        
        with col3:
            if st.button("🗑️", key=f"del_{i}"):
                todos.pop(i)
                save_todos(todos)
                st.rerun()

# Clear all
if todos and st.button("🗑️ 清除全部 / Clear All"):
    todos = []
    save_todos(todos)
    st.rerun()
