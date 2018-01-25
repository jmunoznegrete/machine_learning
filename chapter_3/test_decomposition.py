from priceSerie import PriceSerie
from stationarity import evaluate_stationarity
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib import rcParams
from statsmodels.tsa.seasonal import seasonal_decompose

StockPrice = PriceSerie('YAHOO')

date_tresh = datetime.strptime('2016-10-01', "%Y-%m-%d").date()

dates = [x[0] for x in StockPrice.get_list_data()]
values = [x[1] for x in StockPrice.get_list_data()]
data = pd.DataFrame({'Close_Adj':values}, index = dates)


data_train = data[:date_tresh]
data_test = data[date_tresh:]

data_log = np.log(data_train['Close_Adj'])

decomposition = seasonal_decompose(list(data_log), freq=15)

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

plt.subplot(411)
plt.plot(data_log, label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(trend, label='Trends')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal, label='Seasonality')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residuals')
plt.legend(loc='best')
plt.tight_layout()
plt.show(block=False)

data_log_decompose = pd.Series(residual)
data_log_decompose.dropna(inplace=True)

data_to_show = data_log_decompose

evaluate_stationarity(
    data_to_show,
    data_to_show.index, 
    15)

