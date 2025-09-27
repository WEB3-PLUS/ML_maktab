import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

tips=pd.read_csv("tips.csv")

# historial chart for tips
# sns.histplot(data=tips,x="tip",bins=20,kde=True,hue="sex") 

# sns.countplot(data=tips,x="smoker",hue="sex")

# sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", style="time")


corr = tips.corr(numeric_only=True)  # ماتریس همبستگی
sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.show()


# print(tips.head())