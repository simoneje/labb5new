import numpy as np
from numpy import percentile
import pandas as pd
import csv, sys
import matplotlib.pyplot as plt

#HÄR ÄNDRAR JAG ALLA DECIMALER TILL PUNKTER SÅ NUMERIC BLIR KORREKT
# text = open("totalskatt.csv", "r")
# text = ''.join([i for i in text]) \
#     .replace(",", ".")
# x = open("totalskattnew.csv","w")
# x.writelines(text)
# x.close()
# ,names=['kommun','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']

df_csv = pd.read_csv('totalskattnew.csv', sep=';')
# df_csv.set_index('kommun')
kommun = df_csv[['Upplands Väsby','Vallentuna','Österåker','Värmdö','Järfälla','Ekerö','Huddinge','Botkyrka','Salem','Haninge','Tyresö','Upplands-Bro','Nykvarn','Täby','Danderyd','Sollentuna','Stockholm','Södertälje','Nacka','Sundbyberg','Solna','Lidingö','Vaxholm','Norrtälje','Sigtuna','Nynäshamn']]
år = df_csv['år']

plt.plot(år,kommun,label='År 2000')
# plt.hist(år, bins=kommun, edgecolor='black', log=True)
plt.ylabel('Total skatt i procentenheter')
plt.xlabel('Årtal')
plt.title('Skatten genom åren')
plt.legend(kommun, loc='upper right')
plt.show()


procentÅr = percentile(kommun, [25, 50, 75])
print(f"median-skatten för åren är : ",(procentÅr),"procentenheter")
billigaste = percentile(kommun, [0])
dyraste = percentile(kommun, [100])
print(f"Billigaste skatten låg på", billigaste, "procentenheter")
print(f"Dyraste skatten låg på", dyraste, "procentenheter")


# text = open("genomsnittligskatt.csv", "r")
# text = ''.join([i for i in text]) \
#     .replace(",", ".")
# x = open("genosnittligskattnew.csv","w")
# x.writelines(text)
# x.close()

skatt_sthlm = pd.read_csv('genosnittligskattnew.csv', sep=';')
län = skatt_sthlm[['Stockholms län']]
årtal = skatt_sthlm[['År']]


plt.plot(årtal,län,label='Stockholmslän år 2000-2020')
plt.ylabel('Skatt i procentenheter')
plt.xlabel('Årtal')
plt.legend(län)
plt.tight_layout()
plt.show()


# text = open("skattregion.csv", "r")
# text = ''.join([i for i in text]) \
#     .replace(",", ".")
# x = open("skattregionnew.csv","w")
# x.writelines(text)
# x.close()

#REGIONALA SKATTEN
skatt_region = pd.read_csv('skattregionnew.csv', sep=';')
reg_år = skatt_region['år']
reg_län = skatt_region['Upplands Väsby']


plt.plot(reg_år,reg_län,label='Stockholmslän år 2000-2020')
plt.ylabel('Skatt i procentenheter')
plt.xlabel('Årtal')
plt.title('Regionala skatten genom åren')
plt.tight_layout()
plt.show()

plt.hist


# text = open("skattkommun.csv", "r")
# text = ''.join([i for i in text]) \
#     .replace(",", ".")
# x = open("skattkommunnew.csv","w")
# x.writelines(text)
# x.close()

skatt_kommun = pd.read_csv('skattkommunnew.csv', sep=';')
kom_årtal = skatt_kommun['år']
kom_län = skatt_kommun[['Upplands Väsby','Vallentuna','Österåker','Värmdö','Järfälla','Ekerö','Huddinge','Botkyrka','Salem','Haninge','Tyresö','Upplands-Bro','Nykvarn','Täby','Danderyd','Sollentuna','Stockholm','Södertälje','Nacka','Sundbyberg','Solna','Lidingö','Vaxholm','Norrtälje','Sigtuna','Nynäshamn']]


plt.plot(kom_årtal,kom_län,label='Stockholmslän år 2000-2020')
plt.ylabel('Skatt i procentenheter')
plt.xlabel('Årtal')
plt.title('Kommunala skatterna')
plt.legend(kom_län)
plt.tight_layout()
plt.show()


plt.scatter(reg_år, skatt_kommun['Solna'], linewidth=1, alpha=0.75,color='darkorange')
plt.scatter(reg_år, skatt_kommun['Nynäshamn'], linewidth=1, alpha=0.75,color='aquamarine')
plt.scatter(reg_år, skatt_kommun['Lidingö'], linewidth=1, alpha=0.75,color='navy')
plt.scatter(reg_år, skatt_kommun['Vaxholm'], linewidth=1, alpha=0.75,color='steelblue')
plt.scatter(reg_år, skatt_kommun['Norrtälje'], linewidth=1, alpha=0.75,color='deeppink')
plt.scatter(reg_år, skatt_kommun['Sigtuna'], linewidth=1, alpha=0.75,color='crimson')
plt.scatter(reg_år, skatt_kommun['Vallentuna'], linewidth=1, alpha=0.75,color='b')
plt.scatter(reg_år, skatt_kommun['Österåker'], linewidth=1, alpha=0.75,color='r')
plt.scatter(reg_år, skatt_kommun['Värmdö'], linewidth=1, alpha=0.75,color='silver')
plt.scatter(reg_år, skatt_kommun['Järfälla'], linewidth=1, alpha=0.75,color='chocolate')
plt.scatter(reg_år, skatt_kommun['Ekerö'], linewidth=1, alpha=0.75,color='orange')
plt.scatter(reg_år, skatt_kommun['Huddinge'], linewidth=1, alpha=0.75,color='olive')
plt.scatter(reg_år, skatt_kommun['Botkyrka'], linewidth=1, alpha=0.75,color='lime')
plt.scatter(reg_år, skatt_kommun['Salem'], linewidth=1, alpha=0.75,color='coral')
plt.scatter(reg_år, skatt_kommun['Haninge'], linewidth=1, alpha=0.75,color='lightcoral')
plt.scatter(reg_år, skatt_kommun['Tyresö'], linewidth=1, alpha=0.75,color='gold')
plt.scatter(reg_år, skatt_kommun['Upplands-Bro'], linewidth=1, alpha=0.75,color='gray')
plt.scatter(reg_år, skatt_kommun['Nykvarn'], linewidth=1, alpha=0.75,color='skyblue')
plt.scatter(reg_år, skatt_kommun['Täby'], linewidth=1, alpha=0.75,color='darkcyan')
plt.scatter(reg_år, skatt_kommun['Danderyd'], linewidth=1, alpha=0.75,color='lightseagreen')
plt.scatter(reg_år, skatt_kommun['Sollentuna'], linewidth=1, alpha=0.75,color='pink')
plt.scatter(reg_år, skatt_kommun['Stockholm'], linewidth=1, alpha=0.75,color='palegreen')
plt.scatter(reg_år, skatt_kommun['Södertälje'], linewidth=1, alpha=0.75,color='violet')
plt.scatter(reg_år, skatt_kommun['Nacka'], linewidth=1, alpha=0.75,color='purple')
plt.scatter(reg_år, skatt_kommun['Sundbyberg'], linewidth=1, alpha=0.75,color='cyan')
plt.scatter(reg_år, skatt_kommun['Upplands Väsby'], linewidth=1, alpha=0.75,color='g')


plt.scatter(reg_år, reg_län, linewidth=1, alpha=0.75,color='black')
plt.xlabel('Svart = regionalskatt // Färg = kommunalskatt')
plt.ylabel('Skatt i procentenheter')
plt.show()


