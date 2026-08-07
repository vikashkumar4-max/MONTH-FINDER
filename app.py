import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Page Configuration
st.set_page_config(page_title="PAPA Calander", page_icon="👨🏻‍🦰", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1E88E5;
        font-weight: bold;
    }
    .topup-box {
        background-color: #E3F2FD;
        border-left: 6px solid #1E88E5;
        padding: 18px;
        border-radius: 8px;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    .topup-text {
        font-size: 22px;
        font-weight: bold;
        color: #0D47A1;
        margin: 0;
    }
    .topup-subtext {
        font-size: 13px;
        color: #555;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 🔒 FEATURE 1: APP PROTECTION (PASSWORD)
# ==========================================
APP_PASSWORD = "admin"  # Set your desired password here

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def check_password():
    if st.session_state.password_input == APP_PASSWORD:
        st.session_state.authenticated = True
        del st.session_state.password_input
    else:
        st.session_state.authenticated = False
        st.error("Incorrect password! Please try again.")

if not st.session_state.authenticated:
    st.markdown("<h2 class='main-title'>🔒 Application Locked</h2>", unsafe_allow_html=True)
    st.text_input("Enter password to access the app:", type="password", key="password_input", on_change=check_password)
    st.info("Default password: admin")
    st.stop()

# Sidebar Lock Button
st.sidebar.button("🔒 Lock App", on_click=lambda: st.session_state.update({"authenticated": False}))

# ==========================================
# 📅 MAIN APP CONTENT
# ==========================================
st.markdown("<h1 class='main-title'>📅 Month Finder & Top-Up Calculator</h1>", unsafe_allow_html=True)
st.write("Select the Start Date and End Date below:")

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", value=datetime.today())
with col2:
    end_date = st.date_input("End Date", value=datetime.today())

if st.button("Calculate Duration"):
    if end_date < start_date:
        st.error("End Date must be after Start Date!")
    else:
        # Calculate exact duration
        delta = relativedelta(end_date, start_date)
        
        years = delta.years
        months = delta.months
        days = delta.days
        
        total_actual_months = (years * 12) + months

        # ------------------------------------------
        # Standard Result Display
        # ------------------------------------------
        st.success(f"Exact Duration: {years} Years, {months} Months, {days} Days")
        
        # ==========================================
        # 💡 FEATURE 2: TOP-UP MONTH LOGIC
        # ==========================================
        # If even 1 day is extra (days > 0), add 1 extra month
        if days > 0:
            topup_months = total_actual_months + 1
        else:
            topup_months = total_actual_months

        # Separate Box Display (Only Months shown, no Days)
        st.markdown(f"""
            <div class="topup-box">
                <p class="topup-text">Top-Up Calculated Duration: {topup_months} Months</p>
                <p class="topup-subtext">(Note: Any extra days have been rounded up to +1 full month)</p>
            </div>
        """, unsafe_allow_html=True)
