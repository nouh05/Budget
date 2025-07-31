import streamlit as st
from datetime import date, timedelta

# --- Init session state ---
# --- Initialize session state safely ---
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "last_check" not in st.session_state:
    st.session_state.last_check = None
if "total_saved" not in st.session_state:
    st.session_state.total_saved = 0.0

# --- Fallback values ---
habit = st.session_state.get("habit", "your habit")
monthly_spend = float(st.session_state.get("valid_amount", 100.0))

# --- Core Metrics ---
daily_1pct = max((monthly_spend / 30) * 0.01, 0.01)
#weekly_goal = max(daily_1pct * 7, 0.01)
weekly_goal = monthly_spend / 2

# --- Header ---
st.markdown(f"""
<h1 style='text-align: center; font-size: 2.5rem; margin-bottom: 0.5rem;'>
    🔥 Your {habit} Progress
</h1>
""", unsafe_allow_html=True)

st.markdown(f"""
<p style='text-align: center; font-size: 1.1rem; color: #4B5563;'>
    Saving <b>${daily_1pct:.2f}</b> daily → <b>${weekly_goal:.2f}</b> weekly
</p>
""", unsafe_allow_html=True)

# --- Custom Amount Input + Logging ---
st.markdown("---")
st.markdown("### 💾 Log a Saving")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    custom_amount = st.number_input("How much did you save today?", min_value=0.01, step=0.01, label_visibility="collapsed")
    st.markdown("""
        <style>
        .stButton>button {
            font-size: 1.1rem;
            padding: 0.6rem 1.5rem;
            border-radius: 0.6rem;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

    if st.button("✅ Log This Savings", type="primary"):
        today = date.today()
        if st.session_state.last_check != today:
            st.session_state.total_saved += custom_amount
            st.session_state.streak = (
                st.session_state.streak + 1 if st.session_state.last_check == today - timedelta(days=1) else 1
            )
            st.session_state.last_check = today
            st.rerun()

# --- Metrics ---
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Current Streak", f"{st.session_state.streak} days")
with col2:
    st.metric("Weekly Saved", 
              f"${st.session_state.total_saved:.2f}", 
              f"${weekly_goal:.2f} goal")
with col3:
    #st.metric("Projected Yearly", f"${daily_1pct * 365:.2f}")
    st.metric("Projected Yearly", f"${custom_amount * 365:.2f}")


# --- Progress Bar ---
progress = min(st.session_state.total_saved / weekly_goal, 1.0)
st.progress(progress, text=f"{int(progress*100)}% to weekly goal")

# --- Celebration ---
if st.session_state.streak > 0 and st.session_state.streak % 7 == 0:
    st.balloons()
    st.success(f"🎉 {st.session_state.streak}-day streak! Total saved: ${st.session_state.total_saved:.2f}")
