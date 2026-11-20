import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil import parser

# 1. Page Config
st.set_page_config(
    page_title="Topup Calendar | Validity Calculator",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Clean Corporate SaaS CSS (Stripe / Linear Inspired)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Crisp Neutral Background */
    .stApp {
        background-color: #F8FAFC;
        color: #0F172A;
    }

    header[data-testid="stHeader"], #MainMenu, footer {
        display: none !important;
    }

    .block-container {
        padding-top: 2.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 740px !important;
    }

    /* Corporate Header */
    .corp-header {
        border-bottom: 1px solid #E2E8F0;
        padding-bottom: 18px;
        margin-bottom: 24px;
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
    }

    .corp-title {
        font-size: 1.65rem;
        font-weight: 700;
        color: #0F172A;
        letter-spacing: -0.5px;
        margin: 0;
        line-height: 1.2;
    }

    .corp-subtitle {
        font-size: 0.85rem;
        color: #64748B;
        margin-top: 4px;
        font-weight: 400;
    }

    .corp-date-badge {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.78rem;
        color: #475569;
        background: #FFFFFF;
        border: 1px solid #CBD5E1;
        padding: 5px 10px;
        border-radius: 6px;
        font-weight: 500;
    }

    /* Input Container */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 10px !important;
        padding: 20px !important;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04) !important;
    }

    label {
        color: #334155 !important;
        font-size: 0.78rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.2px;
        margin-bottom: 6px !important;
    }

    /* Segmented Control (Clean Neutral Style) */
    div[data-testid="stSegmentedControl"] {
        background-color: #F1F5F9 !important;
        padding: 3px !important;
        border-radius: 8px !important;
        border: 1px solid #E2E8F0 !important;
    }

    div[data-testid="stSegmentedControl"] button {
        border-radius: 6px !important;
        font-weight: 600 !important;
        font-size: 0.84rem !important;
        border: none !important;
        padding: 6px 14px !important;
        transition: all 0.15s ease !important;
    }

    div[data-testid="stSegmentedControl"] button[aria-checked="true"] {
        background-color: #0F172A !important;
        color: #FFFFFF !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1) !important;
    }

    div[data-testid="stSegmentedControl"] button[aria-checked="false"] {
        color: #475569 !important;
        background-color: transparent !important;
    }

    /* Input Field */
    div[data-baseweb="input"] {
        border-radius: 8px !important;
        border: 1px solid #CBD5E1 !important;
        background-color: #FFFFFF !important;
        transition: border-color 0.15s ease, box-shadow 0.15s ease !important;
    }
    
    div[data-baseweb="input"] input {
        font-family: 'JetBrains Mono', monospace !important;
        color: #0F172A !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        padding: 9px 12px !important;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #2563EB !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
    }

    /* 4-Column Standard KPI Grid */
    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        margin: 20px 0;
    }

    @media (max-width: 640px) {
        .kpi-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        .corp-header {
            flex-direction: column;
            align-items: flex-start;
            gap: 10px;
        }
    }

    .kpi-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 16px 18px;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.03);
    }

    .kpi-label {
        font-size: 0.72rem;
        font-weight: 600;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }

    .kpi-value {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 1.25rem;
        font-weight: 700;
        color: #0F172A;
        letter-spacing: -0.4px;
    }

    .kpi-sub {
        font-size: 0.72rem;
        color: #94A3B8;
        margin-top: 4px;
    }

    /* Primary Highlighted KPI Card */
    .kpi-primary {
        background: #0F172A;
        border: 1px solid #0F172A;
    }

    .kpi-primary .kpi-label {
        color: #94A3B8;
    }

    .kpi-primary .kpi-value {
        color: #FFFFFF;
    }

    .kpi-primary .kpi-sub {
        color: #38BDF8;
        font-weight: 500;
    }

    /* Professional Ledger Table */
    .report-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.03);
    }

    .report-header {
        background: #F8FAFC;
        padding: 12px 20px;
        border-bottom: 1px solid #E2E8F0;
        font-size: 0.8rem;
        font-weight: 600;
        color: #334155;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .badge-compliant {
        background: #DCFCE7;
        color: #166534;
        font-size: 0.7rem;
        font-weight: 600;
        padding: 2px 8px;
        border-radius: 4px;
        text-transform: none;
        letter-spacing: 0;
    }

    .report-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 20px;
        border-bottom: 1px solid #F1F5F9;
        font-size: 0.88rem;
    }

    .report-row:last-child {
        border-bottom: none;
        background: #F8FAFC;
    }

    .r-label {
        color: #475569;
        font-weight: 500;
    }

    .r-val {
        font-family: 'JetBrains Mono', monospace !important;
        color: #0F172A;
        font-weight: 600;
    }

    .r-val-highlight {
        font-family: 'JetBrains Mono', monospace !important;
        color: #1D4ED8;
        font-weight: 700;
        font-size: 0.95rem;
    }

    /* Minimal Footer */
    .corp-footer {
        margin-top: 28px;
        padding-top: 16px;
        border-top: 1px solid #E2E8F0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.78rem;
        color: #64748B;
    }

    .corp-footer strong {
        color: #0F172A;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

today = date.today()

# 3. Corporate Header
st.markdown(f"""
    <div class="corp-header">
        <div>
            <h1 class="corp-title">Topup Calendar</h1>
            <div class="corp-subtitle">Subscription Validity & Compliance Calculator</div>
        </div>
        <div class="corp-date-badge">Base Date: {today.strftime('%d %b %Y')}</div>
    </div>
""", unsafe_allow_html=True)

# 4. Control Panel
with st.container(border=True):
    col1, col2 = st.columns([1, 1.5], vertical_alignment="bottom")
    
    with col1:
        duration_choice = st.segmented_control(
            "Target Duration",
            options=["1 Year", "2 Years"],
            default="2 Years",
            selection_mode="single"
        )
        if not duration_choice:
            duration_choice = "2 Years"

    with col2:
        user_date_str = st.text_input(
            "Current Plan Expiry Date", 
            value="16-07-2027", 
            help="Accepted formats: DD-MM-YYYY, YYYY/MM/DD, DD MMM YYYY"
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

target_date = today + relativedelta(years=selected_years)

# 5. Calculations & Output
if not clean_str:
    st.info("Please enter a valid plan expiry date above to calculate required topup.")
elif input_date is None:
    st.error("Invalid date format. Please enter a standard date (e.g., 16-07-2027 or 16 Jul 2027).")
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
        display_month_str = f"-{months_over}M {days_over}D"
        rounded_month_str = "0 Months"

    # 4-Column KPI Grid
    st.markdown(f"""
    <div class="kpi-grid">
        <div class="kpi-card">
            <div class="kpi-label">Target Date</div>
            <div class="kpi-value">{target_date.strftime('%d %b %y')}</div>
            <div class="kpi-sub">{duration_choice} horizon</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Total Gap</div>
            <div class="kpi-value">{total_days_diff}d</div>
            <div class="kpi-sub">Calendar days</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Exact Shortfall</div>
            <div class="kpi-value">{display_month_str}</div>
            <div class="kpi-sub">Months & days</div>
        </div>
        <div class="kpi-card kpi-primary">
            <div class="kpi-label">Required Topup</div>
            <div class="kpi-value">{rounded_month_str}</div>
            <div class="kpi-sub">Rounded full months</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Structured Calculation Report
    if total_days_diff >= 0:
        rounding_note = f"+1 month added for {days_remaining} extra days" if days_remaining > 0 else "Exact month match (no buffer needed)"
        st.markdown(f"""
        <div class="report-box">
            <div class="report-header">
                <span>Calculation Summary</span>
                <span class="badge-compliant">Action Required</span>
            </div>
            <div class="report-row">
                <span class="r-label">Current Expiry Date</span>
                <span class="r-val">{input_date.strftime('%d-%b-%Y')}</span>
            </div>
            <div class="report-row">
                <span class="r-label">Target Benchmark ({duration_choice})</span>
                <span class="r-val">{target_date.strftime('%d-%b-%Y')}</span>
            </div>
            <div class="report-row">
                <span class="r-label">Exact Duration Gap</span>
                <span class="r-val">{months_remaining} Months, {days_remaining} Days ({total_days_diff} Days)</span>
            </div>
            <div class="report-row">
                <span class="r-label">Rounding Policy</span>
                <span class="r-val">{rounding_note}</span>
            </div>
            <div class="report-row">
                <span class="r-label"><strong>Final Topup Allocation</strong></span>
                <span class="r-val-highlight">{final_rounded_months} Full Months</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning(f"Current plan validity exceeds the {duration_choice} target date by {abs(total_days_diff)} days. No additional topup is required.")

    # Corporate Footer
    st.markdown("""
        <div class="corp-footer">
            <span>Internal Operations Tool</span>
            <span>Developed by <strong>Mratyunjay Brahmavanshi</strong></span>
        </div>
    """, unsafe_allow_html=True)