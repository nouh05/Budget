import streamlit as st
from datetime import date, timedelta

# Initialize session state for all habits
if 'habits' not in st.session_state:
    st.session_state.habits = [
        {
            'name': st.session_state.get('habit', 'Primary Habit'),
            'monthly': float(st.session_state.get('valid_amount', 100)),
            'daily_goal': float(st.session_state.get('valid_amount', 100)) / 30,
            'saved': 0.0,
            'streak': 0,
            'last_logged': None
        }
    ]
    
    # Add the 2 additional habits if they exist
    if 'additional_habits' in st.session_state:
        for habit in st.session_state.additional_habits:
            st.session_state.habits.append({
                'name': habit['name'],
                'monthly': float(habit['amount']),
                'daily_goal': float(habit['amount']) / 30,
                'saved': 0.0,
                'streak': 0,
                'last_logged': None
            })

# Dashboard Header
st.markdown("""
<div style="text-align:center; margin-bottom:1.5rem;">
    <h1 style="color:#155e59; font-size:2.3rem;">Your Spending Recovery Dashboard</h1>
    <p style="color:#6B7280;">
        Track progress across all your guilty habits
    </p>
</div>
""", unsafe_allow_html=True)

# Habit Cards - One per column
cols = st.columns(len(st.session_state.habits))

for i, habit in enumerate(st.session_state.habits):
    with cols[i]:
        with st.container(border=True):
            # Habit Header
            st.markdown(f"""
            <div style="text-align:center;">
                <h3 style="color:#155e59; margin-bottom:0.5rem;">{habit['name']}</h3>
                <p style="color:#6B7280; font-size:0.9rem;">
                    ${habit['monthly']:,.2f}/mo → ${habit['daily_goal']:.2f}/day
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Streak Display
            st.markdown(f"""
            <div style="text-align:center; margin:1rem 0;">
                <span style="font-size:1.8rem; font-weight:700; color:#10B981;">
                    {habit['streak']}
                </span>
                <span style="color:#6B7280;">day streak</span>
            </div>
            """, unsafe_allow_html=True)
            
            # Log Button
            if st.button(f"✅ Log ${habit['daily_goal']:.2f}", key=f"log_{i}"):
                today = date.today()
                if habit['last_logged'] != today:
                    habit['saved'] += habit['daily_goal']
                    habit['streak'] = habit['streak'] + 1 if habit['last_logged'] == today - timedelta(days=1) else 1
                    habit['last_logged'] = today
                    st.rerun()
            
            # Total Saved
            st.markdown(f"""
            <div style="text-align:center; margin-top:1rem;">
                <p style="color:#374151; font-size:0.9rem;">Total Saved</p>
                <p style="font-size:1.2rem; font-weight:700; color:#155e59;">
                    ${habit['saved']:,.2f}
                </p>
            </div>
            """, unsafe_allow_html=True)

# Combined Progress
st.markdown("---")
total_saved = sum(h['saved'] for h in st.session_state.habits)
total_monthly = sum(h['monthly'] for h in st.session_state.habits)
progress = min(total_saved / (total_monthly * 0.1), 1.0)  # 10% of total monthly as initial goal

st.markdown(f"""
<div style="text-align:center; margin-bottom:1rem;">
    <h3 style="color:#155e59;">Overall Progress</h3>
    <p style="color:#6B7280;">
        ${total_saved:,.2f} saved of ${total_monthly * 0.1:,.2f} monthly goal
    </p>
</div>
""", unsafe_allow_html=True)

st.progress(progress, text=f"{int(progress*100)}% to monthly goal")

# Celebration Logic
if any(h['streak'] % 7 == 0 and h['streak'] > 0 for h in st.session_state.habits):
    st.balloons()
    st.success("🎉 Weekly streak achieved on at least one habit!")
