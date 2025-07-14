import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import os
from Logic.budget import calculate_return
if not st.session_state.get("challenge_started", False):
    st.warning("⛔ Access denied. Start from the challenge page.")
    st.stop()
# --- Get session values ---
habit = st.session_state.get("habit", "DoorDash")
amount = st.session_state.get("amount", 150)
age = st.session_state.get("age", 25)
COUNTER_FILE = "reminder_toggle_count.txt"

if not os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "w") as f:
        f.write("0")
# --- Financial Calculation ---
what_if = calculate_return(amount, age, 65, 0.08)  # Make sure this matches your function


# --- UI Layout ---
st.title("💸 Financial Reality Check")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
        f"""
        <div style="font-size:1.25rem; margin-bottom:1.5rem;">
            Your <b>{habit}</b> habit costs <b>${amount}/mo</b>.
            Invested instead, that becomes:
        </div>
        <div style="font-size:2rem; font-weight:700; color:#10B981;">
            ${what_if:,.0f}
        </div>
        <div style="font-size:1rem; color:#6B7280; margin-top:0.5rem;">
            by age 65 (assuming 8% returns)
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.toggle("Show calculation"):
        st.markdown(f"""
            - Monthly investment: ${amount}
            - Years invested: {65 - age}
            - Annual return: 8%
            - Future value formula: `FV = PMT × (((1 + r)ⁿ - 1) / r)`
        """)
st.markdown("### 📱 Want a Daily Nudge?")

if "reminder_toggle_clicked" not in st.session_state:
    st.session_state.reminder_toggle_clicked = False

wants_reminder = st.toggle("Text me a daily reminder to track my 1% win (feature coming soon)")

if wants_reminder and not st.session_state.reminder_toggle_clicked:
    st.session_state.reminder_toggle_clicked = True
    st.success("Noted! (Reminders not active yet.)")
# with col2:
#     sharecard = generate_apple_clean_sharecard(habit, amount, what_if)
#     st.image(sharecard, use_column_width=True)
#     st.download_button(
#         label="Download Sharecard",
#         data=sharecard,
#         file_name=f"sharecard_{habit}.png",
#         mime="image/png"
#     )

# --- Navigation ---
st.markdown("---")
if st.button("🔁 Analyze Another Habit", type="primary"):
    st.session_state.challenge_started = True
    st.switch_page("pages/3_Challenge.py")