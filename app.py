import streamlit as st

st.set_page_config(page_title="Budget App", layout="wide", page_icon="💰")

# Custom spacing and centered layout
st.markdown("""
    <div style="text-align:center; padding-top: 6rem;">
        <h1 style="font-size:3rem; color:#1f2937;">Anti-Budget: Because Budgeting Sucks</h1>
        <p style="font-size:1.25rem; color:#4b5563; margin-top:1rem;">
            That money you burned on DoorDash last year could buy you a Volkswagon
        </p>
    </div>
""", unsafe_allow_html=True)
st.markdown("""
<style>
button[kind="primary"] {
    font-size: 1.6rem !important;
    font-weight: 600 !important;
    padding: 1rem 2rem !important;
    max-width: 240px !important;
    margin: auto !important;
    display: block !important;
}
</style>
""", unsafe_allow_html=True)
# Centered primary button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    
    if st.button("🚀 Get Started", type="primary", use_container_width=True):
        st.switch_page("pages/3_Challenge.py")
    st.markdown("</div>", unsafe_allow_html=True)
