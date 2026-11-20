import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil import parser

# 1. Page Config
st.set_page_config(
    page_title="PAPA CALENDAR",
    page_icon="🪙",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Next-Level Polished Executive CSS (Same Classic Layout, Superior Finish)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Soft Premium Canvas Background */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #FFFFFF 0%, #F1F5F9 100%);
        color: #0F172A;
    }

    header[data-testid="stHeader"], #MainMenu, footer {
        display: none !important;
    }

    .block-container {
        padding-top: 2.2rem !important;
        padding-bottom: 2.5rem !important;
        max-width: 680px !important;
    }

    /* Main Title */
    h1 {
        color: #0F172A !important;
        font-weight: 800 !important;
        letter-spacing: -0.7px;
        text-align: center;
        font-size: 2rem !important;
        margin-bottom: 4px !important;
    }

    /* Subtitle Badge */
    .creator-subtitle {
        text-align: center;
        font-size: 0.74rem;
        font-weight: 700;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 1.8px;
        margin-bottom: 24px;
    }

    /* Centered Duration Pill Selector (100% Centered & No Red Border) */
    div[data-testid="stRadio"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        margin-bottom: 14px !important;
    }

    div[data-testid="stRadio"] > label {
        color: #475569 !important;
        font-size: 0.72rem !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px !important;
        text-align: center !important;
    }

    div[data-testid="stRadio"] > div[role="radiogroup"] {
        background: #E2E8F0 !important;
        padding: 4px !important;
        border-radius: 12px !important;
        border: 1px solid #CBD5E1 !important;
        box-shadow: inset 0 1px 3px rgba(15, 23, 42, 0.08) !important;
        display: inline-flex !important;
        gap: 4px !important;
    }

    div[data-testid="stRadio"] > div[role="radiogroup"] > label {
        background: transparent !important;
        padding: 7px 26px !important;
        border-radius: 9px !important;
        margin: 0 !important;
        cursor: pointer !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        border: none !important;
    }

    /* Hide default radio circle */
    div[data-testid="stRadio"] > div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }

    /* Unselected text */
    div[data-testid="stRadio"] > div[role="radiogroup"] > label p {
        font-size: 0.86rem !important;
        font-weight: 700 !important;
        color: #475569 !important;
        margin: 0 !important;
    }

    /* Selected Pill Style */
    div[data-testid="stRadio"] > div[role="radiogroup"] > label:has(input:checked) {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%) !important;
        box-shadow: 0 4px 10px rgba(15, 23, 42, 0.22) !important;
    }

    div[data-testid="stRadio"] > div[role="radiogroup"] > label:has(input:checked) p {
        color: #FFFFFF !important;
    }

    /* Input Label */
    div[data-testid="stTextInput"] label {
        color: #475569 !important;
        font-size: 0.74rem !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 6px !important;
    }

    /* Sleek Input Box */
    div[data-baseweb="input"] {
        border-radius: 12px !important;
        border: 1.5px solid #CBD5E1 !important;
        background: #FFFFFF !important;
        box-shadow: 0 3px 10px rgba(15, 23, 42, 0.04) !important;
        transition: all 0.2s ease !important;
    }
    
    div[data-baseweb="input"] input {
        color: #0F172A !important;
        font-weight: 700 !important;
        font-size: 1.02rem !important;
        padding: 11px 16px !important;
        letter-spacing: 0.3px;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #0F172A !important;
        box-shadow: 0 0 0 4px rgba(15, 23, 42, 0.08), 0 4px 12px rgba(15, 23, 42, 0.06) !important;
    }

    /* Clean Divider */
    hr {
        border: none !important;
        border-top: 1px solid #E2E8F0 !important;
        margin: 22px 0 !important;
    }

    /* 4 Metric Cards Grid */
    .metric-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin: 20px 0;
    }

    @media (max-width: 600px) {
        .metric-container {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    .metric-card {
        padding: 20px 12px;
        border-radius: 16px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        text-align: center;
        box-shadow: 0 6px 16px -4px rgba(15, 23, 42, 0.05);
        transition: transform 0.22s ease, box-shadow 0.22s ease;
    }

    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 14px 26px -6px rgba(15, 23, 42, 0.12);
    }

    /* Card 1: Royal Blue */
    .card-till-then { 
        border-top: 4px solid #2563EB; 
        background: linear-gradient(180deg, #EFF6FF 0%, #FFFFFF 42%);
    }
    .card-till-then .metric-title { color: #2563EB; }
    .card-till-then .metric-val { color: #1E3A8A; }

    /* Card 2: Warm Amber */
    .card-total-days { 
        border-top: 4px solid #F59E0B; 
        background: linear-gradient(180deg, #FFFBEB 0%, #FFFFFF 42%);
    }
    .card-total-days .metric-title { color: #D97706; }
    .card-total-days .metric-val { color: #78350F; }

    /* Card 3: Emerald Green */
    .card-topup-month { 
        border-top: 4px solid #10B981; 
        background: linear-gradient(180deg, #ECFDF5 0%, #FFFFFF 42%);
    }
    .card-topup-month .metric-title { color: #059669; }
    .card-topup-month .metric-val { color: #064E3B; }

    /* Card 4: Obsidian Spotlight Card */
    .card-rounded-month {
        background: linear-gradient(145deg, #0F172A 0%, #1E293B 100%) !important;
        border: 1px solid #334155 !important;
        border-top: 4px solid #38BDF8 !important;
        box-shadow: 0 10px 24px -4px rgba(15, 23, 42, 0.28) !important;
    }
    .card-rounded-month .metric-title { color: #94A3B8 !important; }
    .card-rounded-month .metric-val { color: #FFFFFF !important; font-size: 1.32rem !important; }

    .card-rounded-month:hover {
        box-shadow: 0 16px 32px -4px rgba(15, 23, 42, 0.38) !important;
    }

    .metric-title {
        font-size: 0.66rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 8px;
    }

    .metric-val {
        font-size: 1.18rem;
        font-weight: 800;
        letter-spacing: -0.3px;
    }

    /* Refined Result Details Box */
    div[data-testid="stAlert"] {
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-left: 5px solid #10B981 !important;
        border-radius: 16px !important;
        color: #1E293B !important;
        box-shadow: 0 6px 20px -4px rgba(15, 23, 42, 0.05) !important;
        padding: 20px 22px !important;
    }

    div[data-testid="stAlert"] p, div[data-testid="stAlert"] li {
        color: #334155 !important;
        font-size: 0.92rem !important;
        line-height: 1.7 !important;
    }

    div[data-testid="stAlert"] code {
        background: #F1F5F9 !important;
        color: #0F172A !important;
        font-weight: 700 !important;
        padding: 3px 8px !important;
        border-radius: 6px !important;
        border: 1px solid #CBD5E1 !important;
    }

    /* Crisp Signature Footer */
    .guru-line {
        text-align: center;
        font-size: 0.84rem;
        font-weight: 600;
        color: #64748B;
        margin-top: 24px;
        padding: 12px 16px;
        border-radius: 12px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03);
        letter-spacing: 0.3px;
    }

    .guru-line b {
        color: #0F172A;
        font-weight: 800;
    }

    /* Popup Dialog Box */
    .popup-box {
        background: #FFFFFF;
        border: 1px solid #FCA5A5;
        border-top: 4px solid #DC2626;
        padding: 18px;
        border-radius: 10px;
        text-align: center;
    }
    .popup-header { font-size: 1.15rem; font-weight: 800; color: #991B1B; margin-bottom: 6px; }
    .popup-sub { font-size: 0.85rem; font-weight: 500; color: #4B5563; }
    </style>
""", unsafe_allow_html=True)

# 3. Native Streamlit Popup Dialog
@st.dialog("🚨 Warning!")
def show_error_popup():
    st.markdown("""
        <div class="popup-box">
            <div class="popup-header">Are Malik wo zara si galti ho gyi! 👏🤡</div>
            <div class="popup-sub">"अबे DATE सही डालो भाई!" </div>
        </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Sorry 🙏🏻 (close)", use_container_width=True):
        st.rerun()

# Main Title
st.title("🪙 Topup Calendar")
st.markdown('<div class="creator-subtitle">Avoid Salary Cuts With Smart Calendar Tracking</div>', unsafe_allow_html=True)

# 4. Centered Duration Selector (Guaranteed Center Alignment)
duration_choice = st.radio(
    "⏳ Select  Duration",
    options=["1 Year", "2 Years"],
    index=1,
    horizontal=True
)

selected_years = 1 if duration_choice == "1 Year" else 2

# 5. Date Input Field
user_date_str = st.text_input(
    "📌 Plan Expire At:", 
    value="16-07-2027", 
    help="You can paste any format e.g. 16-07-2027, 2027/07/16, 16 Jul 2027"
)

input_date = None
clean_str = user_date_str.strip()

if clean_str:
    try:
        input_date = parser.parse(clean_str, dayfirst=True).date()
    except (ValueError, OverflowError):
        input_date = None

today = date.today()
target_date = today + relativedelta(years=selected_years)

# Calculation & Logic Handling
if not clean_str:
    st.info("👆 कृपया ऊपर बॉक्स में प्लान की एक्सपायरी डेट डालें।")
elif input_date is None:
    show_error_popup()
    st.error("🚨 Please paste date carefully 100% SALARY CUT CHANCE AVAILABLE ")
else:
    total_days_diff = (target_date - input_date).days
    
    if input_date <= target_date:
        diff = relativedelta(target_date, input_date)
        months_remaining = diff.years * 12 + diff.months
        days_remaining = diff.days
        display_month_str = f"{months_remaining}M {days_remaining}D"
        
        final_rounded_months = months_remaining + 1 if days_remaining > 0 else months_remaining
        rounded_month_str = f"{final_rounded_months} Months"
    else:
        diff = relativedelta(input_date, target_date)
        months_over = diff.years * 12 + diff.months
        days_over = diff.days
        display_month_str = f"-({months_over}M {days_over}D)"
        rounded_month_str = "N/A"

    st.write("---")

    # Metric Cards Layout (Your Exact 4 Cards)
    st.markdown(f"""
    <div class="metric-container">
        <div class="metric-card card-till-then">
            <div class="metric-title">Till Then ({duration_choice})</div>
            <div class="metric-val">{target_date.strftime('%d-%b-%Y')}</div>
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

    # Details Box (Your Exact Structure)
    if total_days_diff >= 0:
        st.success(f"""
        🫵🏻 **Result Details:**
- **Selected Date:** `{input_date.strftime('%d-%b-%Y')}`
- **Target Date ({duration_choice}):** `{target_date.strftime('%d-%b-%Y')}`
- **Exact Time Remaining:** **{months_remaining} Months & {days_remaining} Days** (Total: **{total_days_diff} Days**)
- **Required Topup (Rounded):** **{final_rounded_months} Full Months** *(Extra {days_remaining} days added as +1 month)*
        """)
    else:
        st.warning(f"⚠️ Selected date is **{abs(total_days_diff)} days** beyond target date ({duration_choice})!")

    # FOOTER SIGNATURE
    st.markdown('<div class="guru-line">| Crafted by <b>Mratyunjay Brahmavanshi</b></div>', unsafe_allow_html=True)