import streamlit as st
from Logic.budget import calculate_return

if not st.session_state.get("challenge_started", False):
    st.warning("⛔ Access denied. Start from the challenge page.")
    st.stop()

try:
    age = int(st.session_state.age)
    amount = float(st.session_state.amount)
    habit = st.session_state.habit

    if not habit:
        st.warning("Please pick a habit.")
        st.stop()
    elif age < 16 or age > 100:
        st.warning("Come back when you’re old enough to waste *your own* money.")
        st.stop()
    elif amount <= 0:
        st.warning("Nice try... want me to guess how much you're spending?")
        st.stop()
    else:
        st.session_state.calculated = True
        st.session_state.valid_age = age
        st.session_state.valid_amount = amount
        st.session_state.valid_habit = habit
except ValueError:
    st.warning("Please enter valid numbers for age and amount.")
    st.stop()

# --- Show Result ---
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

# Reset Button
if st.button("🔁 Go to Dashboard"):
    for key in ["age", "amount", "habit", "challenge_started", "calculated", "valid_age", "valid_amount", "valid_habit"]:
        st.session_state.pop(key, None)
    st.switch_page("pages/5_Dashboard.py")
