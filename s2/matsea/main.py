import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_data_frame = pd.read_csv("tips.csv")

# print(file_data_frame["sex"].value_counts())

# label_sex=file_data_frame["sex"].value_counts().keys()
# value_sex=np.array((file_data_frame["sex"].value_counts(normalize=True).values*100),dtype="float32")

# print(value_sex)


# plt.pie(value_sex,labels=label_sex,autopct='%1.1f%%')
# plt.title("chart of tips by sex: ")


# label_day=file_data_frame.day.value_counts().keys()
# value_day=file_data_frame.day.value_counts()

# plt.bar(label_day,value_day)

# tip_value=file_data_frame["tip"].value_counts().values
# label_tip=file_data_frame["tip"].value_counts().keys()


# plt.hist(tip_value)

# plt.scatter(tip_value,label_tip)


# plt.show()