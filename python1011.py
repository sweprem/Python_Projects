import numpy as np
import pandas as pd
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
print(ser.value_counts)
ser[~ser.isin(ser.value_counts().index[0:2])] = 'other'
print(ser)


ser = pd.Series(np.random.random(20))
print(ser.head())
op=pd.qcut(ser,q=[0,.1,.2,.3,.4,.5] ,labels=["one","two","three","four","five"])
print(op)


ser = pd.Series(np.random.randint(1, 10, 7))
vv=np.argwhere(ser%5==0)
print(vv)

ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])
ser.map(lambda x: parse("04"+x))
