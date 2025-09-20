import pandas as pd

print(f"version= {pd.__version__}")

s = pd.Series([30, 12, 11], index=['a', 'b', 'c'], dtype="float32")
print(s)

df = pd.DataFrame({
    'name': ["ali", 'reza', 'mohammad', 'farhad'],
    'age': [14, 35, 40, 89],
    'score': [100, 20, 83, 40]
})
print(df.info())
print(f"shape of dataframe:/n {df.shape}")
print(f"describe of info dataframe: \n{df.describe()}")
print(f"pire mard ha: {df[(df["age"] >= 40) & (df["age"] < 100)]}")
df["passed"]=(df["score"] >60 )
print(df) 
# print(df[["name","score"]])
