import streamlit as st

# Ensure necessary session state is present
if not st.session_state.get("summary", False):
    st.warning("⛔ Access denied. Start from the challenge page.")
    st.stop()

# Safely retrieve state variables with defaults
amount = st.session_state.get("valid_amount", 100.0)
habit = st.session_state.get("valid_habit", "your habit")

# Optional: Warn user if defaults are being used
if "valid_amount" not in st.session_state or "valid_habit" not in st.session_state:
    st.warning("Using default values. Go back to personalize your summary.")

# Calculate initial captured savings (assuming 1 day saved from monthly spend)
daily_savings = amount / 30  # Roughly 1 day
captured_percent = (daily_savings / amount) * 100

# Display Affirmation
st.markdown(f"""
<div style="font-size:1.5rem; font-weight:700; color:#155e59; text-align:center; margin-bottom:2rem;">
    You’re taking control.
</div>
<div style="font-size:2rem; font-weight:900; color:#10B981; text-align:center; margin-bottom:1rem;">
    ${daily_savings:,.2f}
</div>
<div style="font-size:1.25rem; color:#374151; text-align:center; margin-bottom:2rem;">
    That’s {captured_percent:.0f}% of your monthly {habit} spend.
</div>
<div style="font-size:1.1rem; color:#6B7280; text-align:center; margin-bottom:3rem;">
    Every day you stay on track, you’re clawing that money back.
</div>
""", unsafe_allow_html=True)

# CTA Button to Dashboard
if st.button("📊 Go to Dashboard"):
    st.switch_page("pages/6_Dashboard.py")
