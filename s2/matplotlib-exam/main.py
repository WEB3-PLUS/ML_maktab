import matplotlib.pyplot as plt
import numpy as np

# simple chart

# x = [13, 9, 0, 22, 1]
# y = [7, 23, 14, 19, 3]
# y2 = [10, 2, 40, 9, 31]


# plt.plot(x, y, color="skyblue", linestyle="--", marker="*")
# plt.plot(x, y2, color="purple", linestyle="--", marker="*")
# plt.xlabel("x axis", color='red')
# plt.ylabel("y axis", color="green")


# plt.legend()
# plt.show()

# ____________________________________________________________
# bar chart

# langs = ["c#", "javascript", "c++", "java"]
# pop = [10, 70, 100, 45]

# plt.bar(langs, pop, color="purple")

# plt.xlabel("pop")
# plt.ylabel("langs")
# plt.title("chart of pop langs")

# plt.show()


# ____________________________________________________________
# pie chart

x=[23,30,45,2]
company=["apple","samsung","xm","other"]

plt.pie(x,labels=company, autopct='%1.1f%%')
plt.title("phone companys in iran: ")

plt.show()