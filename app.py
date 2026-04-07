#import streamlit as st

#st.set_page_config(page_title="My First App")

#st.title("🚀 My Streamlit App")
#st.write("Hello!")

#name = st.text_input("Enter your name")

#if name:
#   st.success(f"Hello {name} 👋")

import streamlit as st

st.set_page_config(page_title="My First App")

# -----------------------------
# Get user_id from query params
# -----------------------------
query_params = st.query_params
user_id = query_params.get("user_id", None)

# -----------------------------
# UI
# -----------------------------
st.title("🚀 My Streamlit App")

if user_id:
    user_id = str(user_id)
    st.success(f"User ID: {user_id} logged in")
else:
    st.warning("No user ID found. Please login from React app.")

# -----------------------------
# Optional: Access Control
# -----------------------------
allowed_users = ["1", "2", "3", "4", "5"]

if user_id and user_id not in allowed_users:
    st.error("❌ Access Denied")
    st.stop()

# -----------------------------
# Your existing logic
# -----------------------------
st.write("Hello!")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name} 👋")
