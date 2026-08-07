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

# 2. Custom CSS for Font Style, Small Text Sizes & Custom Card Colors
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

    /* Custom Metric Cards */
    .metric-container {
        display: flex;
        gap: 10px;
        margin-top: 10px;
        margin-bottom: 18px;
        flex-wrap: wrap; /* ताकी मोबाइल में भी कार्ड्स अच्छे से सेट रहें */
    }
    
    .metric-card {
        flex: 1;
        min-width: 130px;
        padding: 10px 12px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
    }

    /* Color 1: Till Then (Blue Theme) */
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

    /* Color 4: Rounded Topup (Purple Theme) */
    .card-rounded-month {
        background-color: #F5F3FF;
        border: 1px solid #DDD6FE;
    }
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

    /* Result Details Box */
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

    /* Error Message Box */
    .error-line {
        text-align: center;
        font-size: 0.95rem;
        font-weight: 700;
        color: #DC2626;
        margin-top: 25px;
        padding: 10px;
        border-radius: 8px;
        background: #FEF2F2;
        border: 1.5px dashed #FCA5A5;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.title("💰 Topup Calendar")

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

input_date = None

# Parse input string to standard date object
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

# Calculation Block
if input_date is not None:
    total_days_diff = (two_years_later - input_date).days
    
    if input_date <= two_years_later:
        diff = relativedelta(two_years_later, input_date)
        months_remaining = diff.years * 12 + diff.months
        days_remaining = diff.days
        display_month_str = f"{months_remaining}M {days_remaining}D"
        
        # LOGIC: अगर 1 दिन भी एक्स्ट्रा है तो 1 महीना पूरा जोड़ दिया जाएगा
        if days_remaining > 0:
            final_rounded_months = months_remaining + 1
        else:
            final_rounded_months = months_remaining
            
        rounded_month_str = f"{final_rounded_months} Months"
    else:
        diff = relativedelta(input_date, two_years_later)
        months_over = diff.years * 12 + diff.months
        days_over = diff.days
        display_month_str = f"-({months_over}M {days_over}D)"
        rounded_month_str = "N/A"

    st.write("---")
    
    # Header: Result
    st.subheader("✋🏻🤚🏻 Result")

    # Custom Colored Cards (4 Boxes)
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

    # Result Details Box
    if total_days_diff >= 0:
        st.success(f"""
        🫵🏻 **Result Details:**
        * **Selected Date:** `{input_date.strftime('%d-%b-%Y')}`
        * **Given date (2 Years):** `{two_years_later.strftime('%d-%b-%Y')}`
        * **Exact Time Remaining:** **{months_remaining} Months & {days_remaining} Days** (Total: **{total_days_diff} Days**)
        * **Required Topup (Rounded):** **{final_rounded_months} Full Months** *(Since extra {days_remaining} days required +1 month)*
        """)
        
        # Celebration Button
        if st.button("❄️ Celebrate Calculation"):
            st.snow()
    else:
        st.warning(f"⚠️ Selected date is **{abs(total_days_diff)} days** beyond target date!")

    # Bottom Hindi Tagline
    st.markdown('<div class="guru-line">🔥 "ये बढ़िया था गुरु!" 😎</div>', unsafe_allow_html=True)

else:
    # Error Warning for Wrong/Invalid Date Format
    st.markdown("""
    <div class="error-line">
        🚨 "🦁 वाह मेरे शेर! कर दिया गलत टॉपअप! 👏🤡" 😱💸
    </div>
    """, unsafe_allow_html=True)
