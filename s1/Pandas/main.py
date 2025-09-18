import pandas as pd

titanic_data=pd.read_csv("./titacnic-dataset.csv")    

# print(titanic_data)

print(titanic_data.head(5))
print(titanic_data.tail(5))
print(titanic_data.shape)
print(titanic_data.columns)
print(titanic_data.dtypes)
print(titanic_data.info() )