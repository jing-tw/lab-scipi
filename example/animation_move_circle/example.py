# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# 建立 一個 fig 寬高為 7 與 6.5
fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

# 指定 plt Axe-X 範圍： 0 ~ 10, 
#          plt Axe-Y 範圍  :  0 ~ 10
ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Circle((5, -5), 0.75, fc='y')

# 初始
def init():
    patch.center = (5, 5)    # 設定圓的中心
    ax.add_patch(patch)   # 把圓加入繪圖的行列
    return patch,

def animate(i):
    x, y = patch.center                              # 取得圓形的中心 x, y 座標
    x = 5 + 3 * np.sin(np.radians(i))       # 計算新的 x 座標
    y = 5 + 3 * np.cos(np.radians(i))      # 計算新的 y 座標
    patch.center = (x, y)                           # 更新圓形的位置座標
    patch.radius = x/2                                  # 更新圓形的半徑
    return patch,

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)

plt.show()
