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
# age = st.session_state.valid_age
# amount = st.session_state.valid_amount
# habit = st.session_state.valid_habit

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

# Financial Future Calculations
one_year = calculate_return(amount, age, age+1, 0.08)
five_year = calculate_return(amount, age, age+5, 0.08)
ten_year = calculate_return(amount, age, age+10, 0.08)
sixty_five = calculate_return(amount, age, 65, 0.08)

# Format values before injecting into HTML
one_year_str = f"${one_year:,.0f}"
five_year_str = f"${five_year:,.0f}"
ten_year_str = f"${ten_year:,.0f}"
sixty_five_str = f"${sixty_five:,.0f}"

# Show Results Grid
st.markdown("""
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        margin-top: 2rem;
    }
    .card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    .amount {
        font-size: 1.75rem;
        font-weight: bold;
        color: #10B981;
    }
    .label {
        margin-top: 0.5rem;
        font-size: 1rem;
        color: #6B7280;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="grid-container">
    <div class="card">
        <div class="amount">{one_year_str}</div>
        <div class="label">In 1 Year</div>
    </div>
    <div class="card">
        <div class="amount">{five_year_str}</div>
        <div class="label">In 5 Years</div>
    </div>
    <div class="card">
        <div class="amount">{ten_year_str}</div>
        <div class="label">In 10 Years</div>
    </div>
    <div class="card">
        <div class="amount">{sixty_five_str}</div>
        <div class="label">By Age 65</div>
    </div>
</div>
""", unsafe_allow_html=True)

if st.toggle("📊 Show calculation details"):
    st.markdown(f"""
    - Monthly investment: **${amount}**
    - Years invested: **{65 - age}**
    - Annual return: **8%**
    - Formula: `FV = PMT × (((1 + r)ⁿ - 1) / r)`
    """)
st.session_state.valid_age = age
st.session_state.valid_amount = amount
st.session_state.valid_habit = habit
# Reset Button
if st.button("🔁 Let's Get Saving"):
    st.session_state.summary = True
    
    st.switch_page("pages/5_Summary.py")
