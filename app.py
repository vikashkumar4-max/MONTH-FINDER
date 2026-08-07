import streamlit as st
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

# 1. Page Config
st.set_page_config(
    page_title="PAPA CALANDER",
    page_icon="👨🏻‍🦰",
    layout="centered"
)

# 2. Custom CSS for Font Style, Small Text Sizes & Custom Card Colors
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* Overall Title & Subtitle Styling */
    h1 {
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        color: #1E293B !important;
    }
    
    /* Result Section Title */
    h2, h3 {
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
    }

    /* Input Label styling */
    label {
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        color: #334155 !important;
    }

    /* Custom Metric Cards with distinct colors & smaller text */
    .metric-container {
        display: flex;
        gap: 10px;
        margin-top: 10px;
        margin-bottom: 18px;
    }
    
    .metric-card {
        flex: 1;
        padding: 10px 12px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
    }

    /* Color 1: Till Than (Blue Theme) */
    .card-till-then {
        background-color: #EFF6FF;
        border: 1px solid #BFDBFE;
    }
    .card-till-then .metric-title { color: #1E40AF; }
    .card-till-then .metric-val { color: #1D4ED8; }

    /* Color 2: Total Days (Orange/Amber Theme) */
    .card-total-days {
        background-color: #FEF3C7;
        border: 1px solid #FDE68A;
    }
    .card-total-days .metric-title { color: #92400E; }
    .card-total-days .metric-val { color: #B45309; }

    /* Color 3: Topup Month (Green Theme) */
    .card-topup-month {
        background-color: #F0FDF4;
        border: 1px solid #BBF7D0;
    }
    .card-topup-month .metric-title { color: #166534; }
    .card-topup-month .metric-val { color: #15803D; }

    .metric-title {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 2px;
    }

    .metric-val {
        font-size: 1.1rem;
        font-weight: 700;
    }

    /* Result Details Box - Smaller Font */
    .stAlert {
        font-size: 0.85rem !important;
        padding: 10px 14px !important;
    }

    /* Hindi Fun Line Footer */
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

# Main Title
st.title("💰Topup Calander ")

# 1. Flexible Input: Any Date Format
user_date_str = st.text_input(
    "📌 Plan Expire At:", 
    value="16-07-2027", 
    help="You can paste any format e.g. 16-07-2027, 2027/07/16, 16 Jul 2027"
)

# Supported Date Formats for Auto-detection
supported_formats = [
    "%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d", "%Y/%m/%d",
    "%d-%b-%Y", "%d %b %Y", "%d-%B-%Y", "%d %B %Y",
    "%d.%m.%Y", "%Y.%m.%d"
]

input_date = please paste date here 

# Parse input string to standard date object
if user_date_str.strip():
    for fmt in supported_formats:
        try:
            input_date = datetime.strptime(user_date_str.strip(), fmt).date()
            break
        except ValueError:
            pass

today = date.today()
two_years_later = today + relativedelta(years=2)

if input_date:
    total_days_diff = (two_years_later - input_date).days
    diff = relativedelta(two_years_later, input_date)
    months_remaining = diff.years * 12 + diff.months
    days_remaining = diff.days

    st.write("---")
    
    # 2. Header: Result
    st.subheader("✋🏻🤚🏻 Result")

    # 3. Custom Colored Cards (Till Than, Total Days, Topup Month)
    st.markdown(f"""
    <div class="metric-container">
        <div class="metric-card card-till-then">
            <div class="metric-title">Till Than</div>
            <div class="metric-val">{two_years_later.strftime('%d-%b-%Y')}</div>
        </div>
        <div class="metric-card card-total-days">
            <div class="metric-title">Total Days</div>
            <div class="metric-val">{total_days_diff} Days</div>
        </div>
        <div class="metric-card card-topup-month">
            <div class="metric-title">Topup Month</div>
            <div class="metric-val">{months_remaining}M {days_remaining}D</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 4. Result Details Box
    if total_days_diff >= 0:
        st.success(f"""
        🫵🏻 **Result Details:**
        * **Selected Date:** `{input_date.strftime('%d-%b-%Y')}`
        * **Given date (2 Years):** `{two_years_later.strftime('%d-%b-%Y')}`
        * **Exact Time Remaining:** **{months_remaining} Months & {days_remaining} Days** (Total: **{total_days_diff} Days**)
        """)
        
        # Celebration Button
        if st.button("❄️ Celebrate Calculation"):
            st.snow()
    else:
        st.warning(f"⚠️ Selected date is **{abs(total_days_diff)} days** beyond target date!")

    # 5. Bottom Hindi Tagline
    st.markdown('<div class="guru-line">🔥 "ये बढ़िया था गुरु!" 😎</div>', unsafe_allow_html=True)
else:
  st.markdown("""
    <div /* Top Header Toolbar, Edit button, and Footer ko hide karne ke liye */
header[data-testid="stHeader"] {
    display: none !important;
}
#MainMenu {
    visibility: hidden;
}
footer {
    visibility: hidden;
}="
        text-align: center;
        font-size: 0.95rem;
        font-weight: 700;
        color: #DC2626;
        margin-top: 25px;
        padding: 10px;
        border-radius: 8px;
        background: #FEF2F2;
        border: 1.5px dashed #FCA5A5;
    ">
        🚨 "अबे DATE सही डालो! अगर टॉप-अप गलत हुआ तो . देवेंद्र ले लेगा तुम्हारी!!" 😱💸
    </div>
""", unsafe_allow_html=True)
