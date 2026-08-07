import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Page Configuration
st.set_page_config(page_title="MONTH FINDER", page_icon="📅", layout="centered")

# Custom CSS for the Top-up Box
st.markdown("""
    <style>
    .topup-box {
        background-color: #e6f7ff;
        border-left: 5px solid #1890ff;
        padding: 15px;
        border-radius: 5px;
        margin-top: 20px;
    }
    .topup-title {
        font-size: 20px;
        font-weight: bold;
        color: #0050b3;
        margin: 0;
        padding: 0;
    }
    .topup-desc {
        font-size: 14px;
        color: #595959;
        margin: 5px 0 0 0;
    }
    </style>
""", unsafe_allow_html=True)

# Main Dashboard
st.title("📅 MONTH FINDER")
st.write("Select Start Date and End Date:")

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start Date", value=datetime.today())

with col2:
    end_date = st.date_input("End Date", value=datetime.today())

if st.button("Calculate"):
    if end_date < start_date:
        st.error("End Date must be after Start Date!")
    else:
        # Calculate time difference
        delta = relativedelta(end_date, start_date)
        
        years = delta.years
        months = delta.months
        days = delta.days
        
        # 1. Old Output (Exact Time)
        st.success(f"**Exact Duration:** {years} Years, {months} Months, {days} Days")
        
        # 2. New Feature: Top-Up Logic
        total_months = (years * 12) + months
        if days > 0:
            topup_months = total_months + 1
        else:
            topup_months = total_months
            
        # Display Top-Up Month in a separate box
        st.markdown(f"""
            <div class="topup-box">
                <p class="topup-title">Top-Up Month: {topup_months} Months</p>
                <p class="topup-desc">(Extra days converted into 1 full month)</p>
            </div>
        """, unsafe_allow_html=True)
