import streamlit as st
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

# 1. Page Config
st.set_page_config(
    page_title="PAPA CALENDAR",
    page_icon="👨🏻‍🦰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Custom Executive Light & Sleek Dashboard CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Subtle Rich Minimal Background */
    .stApp {
        background: #F8FAFC;
        color: #0F172A;
    }

    /* Hide Top Header Toolbar & Footer */
    header[data-testid="stHeader"], #MainMenu, footer {
        display: none !important;
    }

    /* Executive Clean Title */
    h1 {
        color: #0F172A !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
        text-align: center;
        font-size: 1.75rem !important;
        margin-bottom: 4px !important;
    }

    /* Classic Subtitle / Creator Badge */
    .creator-subtitle {
        text-align: center;
        font-size: 0.78rem;
        font-weight: 700;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 24px;
    }

    /* Premium Input Styling */
    label {
        color: #64748B !important;
        font-size: 0.75rem !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }

    div[data-baseweb="input"] {
        border-radius: 10px !important;
        border: 1px solid #E2E8F0 !important;
        background: #FFFFFF !important;
        box-shadow: 0px 1px 3px rgba(15, 23, 42, 0.05) !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
    }
    
    div[data-baseweb="input"] input {
        color: #0F172A !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #0F172A !important;
        box-shadow: 0 0 0 3px rgba(15, 23, 42, 0.08) !important;
    }

    /* Metric Cards Grid Layout */
    .metric-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(135px, 1fr));
        gap: 12px;
        margin: 20px 0;
    }

    /* Executive Classic Card Style */
    .metric-card {
        padding: 20px 14px;
        border-radius: 12px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }

    /* Subtle & Professional Hover */
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px -4px rgba(0, 0, 0, 0.08);
        border-color: #CBD5E1;
    }

    /* Distinct Executive Card Colors */
    .card-till-then { border-top: 3px solid #2563EB; }
    .card-till-then .metric-title { color: #2563EB; }
    .card-till-then .metric-val { color: #1E3A8A; }

    .card-total-days { border-top: 3px solid #D97706; }
    .card-total-days .metric-title { color: #D97706; }
    .card-total-days .metric-val { color: #78350F; }

    .card-topup-month { border-top: 3px solid #059669; }
    .card-topup-month .metric-title { color: #059669; }
    .card-topup-month .metric-val { color: #064E3B; }

    /* Rich Obsidian Card (Main Highlight) */
    .card-rounded-month {
        background: #0F172A !important;
        border: 1px solid #1E293B !important;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15) !important;
    }
    .card-rounded-month .metric-title { color: #94A3B8 !important; }
    .card-rounded-month .metric-val { color: #F8FAFC !important; font-size: 1.25rem !important; }

    .card-rounded-month:hover {
        border-color: #334155 !important;
        box-shadow: 0 10px 24px -4px rgba(15, 23, 42, 0.25) !important;
    }

    .metric-title {
        font-size: 0.68rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 8px;
    }

    .metric-val {
        font-size: 1.15rem;
        font-weight: 800;
        letter-spacing: -0.3px;
    }

    /* Result Box (Clean Executive Slate) */
    .stSuccess {
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-left: 4px solid #0F172A !important;
        border-radius: 10px !important;
        color: #334155 !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
        padding: 16px !important;
    }

    /* Crisp Minimal Button */
    .stButton>button {
        width: 100%;
        border-radius: 10px !important;
        background: #0F172A !important;
        color: #FFFFFF !important;
        border: 1px solid #0F172A !important;
        padding: 10px 16px !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
    }

    .stButton>button:hover {
        background: #1E293B !important;
        border-color: #1E293B !important;
        color: #FFFFFF !important;
    }

    .stButton>button:active {
        transform: scale(0.99) !important;
    }

    /* Minimal Tagline Badge */
    .guru-line {
        text-align: center;
        font-size: 0.88rem;
        font-weight: 700;
        color: #475569;
        margin-top: 24px;
        padding: 10px;
        border-radius: 8px;
        background: #F1F5F9;
        border: 1px solid #E2E8F0;
        letter-spacing: 0.3px;
    }

    /* Warning Dialog Box */
    .popup-box {
        background: #FFFFFF;
        border: 1px solid #FCA5A5;
        border-top: 4px solid #DC2626;
        padding: 18px;
        border-radius: 8px;
        text-align: center;
    }

    .popup-header {
        font-size: 1.15rem;
        font-weight: 800;
        color: #991B1B;
        margin-bottom: 6px;
    }

    .popup-sub {
        font-size: 0.85rem;
        font-weight: 500;
        color: #4B5563;
    }

    /* MONEY RAIN ANIMATION STYLES */
    @keyframes fall {
        0% {
            top: -10%;
            transform: translateX(0) rotate(0deg);
            opacity: 1;
        }
        100% {
            top: 100%;
            transform: translateX(100px) rotate(360deg);
            opacity: 0;
        }
    }

    .money-particle {
        position: fixed;
        top: -10%;
        font-size: 2.2rem;
        z-index: 99999;
        pointer-events: none;
        animation: fall 3s linear forwards;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Native Streamlit Popup Dialog
@st.dialog("🚨 Warning!")
def show_error_popup():
    st.markdown("""
        <div class="popup-box">
            <div class="popup-header">🦁 वाह मेरे शेर! कर दिया गलत टॉपअप! 👏🤡</div>
            <div class="popup-sub">"अबे DATE सही डालो भाई!" </div>
        </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Sorry 🙏🏻 (close)", use_container_width=True):
        st.rerun()

# Main Title
st.title("🪙 Topup Calendar")

# 🌟 CLASSIC NAME BADGE (OPTION 1 - Top Subtitle)
# अपना नाम नीचे बदलें:
st.markdown('<div class="creator-subtitle">✦ 💡 Avoid Salary Cuts With Smart Calendar Tracking ✦</div>', unsafe_allow_html=True)

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
    st.error("🚨 Please paste date carefully 100% SALARY CUT CHANCE AVAILABLE ")

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
        
        # 💸 MONEY SHOWER BUTTON
        if st.button("💸 Shower Money"):
            st.markdown("""
                <script>
                const emojis = ['💵', '💸', '💸', '💶', '🪙'];
                for (let i = 0; i < 40; i++) {
                    let particle = document.createElement('div');
                    particle.className = 'money-particle';
                    particle.innerText = emojis[Math.floor(Math.random() * emojis.length)];
                    particle.style.left = Math.random() * 95 + 'vw';
                    particle.style.animationDuration = (Math.random() * 2 + 1.5) + 's';
                    particle.style.animationDelay = (Math.random() * 0.8) + 's';
                    document.body.appendChild(particle);
                    setTimeout(() => particle.remove(), 4000);
                }
                </script>
            """, unsafe_allow_html=True)

    else:
        st.warning(f"⚠️ Selected date is **{abs(total_days_diff)} days** beyond target date!")

    # 🌟 CLASSIC FOOTER SIGNATURE (OPTION 2 - Bottom Footer)
    st.markdown('<div class="guru-line">| Crafted by <b>Mratyunjay Brahmavanshi</b></div>', unsafe_allow_html=True)
