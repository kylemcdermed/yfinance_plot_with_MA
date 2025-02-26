import yfinance as yf
import mplfinance as mpf
import matplotlib.pyplot as plt

# Define futures ticker symbols
futures_tickers = ["NQ=F", "ZN=F", "ZC=F", "CC=F"]

# Create subplots with 1 Axes per contract (only price chart, no volume)
fig, axes = plt.subplots(len(futures_tickers), 1, figsize=(12, 5 * len(futures_tickers)))

# Ensure axes are iterable even if only one future is plotted
if len(futures_tickers) == 1:
    axes = [axes]

# Set background color
fig.patch.set_facecolor('#cfe2f3')  # Light blue-grey background color

# Fetch and plot each contract
for i, (ax, ticker) in enumerate(zip(axes, futures_tickers)):
    data = yf.Ticker(ticker).history(period="7mo", interval="1d")
    
    if not data.empty:
        # Remove unnecessary columns for mplfinance
        data = data[['Open', 'High', 'Low', 'Close', 'Volume']]  # Only required columns

        # Set the custom style for candlesticks (bearish black, bullish grey)
        market_colors = mpf.make_marketcolors(up='grey', down='black', inherit=True)
        custom_style = mpf.make_mpf_style(marketcolors=market_colors, base_mpf_style="charles", rc={'axes.facecolor': '#cfe2f3'})

        # Plot candlestick chart along with the 14-day moving average (mav=14)
        mpf.plot(data, type="candle", style=custom_style, ax=ax, ylabel="Price (USD)", show_nontrading=False, mav=14)

        # Set title for each subplot (on the left axis)
        ax.set_title(f"{ticker} Futures - Price & 14-Day MA")

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
