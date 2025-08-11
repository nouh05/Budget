import streamlit as st

# Initialize session state for additional habits
if 'additional_habits' not in st.session_state:
    st.session_state.additional_habits = []

st.markdown(f"""
<div style="text-align:center;">
    <h1 style="color:#155e59;">Now Add 1-2 More Guilty Spends</h1>
    <p style="color:#6B7280; margin-bottom:2rem;">
        We'll track them all in your dashboard
    </p>
</div>
""", unsafe_allow_html=True)

# Create form
with st.form("habit_form"):
    # Habit 1
    col1, col2 = st.columns([3, 2])
    with col1:
        habit1 = st.selectbox(
            "First Additional Habit",
            ["Select one...", "Coffee Shops", "Rideshares", "Streaming Subscriptions", 
             "Alcohol/Bars", "Fast Food", "Other"],
            key="habit1_select"
        )
        if habit1 == "Other":
            habit1 = st.text_input("Specify first habit", key="habit1_text")
    
    with col2:
        amount1 = st.number_input(
            "Monthly Amount",
            min_value=0.0,
            step=10.0,
            value=0.0,
            format="%.2f",
            key="amount1_input"
        )

    # Divider
    st.markdown("<hr style='margin:1rem 0; border-top:1px solid #e6f7f3;'/>", unsafe_allow_html=True)

    # Habit 2 (optional)
    col3, col4 = st.columns([3, 2])
    with col3:
        habit2 = st.selectbox(
            "Second Habit (optional)",
            ["Select one...", "Online Shopping", "Gaming", "Cigarettes/Vapes", 
             "Convenience Stores", "Hobby Spending", "Other"],
            key="habit2_select"
        )
        if habit2 == "Other":
            habit2 = st.text_input("Specify second habit", key="habit2_text")
    
    with col4:
        amount2 = st.number_input(
            "Monthly Amount",
            min_value=0.0,
            step=10.0,
            value=0.0,
            format="%.2f",
            key="amount2_input"
        )

    # Submit button
    submitted = st.form_submit_button("Continue to Dashboard", type="primary")
    
    if submitted:
        new_habits = []
        
        if habit1 != "Select one..." and amount1 > 0:
            habit_name = habit1 if habit1 != "Other" else st.session_state.habit1_text
            new_habits.append({
                "name": habit_name,
                "amount": amount1
            })
        
        if habit2 != "Select one..." and amount2 > 0:
            habit_name = habit2 if habit2 != "Other" else st.session_state.habit2_text
            new_habits.append({
                "name": habit_name,
                "amount": amount2
            })
        
        if new_habits:
            st.session_state.additional_habits = new_habits
            st.switch_page("pages/6_Dashboard.py")
        else:
            st.warning("Please add at least one habit to continue")

# Visual example
st.markdown("""
<div style="background-color:#e6f7f3; border-radius:12px; padding:1rem; margin-top:2rem;">
    <p style="color:#155e59; font-weight:600;">Example:</p>
    <p style="color:#374151;">"I added <span style="color:#155e59; font-weight:600;">$80/month on coffee</span> and 
    <span style="color:#155e59; font-weight:600;">$120/month on impulse Amazon purchases</span>"</p>
</div>
""", unsafe_allow_html=True)