import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="Date Calculator", page_icon="📅")

st.title("📅 Date & Month Calculator")

today = date.today()
two_years_later = today + relativedelta(years=2)

st.info(f"Today: {today.strftime('%d-%b-%Y')} | 2 Years Later: {two_years_later.strftime('%d-%b-%Y')}")
st.divider()

input_date = st.date_input("Select Input Date:", value=date(2027, 7, 16))

if input_date:
    total_days_diff = (two_years_later - input_date).days
    diff = relativedelta(two_years_later, input_date)
    months_remaining = diff.years * 12 + diff.months
    days_remaining = diff.days

    st.subheader("📊 Result:")
    col1, col2, col3 = st.columns(3)
    col1.metric("Target Date", two_years_later.strftime("%d-%b-%Y"))
    col2.metric("Total Days Left", f"{total_days_diff} Days")
    col3.metric("Pending Time", f"{months_remaining} M, {days_remaining} D")
