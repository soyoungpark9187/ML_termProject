# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 14:16:16 2019

@author: 김진겸
"""
import warnings
warnings.filterwarnings(action="ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
original=pd.read_csv("AFSNT.CSV",encoding='euc_kr')
print(original.head())

print(original["SDT_DY"].value_counts())

elements,count=np.unique(original["SDT_DY"],return_counts=True)
print(elements)
elements=["5","4","3","1","7","6","2"]
plt.bar(elements,count)
plt.show()

elements,count=np.unique(original["SDT_MM"],return_counts=True)
print(elements)
print(original["SDT_MM"].value_counts())
plt.bar(elements,count)
plt.title("2017~2019 number of flight")
plt.show()

month=original[["SDT_MM","SDT_YY"]]
month=month[month["SDT_YY"]==2018]

print(month["SDT_MM"].value_counts())
elements,count=np.unique(month["SDT_MM"],return_counts=True)
print(elements)
plt.bar(elements,count)
plt.title("2018 number of flight")
plt.show()


"""

dly=original[original["DLY"]=="Y"]

print(dly)
elements,count=np.unique(dly["SDT_MM"],return_counts=True)
plt.bar(elements,count)
plt.title("2017~2019 month delay")
plt.show()

dly17=dly[dly["SDT_YY"]==2017]
elements,count=np.unique(dly17["SDT_MM"],return_counts=True)
plt.bar(elements,count)
plt.title("2017 month delay")
plt.show()

dly18=dly[dly["SDT_YY"]==2018]
elements,count=np.unique(dly18["SDT_MM"],return_counts=True)
plt.bar(elements,count)
plt.title("2018 month delay")
plt.show()


dly19=dly[dly["SDT_YY"]==2019]
elements,count=np.unique(dly19["SDT_MM"],return_counts=True)
plt.bar(elements,count)
plt.title("2019 month delay")

plt.show()


year17=original[original["SDT_YY"]==2017]
year18=original[original["SDT_YY"]==2018]
year19=original[original["SDT_YY"]==2019]

reg=year17["REG"].value_counts()
dly17=year17[year17["DLY"]=="Y"]
year17=year17[["REG","DLY"]]
dly17=dly17[["REG","DLY"]]
dly=dly17["REG"].value_counts()
year17=year17.fillna("")
dly17=dly17.fillna("")


elements,count=np.unique(year17["REG"],return_counts=True)
reg=year17["REG"].value_counts()
dly=dly17["REG"].value_counts()
print(reg)
print(dly)

reg_dly=pd.merge(reg,dly,left_index=True,right_index=True,how="inner")
print(reg_dly)
reg_dlyrate=reg_dly["REG_y"]/reg_dly["REG_x"]
reg_dlyrate=pd.DataFrame({"rate":reg_dlyrate})

reg_dly=pd.merge(reg_dly,reg_dlyrate,left_index=True,right_index=True,how="inner")
reg_dly=reg_dly.sort_values(["rate"])
print(reg_dly)

"""
irrN=original[original["IRR"]=="N"]
irrY=original[original["IRR"]=="Y"]


irrN=irrN[["IRR","DLY"]].fillna("")
irrY=irrY[["IRR","DLY"]].fillna("")
print(len(irrN))
print(len(irrY))

print("regular")
print(irrN["DLY"].value_counts())
print("non-regular")
print(irrY["DLY"].value_counts())

print(irrN["DLY"].value_counts()["Y"]/len(irrN))
print(irrY["DLY"].value_counts()["Y"]/len(irrY))