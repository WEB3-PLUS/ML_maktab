---

# 🔑 تفاوت اصلی

* **`.loc`** → انتخاب بر اساس **label** (نام ایندکس‌ها و ستون‌ها)
* **`.iloc`** → انتخاب بر اساس **موقعیت عددی (integer position)**

---

## 🎯 `.loc` (label-based indexing)

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Ali','Sara','Nima','Reza'],
    'age': [23,30,27,35],
    'score': [85,92,78,60]
}, index=['a','b','c','d'])

print(df)
```

```
  name  age  score
a  Ali   23     85
b  Sara  30     92
c  Nima  27     78
d  Reza  35     60
```

### مثال‌ها:

```python
df.loc['a']                 # یک ردیف با label
df.loc[['a','c']]           # چند ردیف
df.loc['a':'c']             # بازه‌ی برچسب‌ها (شامل 'c')

df.loc['a', 'name']         # سطر 'a' و ستون 'name'
df.loc[:, 'age']            # همه‌ی ردیف‌ها، فقط ستون age
df.loc[['a','c'], ['name','score']]  # ترکیبی

# شرطی:
df.loc[df['age'] > 25, ['name','score']]
```

📌 نکته: در `.loc` وقتی slice می‌گیری (`'a':'c'`) انتهای بازه **شامل** می‌شود.

---

## 🎯 `.iloc` (position-based indexing)

```python
df.iloc[0]                  # ردیف اول
df.iloc[[0,2]]              # ردیف‌های اول و سوم
df.iloc[0:3]                # ردیف‌های 0 تا 2

df.iloc[0, 1]               # ردیف 0، ستون 1 → 23
df.iloc[:, 2]               # همه ردیف‌ها، ستون شماره 2 (score)
df.iloc[0:2, 0:2]           # سطرهای 0 و 1، ستون‌های 0 و 1
```

📌 نکته: در `.iloc` وقتی slice می‌گیری (`0:3`) انتهای بازه **شامل نمی‌شود** (مثل لیست‌های پایتون).

---

## 📊 مقایسه‌ی سریع

| ویژگی            | `.loc`                    | `.iloc`                |
| ---------------- | ------------------------- | ---------------------- |
| مبنا             | Label (نام)               | Index عددی (موقعیت)    |
| انتهای slice     | شامل می‌شود               | شامل نمی‌شود           |
| مثال             | `df.loc['a':'c']` → a,b,c | `df.iloc[0:3]` → 0,1,2 |
| قابل استفاده روی | ایندکس‌ها + ستون‌ها       | فقط موقعیت عددی        |

---

## 🧩 ترکیب شرطی + loc

```python
# دانش‌آموزانی که نمره بالای 80 دارند، ستون name فقط
df.loc[df['score'] > 80, 'name']
```

---

## ❗ خطاهای رایج

* `df.loc[0]` → به دنبال **label=0** می‌گردد، نه ردیف اول!
* اگر ایندکس شما 100 تا 200 باشد، `df.loc[0]` خطا می‌دهد.
* برای **ردیف اول واقعی** از `df.iloc[0]` استفاده کن.

---


---

# 🔹 مرحله ۰ — نصب و وارد کردن

```bash
pip install matplotlib
```

```python
import matplotlib.pyplot as plt
import numpy as np
```

`pyplot` همون ماژولیه که بیشتر کار رسم رو انجام میده.

---

# 🔹 مرحله ۱ — اولین نمودار ساده

```python
x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x, y)         # رسم خطی
plt.title("Simple Line Plot")   # عنوان
plt.xlabel("X axis")   # برچسب محور X
plt.ylabel("Y axis")   # برچسب محور Y
plt.show()             # نمایش
```

---

# 🔹 مرحله ۲ — استایل و رنگ‌ها

```python
plt.plot(x, y, color='red', linestyle='--', marker='o')
```

* `color='red'` یا `'r'`
* `linestyle='--'` (خط چین)
* `marker='o'` (دایره برای نقاط)

---

# 🔹 مرحله ۳ — چند نمودار روی هم

```python
y2 = [1,4,9,16,25]
plt.plot(x, y, label='Linear')
plt.plot(x, y2, label='Quadratic')
plt.legend()   # نمایش راهنما (legend)
plt.show()
```

---

# 🔹 مرحله ۴ — انواع نمودار

### 📊 نمودار میله‌ای (Bar)

```python
langs = ['Python','C','Java','C++']
pop = [50,30,40,20]

plt.bar(langs, pop, color='skyblue')
plt.title("Bar Chart")
plt.show()
```

### 🍩 نمودار دایره‌ای (Pie)

```python
sizes = [40,30,20,10]
labels = ['A','B','C','D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()
```

### 📉 نمودار پراکندگی (Scatter)

```python
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='green')
plt.show()
```

### 📊 هیستوگرام (Histogram)

```python
data = np.random.randn(1000)  # داده تصادفی
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.show()
```

---

# 🔹 مرحله ۵ — تنظیمات محورها

```python
plt.plot(x, y)
plt.xlim(0,6)      # محدودیت محور X
plt.ylim(0,12)     # محدودیت محور Y
plt.xticks([0,2,4,6])  # تیک‌های دلخواه روی محور X
plt.yticks([0,5,10])
plt.grid(True)     # شبکه‌بندی
plt.show()
```

---

# 🔹 مرحله ۶ — ساب‌پلات‌ها (چند نمودار در یک شکل)

```python
plt.subplot(1,2,1)   # (ردیف, ستون, شماره)
plt.plot(x, y)
plt.title("Linear")

plt.subplot(1,2,2)
plt.plot(x, y2)
plt.title("Quadratic")

plt.tight_layout()   # جلوگیری از تداخل
plt.show()
```

---

# 🔹 مرحله ۷ — استایل آماده

```python
plt.style.available[:5]   # نمایش چند استایل آماده
plt.style.use('ggplot')   # انتخاب استایل

plt.plot(x, y)
plt.show()
```

---

# 🔹 مرحله ۸ — ذخیره نمودار

```python
plt.plot(x, y)
plt.savefig("plot.png", dpi=300, bbox_inches='tight')
```
