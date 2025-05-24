import streamlit as st

st.set_page_config(
    page_title="Trading App", 
    page_icon="📉",
    layout="wide"
)

st.image("app.png")

st.title("Trading Guide App")
st.header("We provide the greatest platform for you to collect all information prior to investing in stocks")
st.image("app.png")

st.markdown("## We provide the following services")

st.markdown("### :one: Stock Information")
st.write("Through this information, you can see all details about stocks, including historical data, key performance metrics, and market trends.")

st.markdown("### :two: Stock Prediction")
st.write("You can explore predicted closing prices for the next 30 days based on historical stock data and advanced forecasting models.")

st.markdown("### :three: CAPM Return")
st.write("Discover how the Capital Asset Pricing Model (CAPM) calculates the expected return of different stock assets based on their risk.")

st.markdown("### :four: CAPM Beta")
st.write("Calculates Beta and Expected Return for individual stocks, helping you understand their volatility relative to the market.")

st.markdown("---")
st.markdown("💬 *For further details, please contact our support team.*")
