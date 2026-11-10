   import yfinance as yf
   import streamlit as st

   st.title("Microsoft (MSFT) Sharpe Ratio")

   ticker = "MSFT"
   rf_monthly = 0.0025  # 0.25% per month

   # 5 years of monthly data
   data = yf.Ticker(ticker).history(period="5y", interval="1mo")

   if not data.empty:
       monthly_returns = data["Close"].pct_change().dropna()
       excess_returns = monthly_returns - rf_monthly

       sharpe = excess_returns.mean() / monthly_returns.std()

       st.metric(label="Monthly Sharpe Ratio (5 years)", value=f"{sharpe:.3f}")
   else:
       st.error("No data found for MSFT.")
