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
    try:
        age = int(st.session_state.age)
        amount = float(st.session_state.amount)
        habit = st.session_state.habit

        if not habit:
            st.warning("Please pick a habit.")
        elif age < 16 or age > 100:
            st.warning("Come back when you’re old enough to waste *your own* money.")
        elif amount <= 0:
            st.warning("Nice try... want me to guess how much you're spending?")
        else:
            st.session_state.calculated = True
            st.session_state.valid_age = age
            st.session_state.valid_amount = amount
            st.session_state.valid_habit = habit
    except ValueError:
        st.warning("Please enter valid numbers for age and amount.")

# --- Show Result if Valid ---
if st.session_state.calculated:
    age = st.session_state.valid_age
    amount = st.session_state.valid_amount
    habit = st.session_state.valid_habit

    death_age = 80
    years_left = death_age - age
    st.markdown(f"⏳ You’ve got about **{years_left} years** left—and you’re burning them on **{habit}**.")

    # Roasts
    roasts = {
        "DoorDash": f"**Pathetic.** You pay *${amount}/mo* because *walking* is hard? Your future self *hates* you.",
        "Boba Tea": f"**${amount} on sugar water?** Congrats—you *literally* piss away your retirement.",
        "Uber": "**No license?** Not even trying to save money, huh.",
        "Vapes": "**Vapes??** Are you in middle school or just really into bankruptcy?",
        "Monster": "**At least tell me it's the white can.**",
        "Other": "**Not even on the list?** Not worth your money *or* your shame."
    }
    st.error(roasts.get(habit, roasts["Other"]))

    # Financial Future
    st.subheader("💸 What You’re Actually Losing")
    what_if = calculate_return(amount, age, 65, 0.08)
    st.markdown(
        f"""
        <div style="font-size:1.25rem; margin-bottom:1.5rem;">
            If you invested that instead, you’d have:
        </div>
        <div style="font-size:2rem; font-weight:700; color:#10B981;">
            ${what_if:,.0f}
        </div>
        <div style="font-size:1rem; color:#6B7280; margin-top:0.5rem;">
            by age 65 (at 8% annual return)
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.toggle("📊 Show calculation details"):
        st.markdown(f"""
        - Monthly investment: **${amount}**
        - Years invested: **{65 - age}**
        - Annual return: **8%**
        - Formula: `FV = PMT × (((1 + r)ⁿ - 1) / r)`
        """)

    # Email Capture
    st.subheader("📬 Tired of Budget Apps That Overcomplicate Everything?")

    st.markdown(
        """
    We’re building a **simple, fun alternative** to traditional budget apps.

    No spreadsheets. No lectures. Just a piggy bank, your guilty habit, and a daily nudge to save **1% smarter**.

    Drop your email if you're tired of apps that tell you what to do but never actually help.
    """
    )

    #from oauth2client.service_account import ServiceAccountCredentials

    # --- Google Sheets Setup ---
    def save_to_sheets(email):
        try:
            # Updated auth flow
            scope = ["https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/drive"]
            
            creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
            client = gspread.authorize(creds)
            
            sheet = client.open("1PercentGuiltTrip_Emails").sheet1
            sheet.append_row([
                email.strip(), 
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])
            return True
        except Exception as e:
            st.error(f"Error saving: {str(e)}")
            return False

    # --- In your Streamlit code ---
    email = st.text_input("Enter your email:")

    if st.button("Notify Me"):
        if "@" in email and "." in email:
            if save_to_sheets(email):
                st.success("🎉 Saved successfully!")
                st.balloons()
        else:
            st.warning("Please enter a valid email")
    # --- Share to Twitter ---
    tweet_text = f"I realized my ${habit} habit is costing me ${amount}/mo. If I just invested that instead, I'd have ${what_if:,.0f} by age 65. RIP to past me. #UnBudget #1PercentHabit "
    tweet_url = f"https://twitter.com/intent/tweet?text={tweet_text.replace(' ', '%20')}"

    st.markdown("### 🐦 Share the shame:")
    st.markdown(
        f"""<a href="{tweet_url}" target="_blank">
        <button style="background-color:#1DA1F2;border:none;color:white;padding:10px 16px;
        text-align:center;text-decoration:none;display:inline-block;font-size:16px;border-radius:5px;">
        📣 Tweet This
        </button></a>""",
        unsafe_allow_html=True
    )
    # Reset
    st.markdown("---")
    if st.button("🔁 Start Over"):
        for key in ["age", "amount", "habit", "calculated", "valid_age", "valid_amount", "valid_habit"]:
            st.session_state[key] = "" if "age" in key or "amount" in key or "habit" in key else False
        st.rerun()
