import streamlit as st
from Logic.budget import calculate_return
import time
import os
from datetime import datetime
from google.oauth2.service_account import Credentials
import gspread
import json
# --- Session State Initialization ---
for key, default in {
    "calculated": False,
    "age": "",
    "amount": "",
    "habit": "",
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# --- App Title and Intro ---
st.title("🚨 The 1% Guilt Trip")
st.markdown("*Spend 1% less on your **stupidest habit**. Get 100% richer.*")

# --- Input Section ---
st.subheader("🧠 Let’s Diagnose the Damage")

st.session_state.age = st.text_input("How old are you?", value=st.session_state.age, placeholder="e.g. 23")
st.session_state.habit = st.selectbox(
    "What’s your **guiltiest** spend?",
    ["DoorDash", "Boba Tea", "Uber", "Vapes", "Monster", "Other"],
    index=None,
    placeholder="Pick your poison..."
)
st.session_state.amount = st.text_input("How much $$ do you burn monthly on this?", value=st.session_state.amount, placeholder="e.g. 120")

# --- Calculate Button ---
if st.button("🔥 Calculate My Financial Self-Sabotage"):
    st.session_state.challenge_started = True
    st.switch_page("pages/4_Result.py")
