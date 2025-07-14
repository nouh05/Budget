import streamlit as st
st.title("Enter Your Details Below")
st.sidebar.markdown("""
### How It Works
1. Enter your spending
2. Get personalized advice
3. Optimize your finances
""")
# here will be the fields for the user inputs
# For name input
name = st.text_input("Full Name", placeholder="e.g. John Smith").strip()

# age
age = st.number_input(
    "Age", 
    help="Enter your current age", 
    min_value=18, 
    max_value=100, 
    value=None,  # No default value
    step=1,
    placeholder="e.g. 25"
)

# monthly income
income = st.number_input("Monthly Income (post taxes)", value=None, placeholder="e.g. 4000", step=100.0)
# needs spending
needs = st.number_input("Monthly Essential Expenses (rent, groceries, loans)", value=None, step=10.0)
# wants spending
wants = st.number_input("Monthly Non-Essential Expenses (dining, subscriptions, entertainment)", value=None, step=10.0)
# saving strategy
strategy = st.selectbox("Choose your investing strategy:", ["select", "moderate", "aggressive"])
st.caption("Moderate: 20% invested | Aggressive: 30% invested")
# target retirement age
target_age = st.number_input(
    "Choose your target retirement age",
    value=None,  # No default value
    placeholder="Enter age (e.g. 65)",
    step=1,
    help="Must be greater than your current age"
)

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
if st.button("Analyze Budget", type="primary"):
    #check name validation
    if not name.replace(" ", "").isalpha():
        st.warning("Please enter a valid name (letters only)")
    elif len(name.split()) < 2:
        st.warning("Please enter both first and last name")
    # create user field with correct types
    user = {
        "name": name,
        "age": int(age),
        "monthly_income": float(income),
        "strategy": strategy,
        "needs": float(needs),
        "wants": float(wants)
    }
    #make sure of the two strategies was selected
    if strategy == "select":
        st.warning("Please choose a strategy to continue.")

    st.session_state.target_age = target_age
    st.session_state.user = user
    st.session_state.inputs_ready = inputs_ready
    if age is None:
        st.error("Please enter your age")
    st.switch_page("pages/2_Analysis.py")
