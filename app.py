import streamlit as st

st.set_page_config(layout="wide", page_title="Budget", page_icon="💰")

st.title("💰 BudgetAI")
st.write("Budgeting made simple")

if st.button("Get Started", type="primary"):
    st.switch_page("pages/1_Input.py")

st.sidebar.markdown("""
### How It Works
1. Enter your spending
2. Get personalized advice
3. Optimize your finances
""")
