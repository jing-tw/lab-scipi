#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Step 1: 定義我們預想的曲線
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# Step 2: 產生一個帶有亂數的曲線
X = np.linspace(0,4,50)
Y = func(X, 2.5, 1.3, 0.5)
YN = Y + 0.2*np.random.normal(size=len(X))  # 加上亂數 模擬實際的數值

# Step 3: 產生一個最佳貼近的曲線公式
popt, pcov = curve_fit(func, X, YN)

print "popt=", popt
print "pcov=", pcov
print "error=", np.sqrt(np.diag(pcov))

# 把圖畫出來
plt.figure()
plt.plot(X, YN, 'ko', label="Original Noised Data")     # 畫出模擬實際值
plt.plot(X, func(X, *popt), 'r-', label="Fitted Curve")  # 畫出 curfit 所計算出來的參數曲線
plt.legend()
plt.show()
