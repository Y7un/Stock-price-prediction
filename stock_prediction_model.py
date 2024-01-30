# -*- coding: utf-8 -*-
"""Stock prediction model

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ne7Whz3b7ClwjiCdLXnx3C95Xcv84y8X
"""

from google.colab import files
uploaded = files.upload()

!pip install ta

import pandas as pd
import ta
import io

file_name = list(uploaded.keys())[0]

# Read the dataset into a  DataFrame
df = pd.read_csv(io.StringIO(uploaded[file_name].decode('utf-8')))

stock_data = df

stock_data.head()

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  from matplotlib import pyplot as plt
  import seaborn as sns
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Date']
  ys = series['Open']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = _df_9.sort_values('Date', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('Date')):
  _plot_series(series, series_name, i)
  fig.legend(title='Date', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Date')
_ = plt.ylabel('Open')

from matplotlib import pyplot as plt
_df_13['Open'].plot(kind='line', figsize=(8, 4), title='Open')
plt.gca().spines[['top', 'right']].set_visible(False)

from matplotlib import pyplot as plt
_df_3['Close'].plot(kind='hist', bins=20, title='Close')
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
_df_0['Open'].plot(kind='hist', bins=20, title='Open')
plt.gca().spines[['top', 'right',]].set_visible(False)

# Assuming 'stock_data' with columns 'Date', 'Close', 'High', 'Low'

# Convert 'Date' to datetime format
stock_data['Date'] = pd.to_datetime(stock_data['Date'])

# Calculate SMA and EMA
stock_data['SMA_10'] = ta.trend.sma_indicator(stock_data['Close'], window=10)
stock_data['EMA_10'] = ta.trend.ema_indicator(stock_data['Close'], window=10)

# Calculate RSI
stock_data['RSI'] = ta.momentum.RSIIndicator(stock_data['Close'], window=14).rsi()

# Calculate MACD
stock_data['MACD'] = ta.trend.MACD(stock_data['Close']).macd()
stock_data['Signal'] = ta.trend.MACD(stock_data['Close']).macd_signal()

# Calculate Bollinger Bands
stock_data['Upper_Band'], stock_data['Lower_Band'] = ta.volatility.bollinger_hband_indicator(stock_data['Close'], window=20), ta.volatility.bollinger_lband_indicator(stock_data['Close'], window=20)

# Calculate Stochastic Oscillator
stock_data['Stochastic_Oscillator'] = ta.momentum.StochasticOscillator(stock_data['High'], stock_data['Low'], stock_data['Close']).stoch()

# Print the updated DataFrame
print(stock_data)

import matplotlib.pyplot as plt

plt.plot(stock_data['Date'], stock_data['Close'])
plt.title('Stock Price Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.show()

from statsmodels.tsa.seasonal import seasonal_decompose

seasonal_period = 7

result = seasonal_decompose(stock_data['Close'], model='additive', period=seasonal_period)
result.plot()
plt.show()

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(stock_data['Close'], lags=20)
plt.title('Autocorrelation Function (ACF)')
plt.show()

plot_pacf(stock_data['Close'], lags=20)
plt.title('Partial Autocorrelation Function (PACF)')
plt.show()

from statsmodels.tsa.stattools import adfuller

result = adfuller(stock_data['Close'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])

from statsmodels.tsa.holtwinters import ExponentialSmoothing

seasonal_period = 14
short_term_steps = 10
model = ExponentialSmoothing(stock_data['High'], trend='add', seasonal='add', seasonal_periods=seasonal_period)
fitted_model = model.fit()
forecast = fitted_model.forecast(steps=short_term_steps)

print(stock_data)
print(forecast)

import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

features = stock_data[['Open', 'High', 'Low', 'Volume']]  # Update with relevant features
target = stock_data['Close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Random Forest Model
random_forest_model = RandomForestRegressor(n_estimators=100, random_state=42)
random_forest_model.fit(X_train, y_train)

# Gradient Boosting Model
gradient_boosting_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
gradient_boosting_model.fit(X_train, y_train)

# Predictions
rf_predictions = random_forest_model.predict(X_test)
gb_predictions = gradient_boosting_model.predict(X_test)

# Evaluate performance
rf_rmse = mean_squared_error(y_test, rf_predictions, squared=False)
gb_rmse = mean_squared_error(y_test, gb_predictions, squared=False)

print(f"Random Forest RMSE: {rf_rmse}")
print(f"Gradient Boosting RMSE: {gb_rmse}")

# Plot predictions vs. actual values for one of the models
plt.plot(y_test.index, y_test, label='Actual Close Prices')
plt.plot(y_test.index, gb_predictions, label='Gradient Boosting Predictions', linestyle='dashed')
plt.title('Gradient Boosting Model Predictions vs. Actual Close Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

stock_data['Date'] = pd.to_datetime(stock_data['Date'])

time_series = stock_data.set_index('Date')['Close']

plot_acf(time_series, lags=20)
plt.title('Autocorrelation Function (ACF)')
plt.show()

plot_pacf(time_series, lags=20)
plt.title('Partial Autocorrelation Function (PACF)')
plt.show()

# Determine ARIMA parameters (p, d, q)
# p: Order of the autoregressive part
# d: Degree of differencing
# q: Order of the moving average part

# For demonstration purposes, let's set p=1, d=1, q=1
p, d, q = 1, 1, 1

# Fit ARIMA model
arima_model = ARIMA(time_series, order=(p, d, q))
arima_results = arima_model.fit()

# Forecast short-term steps into the future
short_term_steps = 5
forecast = arima_results.forecast(steps=short_term_steps)

# Plot the original time series and the forecast
plt.plot(time_series.index, time_series, label='Original Time Series')
plt.plot(pd.date_range(time_series.index[-1], periods=short_term_steps+1, freq=time_series.index.freq)[1:], forecast, label='ARIMA Forecast', linestyle='dashed')
plt.title('ARIMA Short-Term Forecast')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split

features = stock_data[['Open', 'High', 'Low', 'Volume']]  # Update with relevant features
target = stock_data['Close']

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Display the shapes of the resulting sets
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

from sklearn.metrics import mean_squared_error

# Calculate RMSE
rf_rmse = mean_squared_error(y_test, rf_predictions, squared=False)
gb_rmse = mean_squared_error(y_test, gb_predictions, squared=False)

print(f"Random Forest RMSE: {rf_rmse}")
print(f"Gradient Boosting RMSE: {gb_rmse}")