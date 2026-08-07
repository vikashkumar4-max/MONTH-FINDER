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

# 2. Custom Classic CSS (Luxurious & Sleek Look)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif !important;
    }

    /* Dark Executive Background */
    .stApp {
        background: #0B0F19;
        color: #E2E8F0;
    }

    /* Hide Top Header Toolbar & Footer */
    header[data-testid="stHeader"], #MainMenu, footer {
        display: none !important;
    }

    /* Royal Title */
    h1 {
        font-family: 'Cinzel', serif !important;
        color: #F8FAFC !important;
        letter-spacing: 2px;
        text-align: center;
        font-size: 1.8rem !important;
        margin-bottom: 25px !important;
        text-transform: uppercase;
    }

    /* Label Styling */
    label {
        color: #94A3B8 !important;
        font-size: 0.8rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600 !important;
    }

    /* Classic Input with Inner Shadow & Glow */
    div[data-baseweb="input"] {
        border-radius: 8px !important;
        border: 1px solid #1E293B !important;
        background: #111827 !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    div[data-baseweb="input"] input {
        color: #F8FAFC !important;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #475569 !important;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.5), 0 0 12px rgba(255, 255, 255, 0.08) !important;
    }

    /* Custom Metric Cards Grid */
    .metric-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
        gap: 12px;
        margin: 25px 0;
    }

    /* Frosted Glass Card Base */
    .metric-card {
        padding: 18px 12px;
        border-radius: 12px;
        background: rgba(17, 24, 39, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        text-align: center;
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* Classic Gold Shimmer Hover Effect */
    .metric-card:hover {
        border-color: rgba(212, 175, 55, 0.45) !important;
        transform: translateY(-3px);
        box-shadow: 0 12px 25px -5px rgba(0, 0, 0, 0.6);
    }

    /* Specific Card Color Accents */
    .card-till-then .metric-title { color: #38BDF8; }
    .card-till-then .metric-val { color: #F0F9FF; }

    .card-total-days .metric-title { color: #FBBF24; }
    .card-total-days .metric-val { color: #FFFBEB; }

    .card-topup-month .metric-title { color: #34D399; }
    .card-topup-month .metric-val { color: #ECFDF5; }

    /* Special Full Topup Gold Highlight Card */
    .card-rounded-month {
        background: linear-gradient(145deg, #1E293B 0%, #0F172A 100%) !important;
        border: 1px solid rgba(212, 175, 55, 0.5) !important;
        box-shadow: 0 4px 20px rgba(212, 175, 55, 0.08) !important;
    }
    .card-rounded-month .metric-title { color: #FDE68A !important; }
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

    /* Result Details Box */
    .stSuccess {
        background: #111827 !important;
        border: 1px solid #1E293B !important;
        border-left: 4px solid #10B981 !important;
        border-radius: 8px !important;
        color: #E2E8F0 !important;
    }

    /* Classic Button with Active Press Effect */
    .stButton>button {
        width: 100%;
        border-radius: 8px !important;
        background: #1E293B !important;
        color: #F8FAFC !important;
        border: 1px solid #334155 !important;
        padding: 10px !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
        transition: all 0.2s ease !important;
    }

    .stButton>button:hover {
        background: #334155 !important;
        border-color: #64748B !important;
        color: #FFFFFF !important;
    }

    .stButton>button:active {
        transform: scale(0.98) !important;
        background: #0F172A !important;
    }

    /* Classic Minimal Tagline */
    .guru-line {
        text-align: center;
        font-family: 'Cinzel', serif !important;
        font-size: 0.95rem;
        font-weight: 600;
        color: #CBD5E1;
        margin-top: 30px;
        padding: 12px;
        border-radius: 8px;
        background: #111827;
        border: 1px solid #1E293B;
        letter-spacing: 1px;
    }

    /* Unique Animated Error Popup Style */
    .popup-box {
        background: #1E1010;
        border: 1.5px dashed #EF4444;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 8px 25px rgba(239, 68, 68, 0.2);
    }

    .popup-header {
        font-size: 1.3rem;
        font-weight: 800;
        color: #FCA5A5;
        margin-bottom: 8px;
    }

    .popup-sub {
        font-size: 0.85rem;
        font-weight: 500;
        color: #FECACA;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Popup Function using Native Streamlit Dialog
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
    # Trigger Popup Dialog automatically on wrong input
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
