import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline 

class pandas_class():
	def __init__(self):
		pass
	
	def pandas_func(self):		
		df = pd.read_csv('data/btc-market-price.csv',header=None)# no columns hence header=Nnone
		print(df.head())

		#name the columns
		df.columns=["Timestamp","Price"]
		print(df.head())

		#check the shape
		print(df.shape)

		#see last 5 records
		df.tail(5)

		#print dtypes
		print("\n")
		print(df.dtypes)


		#hist of p
		p=df["Price"]
		print(p)

		plt.hist(df["Price"])
		plt.show()

		#change format of timestamp
		df['Timestamp']=pd.to_datetime(df['Timestamp'])
		ts=df["Timestamp"]
		print(df.head())

		#set Timestamp as index. records can be accessed by this index
		df.set_index('Timestamp', inplace=True)
		print(df.head())

		#access a record using timestamp
		print("\n")
		print(df.loc['2017-09-29'])



		#all the above in one line


		df = pd.read_csv(
			'data/btc-market-price.csv',
			header=None,
			names=['Timestamp', 'Price'],
			index_col=0,
			parse_dates=True
		)

		print(df.head())
		plt.plot(df.index, df["Price"])
		plt.show()

		#file 2
		df1=pd.read_csv("data/btc-eth-prices-original.csv", index_col=0)
		print df1.head()
		print(df1.loc['2017-04-02'])

		plt.hist(df1["Bitcoin"], histtype='barstacked')
		plt.show()
		
		df1.plot()
		plt.show()
		print(df1.head())
		df1.loc['2017-12-11':'2018-01-01'].plot(figsize=(12, 6))
		plt.show()
		
		df = pd.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],columns=['dogs', 'cats'])
        df.head()     
		


if __name__=="__main__":
	panda_obj=pandas_class()
	panda_obj.pandas_func()
