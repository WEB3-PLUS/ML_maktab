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

# data_frame=np.array(data_frame)

plt.pie(x=data_frame["Type"].value_counts().values[:2],labels=data_frame["Type"].value_counts().keys()[:2],autopct='%1.1f%%')
plt.title("paid/free")
plt.show()

topAppsInstallByCategory=data_frame[data_frame["Rating"]>4.9]["Category"].value_counts(normalize=True)

scs.barplot(x=(topAppsInstallByCategory.values*100)[:11],y=topAppsInstallByCategory.keys()[:11])
plt.title="top 10 apps rating: "
plt.grid(True)

plt.show()

# scs.barplot(data=data_frame)