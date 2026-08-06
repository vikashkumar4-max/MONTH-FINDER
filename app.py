import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

# 1. Page Configuration
st.set_page_config(
    page_title="Date & Month Calculator Pro",
    page_icon="📅",
    layout="centered"
)

# 1. Page Configuration
st.set_page_config(
    page_title="Date & Month Calculator Pro",
    page_icon="📅",
    layout="centered"
)

# 2. Custom CSS for UI styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# App Title & Header
st.title("⚡VIKAS MONTH FINDER ⚡")
st.caption("Calculate accurate time differences in days, months, and years.")

# 3. Sidebar Inputs
st.sidebar.header("⚙️ Configuration")
today = date.today()
two_years_later = today + relativedelta(years=2)

st.sidebar.info(f"**Today:** {today.strftime('%d-%b-%Y')}\n\n**Base (2 Yrs):** {two_years_later.strftime('%d-%b-%Y')}")

# Input Date Selection
input_date = st.date_input(
    "📌 Select Target Date:",
    value=date(2027, 7, 16),
    help="Pick a date to compare with the 2-year target date"
)

st.divider()

# 4. Calculation Logic
if input_date:
    total_days_diff = (two_years_later - input_date).days
    diff = relativedelta(two_years_later, input_date)
    months_remaining = diff.years * 12 + diff.months
    days_remaining = diff.days

    # Metrics Display
    st.subheader("📊 Summary Metrics")
    col1, col2, col3 = st.columns(3)
    
    col1.metric(label="TILL THAN", value=two_years_later.strftime("%d-%b-%Y"))
    col2.metric(label="TOTAL DAYS", value=f"{total_days_diff} Days")
    col3.metric(label="TOPUP MONTH", value=f"{months_remaining}M {days_remaining}D")

    st.write("")
    
    # Visual Progress/Status Cards
    if total_days_diff >= 0:
        st.success(f"""
        ### 🎯 Result Details
        * **Selected Date:** `{input_date.strftime('%d-%b-%Y')}`
        * **Target Date (2 Years):** `{two_years_later.strftime('%d-%b-%Y')}`
        * **Exact Time Remaining:** **{months_remaining} Months & {days_remaining} Days** (Total: **{total_days_diff} Days**)
        """)
        
        # Celebrate button for interactive feel
        if st.button("🎉 Celebrate Calculation"):
            st.balloons()
    else:
        st.warning(f"⚠️ Selected date is **{abs(total_days_diff)} days** beyond the 2-year target date!")

st.divider()
st.caption("Designed with ❤️ using Streamlit")
