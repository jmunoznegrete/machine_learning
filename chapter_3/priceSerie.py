from xlrd import open_workbook
from datetime import datetime
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

class PriceSerie(object):

    def __init__(self, share):
        self.filename = share + '.xlsx'
        self.list_data = []
        self.loadfile(self.filename)

    def loadfile(self, filename):
        wb = open_workbook(filename)
        i = 0
        for s in wb.sheets():
            #print 'Sheet:',s.name
            self.list_data = []
            for row in range(s.nrows):
        
                if i==0 or i==1:
                    i = i+1
                    continue
                col_value = []
                fecha = date.fromordinal(int(s.cell(row, 0).value) +1900*365+94)
                cotizacion = s.cell(row, 1).value
                col_value.append(fecha)
                col_value.append(cotizacion)
        
                self.list_data.append(col_value)
        
            i = i+1

    def get_list_data(self):
        return self.list_data


##for row in range(len(list_data)):
##    print list_data[row]


if __name__ == 'main':

    StockPrice = PriceSerie('YAHOO')
    
    date_tresh = datetime.strptime('2016-10-01', "%Y-%m-%d").date()
    print type(date_tresh)
    print type(StockPrice.get_list_data()[0][0])
    
    dates = [x[0] for x in StockPrice.get_list_data()]
    values = [x[1] for x in StockPrice.get_list_data()]
    data = pd.DataFrame({'Close_Adj':values}, index = dates)
    
    
    data_train = data[:date_tresh]
    data_test = data[date_tresh:]
    
    
    rcParams['figure.figsize'] = 15, 5
    ## MODIFIED FROM ORIGINAL
    ## data_train is used as y values. x-serie must hav a y-serie value
    plt.plot(data_train.index, data_train['Close_Adj'])
    plt.xlabel('Year')
    plt.ylabel('Adjusted Closing Rate')
    plt.title('Yahoo Ajusted Closing Rate - Year 2016')
    
    plt.show()
