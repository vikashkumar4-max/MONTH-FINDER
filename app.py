import streamlit as st
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import math

# 1. Page Config
st.set_page_config(
    page_title="PAPA CALENDAR",
    page_icon="👨🏻‍🦰",
    layout="centered"
)

# 2. Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* Hide Top Header Toolbar, Edit button, and Footer */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    #MainMenu {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
    }

    /* Overall Title & Subtitle Styling */
    h1 {
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        color: #1E293B !important;
    }
    
    h2, h3 {
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
    }

    label {
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        color: #334155 !important;
    }

    /* Custom Metric Cards */
    .metric-container {
        display: flex;
        gap: 10px;
        margin-top: 10px;
        margin-bottom: 18px;
        flex-wrap: wrap;
    }
    
    .metric-card {
        flex: 1;
        min-width: 130px;
        padding: 10px 12px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
    }

    /* Card Themes */
    .card-till-then { background-color: #EFF6FF; border: 1px solid #BFDBFE; }
    .card-till-then .metric-title { color: #1E40AF; }
    .card-till-then .metric-val { color: #1D4ED8; }

    .card-total-days { background-color: #FEF3C7; border: 1px solid #FDE68A; }
    .card-total-days .metric-title { color: #92400E; }
    .card-total-days .metric-val { color: #B45309; }

    .card-topup-month { background-color: #F0FDF4; border: 1px solid #BBF7D0; }
    .card-topup-month .metric-title { color: #166534; }
    .card-topup-month .metric-val { color: #15803D; }

    .card-rounded-month { background-color: #F5F3FF; border: 1px solid #DDD6FE; }
    .card-rounded-month .metric-title { color: #5B21B6; }
    .card-rounded-month .metric-val { color: #6D28D9; }

    .metric-title {
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 2px;
    }

    .metric-val {
        font-size: 1.05rem;
        font-weight: 700;
    }

    /* Unique Animated Error Popup Style */
    .popup-box {
        background: linear-gradient(135deg, #FFF5F5 0%, #FED7D7 100%);
        border: 2px dashed #E53E3E;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 8px 20px rgba(229, 62, 62, 0.2);
        animation: pulse 1.5s infinite alternate;
    }

    .popup-header {
        font-size: 1.4rem;
        font-weight: 800;
        color: #C53030;
        margin-bottom: 8px;
    }

    .popup-sub {
        font-size: 0.9rem;
        font-weight: 600;
        color: #742A2A;
    }

    .guru-line {
        text-align: center;
        font-size: 1rem;
        font-weight: 700;
        color: #4F46E5;
        margin-top: 25px;
        padding: 8px;
        border-radius: 8px;
        background: #EEF2FF;
        border: 1px dashed #C7D2FE;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Popup Function using Native Streamlit Dialog
@st.dialog("🚨 Warning!")
def show_error_popup():
    st.markdown("""
        <div class="popup-round">
            <div class="popup-header">🦁 वाह मेरे शेर! कर दिया गलत टॉपअप! 👏🤡</div>
            <div class="popup-sub">"अबे DATE सही डालो भाई!" 💸😱</div>
        </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Sorry 🙏🏻 (बेइज़्ज़ती करवा ली।)", use_container_width=True):
        st.rerun()

# Main Title
st.title("💰 Topup Calendar")

# Input Field
user_date_str = st.text_input(
    "📌 Plan Expire At:", 
    value="16-07-2027", 
    help="You can paste any format e.g. 16-07-2027, 2027/07/16, 16 Jul 2027"
)

supported_formats = [
    "%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d", "%Y/%m/%d",
    "%d-%b-%Y", "%d %b %Y", "%d-%B-%Y", "%d %B %Y",
    "%d.%m.%Y", "%Y.%m.%d"
]

input_date = None
clean_str = user_date_str.strip()

if clean_str:
    for fmt in supported_formats:
        try:
            input_date = datetime.strptime(clean_str, fmt).date()
            break
        except ValueError:
            pass

today = date.today()
two_years_later = today + relativedelta(years=2)

# If Date Input Is Invalid Trigger Popup & Banner
if input_date is None:
    # Trigger Modal Dialog Popup automatically!
    show_error_popup()
    
    # Inline subtle warning in case popup is closed
    st.error("🚨 Please paste carefully it's was wrong ")

else:
    # Calculations
    total_days_diff = (two_years_later - input_date).days
    
    if input_date <= two_years_later:
        diff = relativedelta(two_years_later, input_date)
        months_remaining = diff.years * 12 + diff.months
        days_remaining = diff.days
        display_month_str = f"{months_remaining}M {days_remaining}D"
        
        final_rounded_months = months_remaining + 1 if days_remaining > 0 else months_remaining
        rounded_month_str = f"{final_rounded_months} Months"
    else:
        diff = relativedelta(input_date, two_years_later)
        months_over = diff.years * 12 + diff.months
        days_over = diff.days
        display_month_str = f"-({months_over}M {days_over}D)"
        rounded_month_str = "N/A"

    st.write("---")
    st.subheader("✋🏻🤚🏻 Result")

    # Metric Cards Box
    st.markdown(f"""
    <div class="metric-container">
        <div class="metric-card card-till-then">
            <div class="metric-title">Till Then</div>
            <div class="metric-val">{two_years_later.strftime('%d-%b-%Y')}</div>
        </div>
        <div class="metric-card card-total-days">
            <div class="metric-title">Total Days</div>
            <div class="metric-val">{total_days_diff} Days</div>
        </div>
        <div class="metric-card card-topup-month">
            <div class="metric-title">Exact Topup</div>
            <div class="metric-val">{display_month_str}</div>
        </div>
        <div class="metric-card card-rounded-month">
            <div class="metric-title">Full Topup</div>
            <div class="metric-val">{rounded_month_str}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Details Box
    if total_days_diff >= 0:
        st.success(f"""
        🫵🏻 **Result Details:**
        * **Selected Date:** `{input_date.strftime('%d-%b-%Y')}`
        * **Given date (2 Years):** `{two_years_later.strftime('%d-%b-%Y')}`
        * **Exact Time Remaining:** **{months_remaining} Months & {days_remaining} Days** (Total: **{total_days_diff} Days**)
        * **Required Topup (Rounded):** **{final_rounded_months} Full Months** *(Extra {days_remaining} days added as +1 month)*
        """)
        
        if st.button("❄️ Celebrate Calculation"):
            st.snow()
    else:
        st.warning(f"⚠️ Selected date is **{abs(total_days_diff)} days** beyond target date!")

    st.markdown('<div class="guru-line">🔥 "ये बढ़िया था गुरु!" 😎</div>', unsafe_allow_html=True)
