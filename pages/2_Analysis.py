import streamlit as st
import plotly.graph_objects as go
from Logic.budget import validate_user, get_budget_percentage, calculate_budget, calculate_return, compare_spending_rec
#core logic below
# Format the dollar values
def format_currency(value):
    return f"${value:,.2f}"
if st.session_state.inputs_ready:
    try:
        #validate the inputted user
        validate_user(st.session_state.user)
        result = compare_spending_rec(st.session_state.user, st.session_state.target_age)
        # Display Results
        st.header(f"Budget Summary for {result['name']}")

        # easy display metrics
        col1, col2, col3 = st.columns(3)
        #display needs spending
        with col1:
            delta_needs = result['actual']['needs'] - result['recommended']['needs']
            st.markdown(
                f"""
                <div style="font-size: 1rem; margin-bottom: -1.5rem;">
                Your spending on essentials: <span style="font-size: 1.3rem; font-weight: bold;">{format_currency(result['actual']['needs'])}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.metric(
                label="",  # Empty label
                value="",  # Empty value
                delta=f"{'Over budget' if delta_needs > 0 else 'Under budget'} by {format_currency(abs(delta_needs))}",
                delta_color="inverse" if delta_needs > 0 else "normal",
                help=f"Recommended: {format_currency(result['recommended']['needs'])}"
            )
        #display wants spending
        with col2:
            delta_wants = result['actual']['wants'] - result['recommended']['wants']
            st.markdown(
                f"""
                <div style="font-size: 1rem; margin-bottom: -1.5rem;">
                Your spending on wants: <span style="font-size: 1.3rem; font-weight: bold;">{format_currency(result['actual']['wants'])}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.metric(
                label="",  # Empty label
                value="",  # Empty value
                delta=f"{'Over budget' if delta_wants > 0 else 'Under budget'} by {format_currency(abs(delta_wants))}",
                delta_color="inverse" if delta_wants > 0 else "normal",
                help=f"Recommended: {format_currency(result['recommended']['wants'])}"
            )
        with col3:
             st.markdown(
                f"""
                <div style="font-size: 1rem; margin-bottom: -1.5rem;">
                Estimated earnings at retirement: <span style="font-size: 1.3rem; font-weight: bold;">{format_currency(result['expected_index_return']['expected_return'])}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
        #Section 2: Charts/graphs
        # easy display metrics
        col4, col5, col6 = st.columns(3)
        #bar graph for needs act vs rec
        with col4:
            st.markdown("#### Essentials Spending")
            fig_needs = go.Figure(data=[
                go.Bar(name='Actual', x=['Essentials'], y=[result['actual']['needs']], marker_color='blue'),
                go.Bar(name='Recommended', x=['Essentials'], y=[result['recommended']['needs']], marker_color='lightgreen')
            ])
            fig_needs.update_layout(
                barmode='group',
                height=300,
                margin=dict(l=0, r=0, t=30, b=0),
                yaxis_title="Dollars"
            )
            st.plotly_chart(fig_needs, use_container_width=True)
        with col5:
            st.markdown("#### Non-Essentials Spending")
            fig_wants = go.Figure(data=[
                go.Bar(name='Actual', x=['Non-Essentials'], y=[result['actual']['wants']], marker_color='blue'),
                go.Bar(name='Recommended', x=['Non-Essentials'], y=[result['recommended']['wants']], marker_color='lightgreen')
            ])
            fig_wants.update_layout(
                barmode='group',
                height=300,
                margin=dict(l=0, r=0, t=30, b=0),
                yaxis_title="Dollars"
            )
            st.plotly_chart(fig_wants, use_container_width=True)
        with st.expander("📊 Full Details & Recommendations"):
            st.markdown("### Recommended Budget Split")
            # pie chart
            fig_pie = go.Figure(data=[
                go.Pie(labels=["Needs", "Wants", "Investments"],
                    values=[result['recommended']['needs'], result['recommended']['wants'], result['expected_index_return']['monthly_investment']],
                    hole=0.4)
            ])
            fig_pie.update_layout(height=400, showlegend=True)
            st.plotly_chart(fig_pie, use_container_width=True)
    except Exception as e:
            st.error(f"Error: {e}")
else:
    st.caption("Fill in all fields above to run your analysis.")
# if st.button("Home"):
#      st.switch_page("app.py")
# elif st.button("Input"):
#      st.switch_page("pages/Input.py")


