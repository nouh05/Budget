import streamlit as st
import time
#get variables from session state
result = st.session_state.spending_style
name = st.session_state.user_name
# Personality reveal
st.title(f"Hey {name}, you're a...")
st.markdown(f"# {result['output']}")
st.progress(int(result['invest_pct']*100), text=f"Saving Power: {int(result['invest_pct']*100)}%")

# Recommendation
st.subheader("💰 Recommended Money Split")
st.write(f"""
- Needs: {result['needs_pct']*100}%
- Wants: {result['wants_pct']*100}%
- Saving/Investing: {result['invest_pct']*100}%
""")

if st.button("🚀 Start My 1% Challenge", type="primary"):
    st.switch_page("pages/3_Challenge.py")
with st.spinner("Moving on..."):
    time.sleep(1.5)