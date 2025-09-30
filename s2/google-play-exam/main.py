import pandas as pd
import numpy as np
import seaborn as scs
import matplotlib.pyplot as plt
 
data_frame=pd.read_csv("data\googleplaystore.csv")

# print(data_frame)

(rows,columns)=data_frame.shape

print(f"rows= {rows}")
print(f"columns= {columns}")

print(f"\n\n{data_frame.info()}")

print(f"\n\n{data_frame.describe()}")
print(f"missing value=\n")
print(data_frame.isnull().sum())





# scs.barplot(data=data_frame)