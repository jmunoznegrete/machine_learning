from priceSerie import PriceSerie
from stationarity import evaluate_stationarity
from datetime import datetime
import pandas as pd
import numpy as np

StockPrice = PriceSerie('YAHOO')

date_tresh = datetime.strptime('2016-10-01', "%Y-%m-%d").date()
##print type(date_tresh)
##print type(StockPrice.get_list_data()[0][0])

dates = [x[0] for x in StockPrice.get_list_data()]
values = [x[1] for x in StockPrice.get_list_data()]
data = pd.DataFrame({'Close_Adj':values}, index = dates)


data_train = data[:date_tresh]
data_test = data[date_tresh:]

options = [" ", "1. Price stationarity", "2. log(Price) stationarity",
            "3. sqrt(Price) stationarity", "4. cube(Price) stationarity"]

for i in range(len(options)):
    print options[i]

option = int(raw_input("Choose an option:"))

print " "
if option<2 or option >len(options)-1:
    option = 1
print options[option]
print " "

if option==2:
    data_plot = np.log(data_train['Close_Adj'])
elif option==3:
    data_plot = np.sqrt(data_train['Close_Adj'])
elif option==4:
    data_power = [3 for i in range(len(data_train['Close_Adj']))]
    data_plot = np.power(data_train['Close_Adj'], data_power)
else:
    data_plot = data_train['Close_Adj']

evaluate_stationarity(data_plot, data_train.index, 15)

