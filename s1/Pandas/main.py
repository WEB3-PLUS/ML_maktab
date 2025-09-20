import pandas as pd

titanic_data=pd.read_csv("./titacnic-dataset.csv")    

# print(titanic_data)

# print(titanic_data.head(5))
# print(titanic_data.tail(5))
# print(titanic_data.shape)
# print(titanic_data.columns)
# print(titanic_data.dtypes)
# print(titanic_data.info() )


print(titanic_data.columns)
print(titanic_data[["Survived","Age"]][0:10])
# print(f"count of dead: {(titanic_data["Survived"].value_counts()).__getitem__(["0"])}")

print(titanic_data["Survived"].value_counts(normalize=True)*100 )
print(pd.crosstab(titanic_data.Sex,titanic_data.Survived))
print(pd.crosstab(titanic_data.Sex,titanic_data.Survived,normalize="columns"))

print(titanic_data[titanic_data["Age"] <=5]["Survived"].value_counts(normalize=True)*100)
print(titanic_data["Name"].str.contains("Allen").value_counts())
print(titanic_data.groupby(["Sex","Pclass"])["Fare"].mean().sort_values(ascending=False))