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
from plotly_figure import plotly_table, Moving_average, Moving_average_forecast

st.set_page_config(
    page_title="Stock Prediction",
    page_icon="chart_with_downward_trend",
    layout="wide"
)

st.title("Stock Prediction")

col1, col2, col3 = st.columns(3)
with col1:
    ticker = st.text_input("Stock Ticker", "AAPL")

rmse = 0

st.subheader(f"Predicting Next 30 Days Close Price for {ticker}")

try:
    close_price = get_data(ticker)
    rolling_price = get_rolling_mean(close_price)

    differncing_order = get_differencing_order(rolling_price)
    scaled_data, scaler = scaling(rolling_price)
    rmse = evaluate_model(scaled_data, differncing_order)

    st.write(f"Model RMSE Score: **{rmse}**")

    forecast = get_forecast(scaled_data, differncing_order)
    forecast['Close'] = inverse_scaling(scaler, forecast['Close'])

    st.write("Forecast Data (Next 30 Days)")
    fig_tail = plotly_table(forecast.sort_index(ascending=True).round(3))
    fig_tail.update_layout()
    st.plotly_chart(fig_tail, use_container_width=True)

    forecast = pd.concat([rolling_price, forecast])
    st.plotly_chart(Moving_average_forecast(forecast.iloc[150:]), use_container_width=True)
except Exception as e:
    st.error(f"Error: {e}")
