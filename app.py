import streamlit as st
import pandas as pd

st.set_page_config(page_title="Funded Guard 2026", layout="wide")

st.title("🛡️ Metal Strategy Control Center")

# --- Sidebar: Real-time Account Stats ---
st.sidebar.header("Funded Account Status")
# In a real app, these values would come from the API we built
balance = st.sidebar.metric("Current Balance", "$100,000", "+$250")
drawdown = st.sidebar.metric("Daily Drawdown", "0.45%", "-$450", delta_color="inverse")

# --- Main Controls ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Strategy Status")
    trading_active = st.toggle("Activate Metal Bot", value=False)
    if trading_active:
        st.success("BOT ACTIVE: Scanning XAU/USD & XAG/USD")
    else:
        st.warning("BOT PAUSED: Manual Control Only")

with col2:
    st.subheader("Emergency Tools")
    if st.button("🚨 KILL SWITCH: CLOSE ALL TRADES", use_container_width=True):
        st.error("Closing all open positions across XAU/XAG...")

# --- Strategy Settings ---
st.divider()
st.subheader("Risk Settings (1:3 RR Optimized)")
risk_per_trade = st.select_slider("Risk per Trade (%)", options=[0.25, 0.5, 1.0, 2.0], value=0.5)
st.info(f"Bot will automatically calculate lot sizes to risk exactly {risk_per_trade}%")
