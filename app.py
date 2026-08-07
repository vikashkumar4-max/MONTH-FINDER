import streamlit as st
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

# 1. Page Config
st.set_page_config(
    page_title="PAPA CALENDAR - Topup Calculator 💰",
    page_icon="👨🏻‍🦰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS with REAL 3D CARD EFFECTS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');
    
    * {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Clean Modern Light Background */
    .stApp {
        background: linear-gradient(180deg, #F8FAFC 0%, #F1F5F9 100%);
        color: #0F172A;
    }

    /* Hide Top Header Toolbar & Footer */
    header[data-testid="stHeader"], #MainMenu, footer {
        display: none !important;
    }

    /* Title Styling */
    h1 {
        color: #0F172A !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
        text-align: center;
        font-size: 1.8rem !important;
        margin-bottom: 25px !important;
    }

    /* Label Styling */
    label {
        color: #475569 !important;
        font-size: 0.85rem !important;
        font-weight: 700 !important;
    }

    /* Input Box */
    div[data-baseweb="input"] {
        border-radius: 12px !important;
        border: 2px solid #E2E8F0 !important;
        background: #FFFFFF !important;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.03) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    div[data-baseweb="input"] input {
        color: #0F172A !important;
        font-weight: 600 !important;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #6366F1 !important;
        box-shadow: 0px 0px 16px rgba(99, 102, 241, 0.25) !important;
        transform: translateY(-1px);
    }

    /* 🔥 3D PERSPECTIVE CONTAINER FOR CARDS */
    .metric-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
        gap: 14px;
        margin: 25px 0;
        perspective: 1000px; /* Gives 3D Depth Perception */
    }

    /* 🔥 REAL 3D CARD BASE STYLE */
    .metric-card {
        padding: 18px 12px;
        border-radius: 16px;
        background: #FFFFFF;
        border: 1.5px solid #E2E8F0;
        text-align: center;
        transform-style: preserve-3d;
        box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
    }

    /* 🔥 3D HOVER EFFECT: TILT, LIFT & DEEP SHADOW */
    .metric-card:hover {
        transform: translateY(-10px) rotateX(8deg) rotateY(-4deg) scale(1.03);
        box-shadow: 0 20px 30px -5px rgba(0, 0, 0, 0.15), 0 10px 15px -5px rgba(0, 0, 0, 0.08) !important;
        border-color: #6366F1 !important;
    }

    /* Specific Card Color Accents */
    .card-till-then { border-top: 5px solid #3B82F6; }
    .card-till-then .metric-title { color: #1D4ED8; }
    .card-till-then .metric-val { color: #1E40AF; }

    .card-total-days { border-top: 5px solid #F59E0B; }
    .card-total-days .metric-title { color: #D97706; }
    .card-total-days .metric-val { color: #B45309; }

    .card-topup-month { border-top: 5px solid #10B981; }
    .card-topup-month .metric-title { color: #059669; }
    .card-topup-month .metric-val { color: #047857; }

    /* Special Full Topup Highlight Card (Royal Gradient 3D) */
    .card-rounded-month {
        background: linear-gradient(135deg, #4F46E5 0%, #3730A3 100%) !important;
        border: none !important;
        box-shadow: 0 12px 25px rgba(79, 70, 229, 0.35) !important;
    }
    .card-rounded-month .metric-title { color: #E0E7FF !important; }
    .card-rounded-month .metric-val { color: #FFFFFF !important; font-size: 1.25rem !important; }

    .card-rounded-month:hover {
        box-shadow: 0 25px 35px rgba(79, 70, 229, 0.55) !important;
    }

    /* 3D Inner Content Depth Effect */
    .metric-title {
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 6px;
        transform: translateZ(20px); /* Pushes text forward in 3D */
    }

    .metric-val {
        font-size: 1.15rem;
        font-weight: 800;
        transform: translateZ(30px); /* Pushes number further forward for pop-out feel */
    }

    /* Result Details Box */
    .stSuccess {
        background: #FFFFFF !important;
        border: 1.5px solid #E2E8F0 !important;
        border-left: 5px solid #10B981 !important;
        border-radius: 12px !important;
        color: #1E293B !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
    }

    /* Button with Active Click Scale Effect */
    .stButton>button {
        width: 100%;
        border-radius: 12px !important;
        background: linear-gradient(90deg, #2563EB 0%, #1D4ED8 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 12px !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.25) !important;
        transition: all 0.2s ease !important;
    }

    .stButton>button:hover {
        transform: translateY(-2px) scale(1.01);
        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.4) !important;
    }

    .stButton>button:active {
        transform: scale(0.97) !important;
    }

    /* Tagline Badge */
    .guru-line {
        text-align: center;
        font-size: 1rem;
        font-weight: 800;
        color: #4338CA;
        margin-top: 25px;
        padding: 12px;
        border-radius: 50px;
        background: #EEF2FF;
        border: 1px solid #C7D2FE;
        box-shadow: 0 2px 8px rgba(99, 102, 241, 0.1);
    }

    /* Animated Error Popup Style */
    .popup-box {
        background: #FEF2F2;
        border: 2px dashed #EF4444;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 8px 25px rgba(239, 68, 68, 0.15);
    }

    .popup-header {
        font-size: 1.3rem;
        font-weight: 800;
        color: #991B1B;
        margin-bottom: 8px;
    }

    .popup-sub {
        font-size: 0.88rem;
        font-weight: 600;
        color: #7F1D1D;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Native Streamlit Popup Dialog
@st.dialog("🚨 Warning!")
def show_error_popup():
    st.markdown("""
        <div class="popup-box">
            <div class="popup-header">🦁 वाह मेरे शेर! कर दिया गलत टॉपअप! 👏🤡</div>
            <div class="popup-sub">"अबे DATE सही डालो भाई! गलत तारीख डालकर क्या साबित करना चाहते हो?" 💸😱</div>
        </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("गलती मान ली 🙏🏻 (बंद करें)", use_container_width=True):
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

# Calculation & Logic Handling
if input_date is None:
    show_error_popup()
    st.error("🚨 अमान्य तारीख (Invalid Date)! कृपया सही Format दर्ज करें।")

else:
    total_days_diff = (two_years_later - input_date).days
    
    if input_date <= two_years_later:
        diff = relativedelta(two_years_later, input_date)
        months_remaining = diff.years * 12 + diff.months
        days_remaining = diff.days
        display_month_str = f"{months_remaining}M {days_remaining}D"
        
        # LOGIC: 1 दिन भी एक्स्ट्रा होने पर +1 महीना बढ़ जाएगा
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

    # Metric Cards Layout
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
        
        # Celebration Button
        if st.button("❄️ Celebrate Calculation"):
            st.snow()
    else:
        st.warning(f"⚠️ Selected date is **{abs(total_days_diff)} days** beyond target date!")

    # Footer Tagline
    st.markdown('<div class="guru-line">🔥 "ये बढ़िया था गुरु!" 😎</div>', unsafe_allow_html=True)
