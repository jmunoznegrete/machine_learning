from priceSerie import PriceSerie
from stationarity import evaluate_stationarity
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib import rcParams
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm

StockPrice = PriceSerie('YAHOO')

date_tresh = datetime.strptime('2016-10-01', "%Y-%m-%d").date()

dates = [x[0] for x in StockPrice.get_list_data()]
values = [x[1] for x in StockPrice.get_list_data()]
data = pd.DataFrame({'Close_Adj':values}, index = dates)


data_train = data[:date_tresh]
data_test = data[date_tresh:]

data_log = np.log(data_train['Close_Adj'])
moving_avg = pd.rolling_mean(data_log, 15)

data_log_diff = data_log - data_log.shift()
##data_log_diff = data_log - moving_avg

data_log_diff.dropna(inplace=True)


print sm.stats.durbin_watson(data_log_diff)

ax1 = plt.subplot(211)
fig  = sm.graphics.tsa.plot_acf(data_log_diff.squeeze(), lags=40, ax=ax1)
ax2 = plt.subplot(212)
fig  = sm.graphics.tsa.plot_pacf(data_log_diff, lags=40, ax=ax2)
plt.show()
