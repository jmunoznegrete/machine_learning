Python machine learning Case Studies

Examples from Danish Haaron book. Some refactoring has being done in order to fix some small bugs and for better code reuse.

Additionally, data source has been changed due to libraries are deprecated. Googlefinance function has been used to retrieve excel file format.

Files at this time:
* priceSerie.py: to initialize source data object
* stationary.py: to hold the function doing the Dickey-Fuller test
* test_stationarity.py:  basic transformations to the source data
* test_smooth.py: Moving average and Exponential Moving Average are tested lo look for stationary
* test_decomposition.py: in trend + stationary + residuals

All of them are plotted.
