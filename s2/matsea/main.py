import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_data_frame = pd.read_csv("tips.csv")

# print(file_data_frame["sex"].value_counts())

label_sex=file_data_frame["sex"].value_counts().keys()
value_sex=np.array((file_data_frame["sex"].value_counts(normalize=True).values*100),dtype="float32")

# print(value_sex)


plt.pie(value_sex,labels=label_sex,autopct='%1.1f%%')
plt.title("chart of tips by sex: ")
plt.show()