import streamlit as st
from Logic.budget import validate_user, get_budget_percentage, calculate_budget, calculate_return, compare_spending_rec
import plotly.graph_objs as go
import random
import time
# Initialize session state variables
if "challenge_started" not in st.session_state:
    st.session_state.challenge_started = False
if "example_loaded" not in st.session_state:
    st.session_state.example_loaded = False
if "age" not in st.session_state:
    st.session_state.age = None
if "amount" not in st.session_state:
    st.session_state.amount = None
if "habit" not in st.session_state:
    st.session_state.habit = ""
if "preset_used" not in st.session_state:  
    st.session_state.preset_used = False

st.title("🚨 The 1% Guilt Trip")  
st.markdown("*Spend 1% less on your **stupidest habit**. Get 100% richer.*")  
# lazy user example
# Preset button
# if st.button("Try Starbucks Example", help="Prefill $120/month at age 25"):
#     st.session_state.preset_used = True
#     st.session_state.age = 25
#     st.session_state.amount = 120
#     st.session_state.habit = "Starbucks"
    
#age
age = st.number_input("How old are you?", value=st.session_state.age if st.session_state.preset_used else None)
#habit
# Make it visual  
habit = st.selectbox(  
    "What’s your **guiltiest** spend?",  
    ["DoorDash", "Boba Tea", "Uber", "Sephora Hauls", "Vapes", "Monster"],  
    index=None,  
    placeholder="Pick your poison..."  
)  

#amount per month
amount = st.number_input("How much moola do you set on fire here monthly?", value=st.session_state.amount if st.session_state.preset_used else None, placeholder="Don't worry twin, I probably spent more")
# Update session state with current inputs
st.session_state.age = age
st.session_state.habit = habit if habit else None
st.session_state.amount = amount
# Visual indicator when preset is active
# if st.session_state.preset_used:
#     st.markdown("---")
#     st.markdown("ℹ️ Using **Starbucks example**: $120/month at age 25")
#     st.markdown("*(Edit any field above to customize)*")
#     st.markdown("---")

if st.button("You're gonna want to see this...", type='primary'):
    if not habit or amount is None or age is None:
        st.warning("Please fill in all fields!")
    elif age < 16:
        st.warning("Age must be at least 16")
    elif amount <= 0:
        st.warning("Amount must be greater than 0")
    else:
        st.session_state.challenge_started = True
        with st.spinner("Calculating your potential..."):
            time.sleep(1.5)
        st.switch_page("pages/4_Result.py")
# Move everythin below here
# if st.session_state.challenge_started:
#     if st.session_state.preset_used:
#         habit = st.session_state.habit
#         age = st.session_state.age
#         amount = st.session_state.amount
#     monthly_investment = amount * 0.01
#     returns = calculate_return(monthly_investment, age, 65, 0.08)

#     #graph showing monthly returns
#     years = list(range(int(age), 66))  # From current age to 65
#     future_vals = []
        
#     for y in years:
#         if y <= age:
#             future_vals.append(0)
#         else:
#             future_vals.append(calculate_return(monthly_investment, age, y, 0.08))
#     #user statement on saving
#     st.markdown(f"### If you invested just 1% of your monthly **{habit}** habit...")
#     # First format the numbers properly
#     monthly_str = f"${monthly_investment:,.2f}"  # $12.50
#     returns_str = f"${returns:,.0f}"             # $3,450

#     # Then print it cleanly with normal formatting
#     st.markdown(
#         f"<p style='font-size:30px;'>That's <b>{monthly_str}</b> a month, turned into <b>{returns_str}</b> by age 65!</p>",
#         unsafe_allow_html=True
#     )
#     st.markdown("### 🧠 Imagine what happens if you invested a little more:")
#     #SLIDER
#     # For the slider with larger text
#     st.markdown("""
#         <p style="font-size:18px; margin-bottom:0.5rem;">
#         Try investing a bigger % instead:
#         </p>
#         """, unsafe_allow_html=True)
#     more_pct = st.slider("", 1, 50, step=1, label_visibility="collapsed")
#     more_investment = amount * (more_pct / 100)
#     more_returns = calculate_return(more_investment, age, 65, 0.08)
#     st.markdown(
#         f"<p style='font-size:16px;'>That's <b>${more_investment:.2f}/mo</b> → 💥 about <b>${more_returns:,.0f}</b> by age 65.</p>",
#         unsafe_allow_html=True
#     )
    

