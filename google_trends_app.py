import streamlit as st
from pytrends.request import TrendReq
import datetime
from pytz import timezone

# Function to fetch Google Trends
def get_google_trends():
    pytrends = TrendReq()
    try:
        pytrends.build_payload(kw_list=["trending"], geo='US')
        trends = pytrends.trending_searches(pn='united_states')
        return trends.head(10).values.flatten().tolist()
    except Exception as e:
        return [f"Error fetching trends: {e}"]

# Function to get the current time in Eastern Time
def get_current_time():
    eastern_tz = timezone("America/New_York")
    current_time = datetime.datetime.now(eastern_tz)
    return current_time.strftime("%A, %I:%M %p EST")

# Streamlit App
st.title("Google Trends Fetcher")
st.write(f"Trends fetched at: {get_current_time()}")

if st.button("Fetch Trends"):
    st.write("Fetching latest Google Trends...")
    trends = get_google_trends()
    for idx, trend in enumerate(trends, start=1):
        st.write(f"{idx}. {trend}")
