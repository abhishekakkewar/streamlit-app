import streamlit as st

st.set_page_config(page_title="My First App")

st.title("🚀 My Streamlit App")
st.write("Hello!")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name} 👋")
