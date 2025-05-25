import streamlit as st
import pandas as pd
from utils.main import (
    get_data,
    get_rolling_mean,
    get_differencing_order,
    scaling,
    evaluate_model, 
    get_forecast,
    inverse_scaling
)
from plotly_figure import plotly_table, Moving_average_forecast

# Streamlit page config
st.set_page_config(
    page_title="Stock Prediction",
    page_icon="📉",
    layout="wide"
)

st.title("📈 Stock Prediction Dashboard")

# Input: Stock Ticker
ticker = st.text_input("Enter Stock Ticker (e.g. AAPL)", value="AAPL")

# Display prediction header
st.subheader(f"Forecasting Next 30 Days Closing Prices for **{ticker}**")

rmse = 0

try:
    with st.spinner("📦 Fetching stock data..."):
        close_price = get_data(ticker)

    with st.spinner("🔁 Applying rolling mean..."):
        rolling_price = get_rolling_mean(close_price)

    with st.spinner("🔍 Identifying differencing order..."):
        differencing_order = get_differencing_order(rolling_price)

    with st.spinner("📐 Scaling data..."):
        scaled_data, scaler = scaling(rolling_price)

    with st.spinner("📊 Evaluating SARIMA model..."):
        rmse = evaluate_model(scaled_data, differencing_order)
        st.success(f"Model RMSE Score: **{rmse:.4f}**")

    with st.spinner("📈 Forecasting next 30 days..."):
        forecast = get_forecast(scaled_data, differencing_order)
        forecast['Close'] = inverse_scaling(scaler, forecast['Close'])

    # Display forecast
    st.markdown("### 📅 Forecast Table")
    fig_table = plotly_table(forecast.sort_index().round(3))
    st.plotly_chart(fig_table, use_container_width=True)

    # Plot original + forecast
    forecast_full = pd.concat([rolling_price, forecast])
    st.markdown("### 🔮 Forecast Visualization")
    st.plotly_chart(Moving_average_forecast(forecast_full.iloc[150:]), use_container_width=True)

except Exception as e:
    st.error(f"⚠️ An error occurred: {e}")
