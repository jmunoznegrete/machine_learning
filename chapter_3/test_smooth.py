from priceSerie import PriceSerie
from stationarity import evaluate_stationarity
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib import rcParams

StockPrice = PriceSerie('YAHOO')

date_tresh = datetime.strptime('2016-10-01', "%Y-%m-%d").date()
##print type(date_tresh)
##print type(StockPrice.get_list_data()[0][0])

dates = [x[0] for x in StockPrice.get_list_data()]
values = [x[1] for x in StockPrice.get_list_data()]
data = pd.DataFrame({'Close_Adj':values}, index = dates)


data_train = data[:date_tresh]
data_test = data[date_tresh:]

options = [" ", "1. Moving Avg(log)", "2. EMA (log)", 
        "3. Differencing 1st order",
        "4. Differencing 2nd order"]

for i in range(len(options)):
    print options[i]

option = int(raw_input("Choose an option:"))

print " "
if option<2 or option >len(options):
    option = 1
print options[option]
print " "

data_log = np.log(data_train['Close_Adj'])

if option==1:
    moving_avg = pd.rolling_mean(data_log, 15)

    data_log_moving_avg_diff = data_log - moving_avg
    data_log_moving_avg_diff.dropna(inplace=True)
    data_to_show = data_log_moving_avg_diff
elif option==2:
    expwighted_avg = pd.ewma(data_log, halflife=15)

    data_log_ewma_diff = data_log - expwighted_avg
    data_log_ewma_diff.dropna(inplace=True)
    data_to_show = data_log_ewma_diff
elif option==3:
    data_log_diff = data_log - data_log.shift()
    data_log_diff.dropna(inplace=True)
    data_to_show = data_log_diff
elif option==4:
    data_log_diff = data_log - data_log.shift()
    data_log_diff2 = data_log_diff - data_log_diff.shift()
    data_log_diff2.dropna(inplace=True)
    data_to_show = data_log_diff2


##plt.plot(data_log)
##plt.plot(moving_avg, color='red')
##plt.show()


evaluate_stationarity(
    data_to_show,
    data_to_show.index, 
    15)

