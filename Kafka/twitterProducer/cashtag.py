# -*- coding: utf-8 -*-
import csv
# __all__ = ['cashtag', 'cashtagSet']

def cashtag(Type):

    # map the inputs to the function blocks

    flag = 0
    # define the function blocks
    if Type=="DOW30":
        FILE_NAME = '../stockData/nasdaq100.csv'
    elif Type=="NASDAQ100":
        FILE_NAME = '../stockData/nasdaq100.csv'
    elif Type== "NYSE100":
        FILE_NAME = '../stockData/nyse100.csv'
    elif Type== "SP500":
        FILE_NAME = '../stockData/SP500.csv'
    elif Type== "NASDAQ_COMPOSITE":
        FILE_NAME = '../stockData/NASDAQComposite.csv'
    elif Type== "NYSE_COMPOSITE":
        FILE_NAME = '../stockData/NYSEComposite.csv'
    elif Type=="COMPANIES":
	FILE_NAME = '../stockData/companies.csv'
    elif Type== "ALL":
        FILE_NAME = '../stockData/allStocks.csv'
        flag = 1
    else:
        raise Exception("unknown stock type")


 #   options.get(Type,errhandler)()
    with open(FILE_NAME,'rU') as file1:
        if flag==1:
            dat = csv.reader(file1,  dialect=csv.excel_tab, delimiter=',')
            idx = 1
        else:
            dat = csv.reader(file1, dialect=csv.excel_tab, delimiter=',')
            next(dat, None)
            idx = 0


        filterTwitter = ''
        counter = 0
        for line in dat:
            if counter == 0:
                filterTwitter = '$'+line[idx]
                counter+=1
            else:
                filterTwitter = filterTwitter+',$'+line[idx]

        return filterTwitter