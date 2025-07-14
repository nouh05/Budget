import streamlit as st
import time
st.title("👋 Let's get to know you better")

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

#name input 
name = st.text_input("Full Name", placeholder="e.g. Jordan Smith").strip()

#Quiz here
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("🍽️ Food habits")
    q1 = st.radio("Your fridge right now:", 
                    ["Meal-prepped perfection", 
                    "Half takeout", 
                    "Has this expired already?"], 
                    index=None, key="q1")
with col2:
    st.subheader("💸 Treat yourself")
    q2 = st.radio("Ideal 'treat yourself' moment:", 
                    ["Library book", 
                    "Fancy coffee", 
                    "Shopping!"], index=None, key="q2")
with col3:
    st.subheader("💰 Payday moves")
    q3 = st.radio("Your payday ritual:", 
                    ["Transfer savings first", 
                    "Check bills", 
                    "Venmo request? What’s that?"], 
                    index=None, key="q3")

    if st.button("Reveal Spend Personality!"):
        if not name:
            st.warning("Please enter your name!")
        elif not all([q1, q2, q3]):
            st.warning("Please answer all 3 questions!")
        else:
            with st.spinner("Analyzing your spending vibes..."):
                time.sleep(1.5)
                # Scoring logic
            score = 0
            if q1 == "Has this expired already?": score += 1
            elif q1 == "Meal Prepped to Perfection": score += 2

            if q2 == "Library book": score += 2
            elif q2 == "Fancy coffee": score += 1

            if q3 == "Transfer savings first": score += 2
            elif q3 == "Check bills": score += 1

            # Determine profile
            if score >= 5:
                output = "💰 **Neon Saver** (Needs: 45%, Wants: 25%, Saving: 30%)"
                result = "Saver"
                needs_pct, wants_pct, invest_pct = 0.45, 0.25, 0.3
            elif score >= 2:
                output = "🛍️ **Balance Boss** (Needs: 50%, Wants: 30%, Saving: 20%)"
                result = "Balanced"
                needs_pct, wants_pct, invest_pct = 0.5, 0.3, 0.2
            else:
                output = "🎉 **YOLO Spender** (Needs: 55%, Wants: 35%, Saving: 10%)"
                result = "Spender"
                needs_pct, wants_pct, invest_pct = 0.55, 0.35, 0.1

            # Show result + store
            st.session_state.user_name = name
            st.session_state.spending_type = result
            st.session_state.update({
                "user_name": name,
                "spending_type": result,
                "spending_style": {
                    "type": result,
                    "needs_pct": needs_pct,
                    "wants_pct": wants_pct,
                    "invest_pct": invest_pct,
                    "output": output
                },
                "quiz_submitted": True
            })
            # Success message before redirect
            st.success("Analysis complete!")
            time.sleep(0.5)  # Let them see the success message
            st.switch_page("pages/2_Personality.py")
            
            





# elif st.button("Let's save you some money"):
#     if not name or len(name.split()) < 2 or not name.replace(" ", "").isalpha():
#         st.warning("Please enter a valid full name.")
#     elif spending_type is None:
#         st.warning("Please select a spending habit.")
#     elif spending_type != "Not sure — take a quiz":
#         if spending_type == "Saver":
#             needs_pct, wants_pct, saving_pct = 0.45, 0.25, 0.3
#         elif spending_type == "Balanced":
#             needs_pct, wants_pct, saving_pct = 0.5, 0.3, 0.2
#         else:
#             needs_pct, wants_pct, saving_pct = 0.55, 0.35, 0.1
#         # Store in session and continue
#         st.session_state.user_name = name
#         st.session_state.spending_type = spending_type.lower()
#         st.session_state.spending_style = {
#             "type": spending_type.lower(),
#             "needs_pct": needs_pct,
#             "wants_pct": wants_pct,
#             "invest_pct": saving_pct
#         }
#         st.switch_page("pages/2_BudgetPlan.py")
