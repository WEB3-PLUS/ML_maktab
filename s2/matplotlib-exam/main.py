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

# x=[23,30,45,2]
# company=["apple","samsung","xm","other"]

# plt.pie(x,labels=company, autopct='%1.1f%%')
# plt.title("phone companys in iran: ")

# plt.show()

# ____________________________________________________________
# scatter chart

# x=np.random.rand(50)*100
# y=np.random.rand(50)*100
# plt.scatter(x,y,color="green")

# plt.show()

# __________________________________________________________
# pow chart

# x = list(range(-10, 11))
# y = np.multiply(x, x)

plt.style.use("ggplot")
# plt.grid(True)
# plt.title("X^2=y")
# # print(plt.style.available[0:10])

# plt.plot(x,y)

# plt.show()


# ____________________________________________________________
# random histogram
x = (np.random.rand(1000)*5).round(decimals=0)
plt.hist(x=x,align="mid")
plt.show()