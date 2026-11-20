import streamlit as st
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from dateutil import parser

# 1. Page Config
st.set_page_config(
    page_title="PAPA CALENDAR | Executive Edition",
    page_icon="🪙",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Ultra-Premium Executive Dashboard CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@600;700&display=swap');
    
    * {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Ambient Luxury Background */
    .stApp {
        background-color: #F4F6FA;
        background-image: 
            radial-gradient(at 0% 0%, rgba(37, 99, 235, 0.06) 0px, transparent 50%),
            radial-gradient(at 100% 0%, rgba(217, 119, 6, 0.06) 0px, transparent 50%),
            radial-gradient(at 50% 100%, rgba(15, 23, 42, 0.04) 0px, transparent 50%);
        color: #0F172A;
    }

    header[data-testid="stHeader"], #MainMenu, footer {
        display: none !important;
    }

    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2.5rem !important;
        max-width: 720px !important;
    }

    /* Executive Top Header */
    .hero-header {
        text-align: center;
        margin-bottom: 24px;
    }

    .live-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);
        color: #334155;
        font-size: 0.7rem;
        font-weight: 700;
        padding: 5px 14px;
        border-radius: 999px;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .pulse-dot {
        width: 7px;
        height: 7px;
        background-color: #10B981;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2);
    }

    .main-title {
        font-size: 2.25rem;
        font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #0F172A 0%, #334155 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        line-height: 1.15;
    }

    .sub-tagline {
        font-size: 0.85rem;
        font-weight: 500;
        color: #64748B;
        margin-top: 6px;
    }

    /* Glassmorphic Input Control Panel */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.92) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid #FFFFFF !important;
        border-radius: 20px !important;
        padding: 22px 24px !important;
        box-shadow: 
            0 20px 35px -10px rgba(15, 23, 42, 0.06),
            0 0 0 1px rgba(226, 232, 240, 0.8) !important;
    }

    label {
        color: #475569 !important;
        font-size: 0.72rem !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        letter-spacing: 0.9px;
        margin-bottom: 6px !important;
    }

    /* Sleek Segmented Toggle */
    div[data-testid="stSegmentedControl"] {
        background: #F1F5F9 !important;
        padding: 4px !important;
        border-radius: 12px !important;
        border: 1px solid #E2E8F0 !important;
    }

    div[data-testid="stSegmentedControl"] button {
        border-radius: 9px !important;
        font-weight: 700 !important;
        font-size: 0.85rem !important;
        border: none !important;
        padding: 6px 12px !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    div[data-testid="stSegmentedControl"] button[aria-checked="true"] {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%) !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 10px rgba(15, 23, 42, 0.25) !important;
    }

    div[data-testid="stSegmentedControl"] button[aria-checked="false"] {
        color: #64748B !important;
        background: transparent !important;
    }

    /* Input Box */
    div[data-baseweb="input"] {
        border-radius: 12px !important;
        border: 1.5px solid #E2E8F0 !important;
        background: #F8FAFC !important;
        transition: all 0.2s ease !important;
    }
    
    div[data-baseweb="input"] input {
        font-family: 'JetBrains Mono', monospace !important;
        color: #0F172A !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        padding: 10px 14px !important;
    }

    div[data-baseweb="input"]:focus-within {
        background: #FFFFFF !important;
        border-color: #0F172A !important;
        box-shadow: 0 0 0 4px rgba(15, 23, 42, 0.08) !important;
    }

    /* Asymmetric Bento Grid Layout */
    .bento-grid {
        display: grid;
        grid-template-columns: 1.15fr 1fr;
        gap: 16px;
        margin: 22px 0;
    }

    @media (max-width: 640px) {
        .bento-grid {
            grid-template-columns: 1fr;
        }
    }

    /* Left VIP Obsidian-Gold Card */
    .vip-hero-card {
        background: linear-gradient(145deg, #090D16 0%, #162032 60%, #1E293B 100%);
        border-radius: 20px;
        padding: 26px 24px;
        color: #FFFFFF;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(251, 191, 36, 0.35);
        box-shadow: 0 20px 35px -10px rgba(15, 23, 42, 0.35);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .vip-hero-card::before {
        content: "";
        position: absolute;
        top: -50%;
        right: -30%;
        width: 220px;
        height: 220px;
        background: radial-gradient(circle, rgba(245, 158, 11, 0.22) 0%, transparent 70%);
        pointer-events: none;
    }

    .vip-tag {
        display: inline-block;
        background: rgba(245, 158, 11, 0.15);
        border: 1px solid rgba(245, 158, 11, 0.4);
        color: #FBBF24;
        font-size: 0.68rem;
        font-weight: 800;
        padding: 4px 10px;
        border-radius: 6px;
        letter-spacing: 1px;
        text-transform: uppercase;
        width: fit-content;
    }

    .vip-main-number {
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -1.5px;
        margin: 14px 0 4px 0;
        background: linear-gradient(90deg, #FFFFFF 0%, #FDE68A 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.1;
    }

    .vip-subtext {
        font-size: 0.82rem;
        color: #94A3B8;
        font-weight: 500;
    }

    /* Right Stack of 3 Mini Cards */
    .mini-stack {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .mini-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 13px 18px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .mini-card:hover {
        transform: translateX(3px);
        border-color: #CBD5E1;
    }

    .mini-label {
        font-size: 0.72rem;
        font-weight: 700;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }

    .mini-val {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 1.02rem;
        font-weight: 700;
        color: #0F172A;
    }

    .accent-blue { border-left: 4px solid #2563EB; }
    .accent-amber { border-left: 4px solid #F59E0B; }
    .accent-emerald { border-left: 4px solid #10B981; }

    /* Visual Timeline Card */
    .ledger-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 18px;
        padding: 20px 24px;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.03);
    }

    .ledger-title {
        font-size: 0.85rem;
        font-weight: 800;
        color: #0F172A;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 14px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .progress-track {
        width: 100%;
        height: 8px;
        background: #F1F5F9;
        border-radius: 999px;
        overflow: hidden;
        margin-bottom: 18px;
    }

    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #2563EB 0%, #10B981 100%);
        border-radius: 999px;
    }

    .ledger-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 9px 0;
        border-bottom: 1px dashed #E2E8F0;
        font-size: 0.88rem;
    }

    .ledger-row:last-child {
        border-bottom: none;
        padding-bottom: 0;
    }

    .l-key { color: #64748B; font-weight: 600; }
    .l-val { color: #0F172A; font-weight: 700; }

    .status-chip {
        background: #ECFDF5;
        color: #047857;
        border: 1px solid #A7F3D0;
        padding: 3px 10px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 800;
    }

    /* Footer */
    .exec-footer {
        text-align: center;
        margin-top: 26px;
        font-size: 0.8rem;
        color: #64748B;
        font-weight: 500;
    }

    .exec-footer span {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        padding: 8px 18px;
        border-radius: 999px;
        box-shadow: 0 2px 6px rgba(15, 23, 42, 0.03);
    }

    .exec-footer b {
        color: #0F172A;
        font-weight: 700;
    }

    /* Popup Styling */
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
@st.dialog("🚨 Invalid Date Format")
def show_error_popup():
    st.markdown("""
        <div class="popup-box">
            <div class="popup-header">Are Malik wo zara si galti ho gyi! 👏🤡</div>
            <div class="popup-sub">"अबे DATE सही डालो भाई!"</div>
        </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Sorry 🙏🏻 (Close)", use_container_width=True):
        st.rerun()

# 4. Executive Hero Header
st.markdown("""
    <div class="hero-header">
        <div class="live-pill"><span class="pulse-dot"></span> Smart Validity Engine</div>
        <h1 class="main-title">Topup Calendar</h1>
        <div class="sub-tagline">Zero-error validity tracking to prevent salary deductions</div>
    </div>
""", unsafe_allow_html=True)

# 5. Control Panel Card
with st.container(border=True):
    col1, col2 = st.columns([1, 1.45], vertical_alignment="bottom")
    
    with col1:
        duration_choice = st.segmented_control(
            "⏳ Target Horizon",
            options=["1 Year", "2 Years"],
            default="2 Years",
            selection_mode="single"
        )
        if not duration_choice:
            duration_choice = "2 Years"

    with col2:
        user_date_str = st.text_input(
            "📌 Current Plan Expiry", 
            value="16-07-2027", 
            help="Paste any date format: 16-07-2027, 2027/07/16, 16 Jul 2027"
        )

selected_years = 1 if duration_choice == "1 Year" else 2

# Date Parsing
input_date = None
clean_str = user_date_str.strip()

if clean_str:
    try:
        input_date = parser.parse(clean_str, dayfirst=True).date()
    except (ValueError, OverflowError):
        input_date = None

today = date.today()
target_date = today + relativedelta(years=selected_years)

# 6. Calculation & Premium Bento Display
if not clean_str:
    st.info("👆 कृपया ऊपर दिए गए बॉक्स में प्लान की एक्सपायरी डेट दर्ज करें।")
elif input_date is None:
    show_error_popup()
    st.error("🚨 Invalid Date! Please enter a valid date to avoid 100% salary cut risk.")
else:
    total_days_diff = (target_date - input_date).days
    total_horizon_days = (target_date - today).days
    
    if input_date <= target_date:
        diff = relativedelta(target_date, input_date)
        months_remaining = diff.years * 12 + diff.months
        days_remaining = diff.days
        display_month_str = f"{months_remaining}M {days_remaining}D"
        
        final_rounded_months = months_remaining + 1 if days_remaining > 0 else months_remaining
        rounded_month_str = f"{final_rounded_months} Months"
        
        # Calculate percentage for visual bar
        coverage_pct = max(5, min(100, int(((total_horizon_days - total_days_diff) / max(1, total_horizon_days)) * 100)))
    else:
        diff = relativedelta(input_date, target_date)
        months_over = diff.years * 12 + diff.months
        days_over = diff.days
        display_month_str = f"-({months_over}M {days_over}D)"
        rounded_month_str = "0 Months"
        coverage_pct = 100

    # Asymmetric Bento Grid (VIP Hero Card + 3 Stacked Cards)
    st.markdown(f"""
    <div class="bento-grid">
        <div class="vip-hero-card">
            <div class="vip-tag">★ Required Full Topup</div>
            <div>
                <div class="vip-main-number">{rounded_month_str}</div>
                <div class="vip-subtext">Rounded up for {duration_choice} target protection</div>
            </div>
        </div>
        <div class="mini-stack">
            <div class="mini-card accent-blue">
                <span class="mini-label">Till Then ({duration_choice})</span>
                <span class="mini-val">{target_date.strftime('%d-%b-%Y')}</span>
            </div>
            <div class="mini-card accent-amber">
                <span class="mini-label">Total Gap Days</span>
                <span class="mini-val">{total_days_diff} Days</span>
            </div>
            <div class="mini-card accent-emerald">
                <span class="mini-label">Exact Topup</span>
                <span class="mini-val">{display_month_str}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Executive Ledger & Progress Bar
    if total_days_diff >= 0:
        extra_rule = f"+1 month buffer for {days_remaining} extra days" if days_remaining > 0 else "Exact month alignment"
        st.markdown(f"""
        <div class="ledger-card">
            <div class="ledger-title">
                <span>Validity Coverage & Breakdown</span>
                <span class="status-chip">✓ Safe Margin</span>
            </div>
            <div class="progress-track">
                <div class="progress-fill" style="width: {coverage_pct}%;"></div>
            </div>
            <div class="ledger-row">
                <span class="l-key">Current Expiry Date</span>
                <span class="l-val">{input_date.strftime('%d %B, %Y')}</span>
            </div>
            <div class="ledger-row">
                <span class="l-key">Target Benchmark ({duration_choice})</span>
                <span class="l-val">{target_date.strftime('%d %B, %Y')}</span>
            </div>
            <div class="ledger-row">
                <span class="l-key">Exact Shortfall</span>
                <span class="l-val">{months_remaining} Months, {days_remaining} Days ({total_days_diff} Days)</span>
            </div>
            <div class="ledger-row">
                <span class="l-key">Rounding Rule Applied</span>
                <span class="l-val">{extra_rule}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ Your plan is already valid **{abs(total_days_diff)} days** beyond the {duration_choice} target date! No topup needed.")

    # Executive Signature Footer
    st.markdown("""
        <div class="exec-footer">
            <span>Crafted with precision by <b>Mratyunjay Brahmavanshi</b></span>
        </div>
    """, unsafe_allow_html=True)