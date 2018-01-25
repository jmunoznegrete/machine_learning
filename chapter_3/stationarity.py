import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf
import matplotlib.pylab as plt
from matplotlib import rcParams

def evaluate_stationarity(timeseries, xtimeseries, t=30):
    """ evaluate_stationary takes as first argument the serie
    and the x-axis serie as the second one to be plotted correctly"""
    ## MODIFIED FROM ORIGINAL
    
    ## Determining rolling statistics
    rolmean = pd.rolling_mean(timeseries, t)
    rolstd = pd.rolling_std(timeseries, t)

    ## Perform Dickey-Fuller test

    print 'Results od Dickey-Fuller test'
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic',
            'p-value', '#Lags Used', 'Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print dfoutput


    ## Plot rolling statistics
    ## MODIFIED FROM ORIGINAL
    ## plt.plot called with x-axis series
    rcParams['figure.figsize'] = 15, 5
    orig = plt.plot(xtimeseries, timeseries, color = 'blue', label = 'Original')
    mean = plt.plot(xtimeseries, rolmean, color = 'red', label = 'Rolling Mean')
    std = plt.plot(xtimeseries, rolstd, color = 'black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    ##plt.show(block=False)

