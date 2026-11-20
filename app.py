import streamlit as st
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from dateutil import parser

# 1. Page Config
st.set_page_config(
    page_title="PAPA CALENDAR",
    page_icon="👨🏻‍🦰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Refined & Polished Executive CSS (Preserving Your Exact Layout)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Clean Subtle Background */
    .stApp {
        background: linear-gradient(180deg, #F8FAFC 0%, #F1F5F9 100%);
        color: #0F172A;
    }

    header[data-testid="stHeader"], #MainMenu, footer {
        display: none !important;
    }

    /* Title Styling */
    h1 {
        color: #0F172A !important;
        font-weight: 800 !important;
        letter-spacing: -0.6px;
        text-align: center;
        font-size: 1.95rem !important;
        margin-bottom: 4px !important;
    }

    /* Subtitle Badge */
    .creator-subtitle {
        text-align: center;
        font-size: 0.76rem;
        font-weight: 700;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 1.6px;
        margin-bottom: 26px;
    }

    /* Input Labels */
    label {
        color: #475569 !important;
        font-size: 0.74rem !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 6px !important;
    }

    /* Segmented Control (Matches Dark Theme Instead of Red) */
    div[data-testid="stSegmentedControl"] {
        background: #E2E8F0 !important;
        padding: 4px !important;
        border-radius: 12px !important;
        border: 1px solid #CBD5E1 !important;
        margin-bottom: 10px !important;
        box-shadow: inset 0 1px 2px rgba(15, 23, 42, 0.06) !important;
    }

    div[data-testid="stSegmentedControl"] button {
        border-radius: 9px !important;
        font-weight: 700 !important;
        font-size: 0.85rem !important;
        border: none !important;
        padding: 6px 18px !important;
        transition: all 0.2s ease !important;
    }

    div[data-testid="stSegmentedControl"] button[aria-checked="true"] {
        background: #0F172A !important;
        color: #FFFFFF !important;
        box-shadow: 0 3px 8px rgba(15, 23, 42, 0.2) !important;
    }

    div[data-testid="stSegmentedControl"] button[aria-checked="false"] {
        color: #475569 !important;
        background: transparent !important;
    }

    /* Date Input Box */
    div[data-baseweb="input"] {
        border-radius: 12px !important;
        border: 1.5px solid #CBD5E1 !important;
        background: #FFFFFF !important;
        box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04) !important;
        transition: all 0.2s ease !important;
    }
    
    div[data-baseweb="input"] input {
        color: #0F172A !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        padding: 10px 14px !important;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #0F172A !important;
        box-shadow: 0 0 0 4px rgba(15, 23, 42, 0.08) !important;
    }

    /* Divider Line */
    hr {
        border: none !important;
        border-top: 1px solid #E2E8F0 !important;
        margin: 22px 0 !important;
    }

    /* Metric Cards Grid Layout */
    .metric-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(135px, 1fr));
        gap: 14px;
        margin: 20px 0;
    }

    /* Enhanced Card Style */
    .metric-card {
        padding: 22px 14px;
        border-radius: 14px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        text-align: center;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 24px -6px rgba(15, 23, 42, 0.1);
    }

    /* Card 1: Blue */
    .card-till-then { 
        border-top: 4px solid #2563EB; 
        background: linear-gradient(180deg, #EFF6FF 0%, #FFFFFF 35%);
    }
    .card-till-then .metric-title { color: #2563EB; }
    .card-till-then .metric-val { color: #1E3A8A; }

    /* Card 2: Amber */
    .card-total-days { 
        border-top: 4px solid #D97706; 
        background: linear-gradient(180deg, #FFFBEB 0%, #FFFFFF 35%);
    }
    .card-total-days .metric-title { color: #D97706; }
    .card-total-days .metric-val { color: #78350F; }

    /* Card 3: Emerald */
    .card-topup-month { 
        border-top: 4px solid #059669; 
        background: linear-gradient(180deg, #ECFDF5 0%, #FFFFFF 35%);
    }
    .card-topup-month .metric-title { color: #059669; }
    .card-topup-month .metric-val { color: #064E3B; }

    /* Card 4: Rich Obsidian Highlight */
    .card-rounded-month {
        background: linear-gradient(145deg, #0F172A 0%, #1E293B 100%) !important;
        border: 1px solid #334155 !important;
        border-top: 4px solid #38BDF8 !important;
        box-shadow: 0 8px 20px -4px rgba(15, 23, 42, 0.25) !important;
    }
    .card-rounded-month .metric-title { color: #94A3B8 !important; }
    .card-rounded-month .metric-val { color: #FFFFFF !important; font-size: 1.3rem !important; }

    .card-rounded-month:hover {
        box-shadow: 0 14px 28px -4px rgba(15, 23, 42, 0.35) !important;
    }

    .metric-title {
        font-size: 0.68rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 8px;
    }

    .metric-val {
        font-size: 1.2rem;
        font-weight: 800;
        letter-spacing: -0.3px;
    }

    /* Polished Result Box (Same Structure, Better Look) */
    div[data-testid="stAlert"] {
        background: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        border-left: 5px solid #059669 !important;
        border-radius: 14px !important;
        color: #1E293B !important;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04) !important;
        padding: 18px 20px !important;
    }

    div[data-testid="stAlert"] p, div[data-testid="stAlert"] li {
        color: #334155 !important;
        font-size: 0.92rem !important;
        line-height: 1.65 !important;
    }

    div[data-testid="stAlert"] code {
        background: #F1F5F9 !important;
        color: #0F172A !important;
        font-weight: 700 !important;
        padding: 2px 7px !important;
        border-radius: 6px !important;
        border: 1px solid #E2E8F0 !important;
    }

    /* Footer Badge */
    .guru-line {
        text-align: center;
        font-size: 0.85rem;
        font-weight: 600;
        color: #475569;
        margin-top: 24px;
        padding: 12px;
        border-radius: 12px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 6px rgba(15, 23, 42, 0.03);
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

# 4. Duration Selector Buttons (Above Date Box)
duration_choice = st.segmented_control(
    "⏳ Select Target Duration:",
    options=["1 Year", "2 Years"],
    default="2 Years",
    selection_mode="single"
)

if not duration_choice:
    duration_choice = "2 Years"

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