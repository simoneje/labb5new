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
år = df_csv[['2002','2003','2004', '2005', '2006','2020']]
kommun = df_csv['kommun']

år.plot(title='År 2000', kind='bar',)
# plt.hist(år, bins=kommun, edgecolor='black', log=True)
plt.ylabel('Total skatt')
plt.xlabel('Stockholms kommuner')
plt.tight_layout()
plt.show()

# text = open("skattregion.csv", "r")
# text = ''.join([i for i in text]) \
#     .replace(",", ".")
# x = open("skattregionnew.csv","w")
# x.writelines(text)
# x.close()


skatt_region = pd.read_csv('skattregionnew.csv', sep=';')
# df_csv.set_index('kommun')
reg_län = skatt_region['år']
reg_årtal = skatt_region['Upplands Väsby']


plt.plot(reg_län,reg_årtal,label='Stockholmslän år 2000-2020')
# plt.hist(år, bins=kommun, edgecolor='black', log=True)
plt.ylabel('Skatt i procentenheter')
plt.xlabel('Årtal')
plt.tight_layout()
plt.show()


# text = open("skattkommun.csv", "r")
# text = ''.join([i for i in text]) \
#     .replace(",", ".")
# x = open("skattkommunnew.csv","w")
# x.writelines(text)
# x.close()

skatt_kommun = pd.read_csv('skattkommunnew.csv', sep=';')
# df_csv.set_index('kommun')
kom_län = skatt_kommun['år']
kom_årtal = skatt_kommun[['Upplands Väsby','Vallentuna','Österåker','Värmdö','Järfälla','Ekerö','Huddinge','Botkyrka','Salem','Haninge','Tyresö','Upplands-Bro','Nykvarn','Täby','Danderyd','Sollentuna','Stockholm','Södertälje','Nacka','Sundbyberg','Solna','Lidingö','Vaxholm','Norrtälje','Sigtuna','Nynäshamn']]


plt.bar(kom_län,kom_årtal,label='Stockholmslän år 2000-2020')
# plt.hist(år, bins=kommun, edgecolor='black', log=True)
plt.ylabel('Skatt i procentenheter')
plt.xlabel('Årtal')
plt.tight_layout()
plt.show()

# text = open("genomsnittligskatt.csv", "r")
# text = ''.join([i for i in text]) \
#     .replace(",", ".")
# x = open("genosnittligskattnew.csv","w")
# x.writelines(text)
# x.close()

skatt_sthlm = pd.read_csv('genosnittligskattnew.csv', sep=';')
# df_csv.set_index('kommun')
län = skatt_sthlm[['Stockholms län']]
årtal = skatt_sthlm[['År']]


plt.plot(årtal,län,label='Stockholmslän år 2000-2020')
# plt.hist(år, bins=kommun, edgecolor='black', log=True)
plt.ylabel('Skatt i procentenheter')
plt.xlabel('Årtal')
plt.tight_layout()
plt.show()