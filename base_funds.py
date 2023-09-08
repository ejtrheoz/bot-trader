import pandas as pd
from datetime import date
import time

def spx_dxy():
	df = pd.read_csv("https://data.nasdaq.com/api/v3/datasets/MULTPL/SP500_REAL_PRICE_MONTH.csv?api_key=_ceSKrfy_fUJnxHD3DN9")
	spx = float((float(df["Value"][0]) / float(df["Value"][1]))-1)*250

	date_time = date.today()
	end_date = str(int(time.mktime(date_time.timetuple())-86400))
	df = pd.read_csv("https://query1.finance.yahoo.com/v7/finance/download/DX-Y.NYB?period1=1637058105&period2="+end_date+"&interval=1d&events=history&includeAdjustedClose=true")

	dxy = ((float(df["Close"][0]) / float(df["Close"][1]))-1) * -600
	return (dxy + spx)/2
