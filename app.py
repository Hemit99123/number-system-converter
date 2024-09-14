import streamlit as st
from pages import page_one, page_two, page_three

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Binary to Decimal", "Decimal to Binary", "Hexadecimal to Binary"])

# Render the selected page
if page == "Binary to Decimal":
    page_one()
elif page == "Decimal to Binary":
    page_two()
elif page == "Hexadecimal to Binary":
    page_three()