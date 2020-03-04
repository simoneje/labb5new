import numpy as np
from numpy import percentile
import pandas as pd
import csv, sys
import matplotlib.pyplot as plt

# text = open("totalskatt.csv", "r")
# text = ''.join([i for i in text]) \
#     .replace(",", ".")
# x = open("totalskattnew.csv","w")
# x.writelines(text)
# x.close()
# ,names=['kommun','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
df_csv = pd.read_csv('totalskattnew.csv', sep=';')
# df_csv.set_index('kommun')
år = df_csv[['2000','2005','2010','2015','2020']]
kommun = df_csv['kommun']

år.plot(title='År 2000', kind='bar',)
# plt.hist(år, bins=kommun, edgecolor='black', log=True)
plt.ylabel('Total skatt')
plt.xlabel('Stockholms kommuner')
plt.tight_layout()
plt.show()

