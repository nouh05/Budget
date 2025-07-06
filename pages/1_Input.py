import streamlit as st
st.title("Enter Your Details Below")
# here will be the fields for the user inputs
# For name input
name = st.text_input("Full Name", placeholder="e.g. John Smith").strip()
if not name.replace(" ", "").isalpha():
    st.warning("Please enter a valid name (letters only)")
elif len(name.split()) < 2:
    st.warning("Please enter both first and last name")
# age
age = st.number_input("Age", help="Enter your current age", min_value=0.0, max_value=100.0, placeholder=30, step=1.0)
# monthly income
income = st.number_input("Monthly Income (post taxes)", min_value=0.0, step=100.0)
# needs spending
needs = st.number_input("Monthly Essential Expenses (rent, groceries, loans)", min_value=0.0, step=10.0)
# wants spending
wants = st.number_input("Monthly Non-Essential Expenses (dining, subscriptions, entertainment)", min_value=0.0, step=10.0)
# saving strategy
strategy = st.selectbox("Choose your investing strategy:", ["select", "moderate", "aggressive"])
st.caption("Moderate: 20% invested | Aggressive: 30% invested")
# target retirement age
target = st.number_input("Choose your target retirement age", min_value=age+1.0, step=1.0)
target_age = int(target)

# validate submission
inputs_ready = (
    name.strip() and
    age >= 18 and
    income > 0 and
    needs >= 0 and
    wants >= 0 and
    strategy in ["moderate", "aggressive"] and
    target_age > age
)
# create user field with correct types
user = {
    "name": name,
    "age": int(age),
    "monthly_income": float(income),
    "strategy": strategy,
    "needs": float(needs),
    "wants": float(wants)
}
if strategy == "select":
    st.warning("Please choose a strategy to continue.")

st.session_state.target_age = target_age
st.session_state.user = user
st.session_state.inputs_ready = inputs_ready
if st.button("Get Started", type="primary"):
    st.switch_page("pages/2_Analysis.py")
