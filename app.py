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
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif !important;
    }

    /* Classic Slate/Navy Background */
    .stApp {
        background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
        color: #F8FAFC;
    }

    /* Hide Unnecessary Streamlit Elements */
    header[data-testid="stHeader"], #MainMenu, footer {
        display: none !important;
    }

    /* Classic Royal Title */
    h1 {
        font-family: 'Cinzel', serif !important;
        color: #F1F5F9 !important;
        font-weight: 700 !important;
        font-size: 1.9rem !important;
        letter-spacing: 2px;
        text-align: center;
        margin-bottom: 25px !important;
        text-transform: uppercase;
    }

    /* Input Box Minimal Classic Style */
    label {
        color: #94A3B8 !important;
        font-size: 0.8rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    div[data-baseweb="input"] {
        border-radius: 8px !important;
        border: 1px solid #334155 !important;
        background: #1E293B !important;
        color: #F8FAFC !important;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.2) !important;
        transition: all 0.3s ease;
    }
    
    div[data-baseweb="input"] input {
        color: #F8FAFC !important;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #CBD5E1 !important;
        box-shadow: 0px 0px 10px rgba(241, 245, 249, 0.15) !important;
    }

    /* Card Container Grid */
    .metric-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
        gap: 12px;
        margin: 25px 0;
    }

    /* Classic Card Style */
    .metric-card {
        padding: 18px 12px;
        border-radius: 10px;
        background: #1E293B;
        border: 1px solid #334155;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        text-align: center;
        transition: all 0.3s ease;
    }

    .metric-card:hover {
        border-color: #64748B;
        transform: translateY(-2px);
    }

    /* Dynamic Classic Themes */
    .card-till-then .metric-title { color: #38BDF8; }
    .card-till-then .metric-val { color: #F0F9FF; }

    .card-total-days .metric-title { color: #FBBF24; }
    .card-total-days .metric-val { color: #FFFBEB; }

    .card-topup-month .metric-title { color: #34D399; }
    .card-topup-month .metric-val { color: #ECFDF5; }

    /* Classic Gold/Platinum Accent Card */
    .card-rounded-month {
        background: linear-gradient(135deg, #334155 0%, #1E293B 100%) !important;
        border: 1px solid #94A3B8 !important;
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.05) !important;
    }
    .card-rounded-month .metric-title { color: #E2E8F0 !important; }
    .card-rounded-month .metric-val { color: #FFFFFF !important; font-size: 1.25rem !important; }

    .metric-title {
        font-size: 0.68rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 6px;
    }

    .metric-val {
        font-size: 1.15rem;
        font-weight: 700;
    }

    /* Result Details Box (Dark Glass) */
    .stSuccess {
        background: #1E293B !important;
        border: 1px solid #334155 !important;
        border-left: 4px solid #10B981 !important;
        border-radius: 8px !important;
        color: #E2E8F0 !important;
    }

    /* Classic Button */
    .stButton>button {
        width: 100%;
        border-radius: 8px !important;
        background: #334155 !important;
        color: #F8FAFC !important;
        font-weight: 600 !important;
        border: 1px solid #475569 !important;
        padding: 10px !important;
        letter-spacing: 0.5px;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        background: #475569 !important;
        border-color: #94A3B8 !important;
        color: #FFFFFF !important;
    }

    /* Classic Minimal Tagline */
    .guru-line {
        text-align: center;
        font-family: 'Cinzel', serif !important;
        font-size: 0.95rem;
        font-weight: 600;
        color: #CBD5E1;
        margin-top: 30px;
        padding: 10px;
        border-radius: 6px;
        background: #1E293B;
        border: 1px solid #334155;
        letter-spacing: 1px;
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
