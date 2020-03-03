import numpy as np
from numpy import percentile
import pandas as pd
import csv, sys
import matplotlib.pyplot as plt



df_csv = pd.read_csv('totalskatt.csv', sep=';',names=['kommun','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'])
df_csv.set_index('kommun')

år = df_csv[['kommun', '2020']]
år.plot(title='År', kind='line')
plt.ylabel('antal')
plt.show()

