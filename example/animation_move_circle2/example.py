# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

Width=10
Height=10

cx=Width/2;
cy=Height/2;

fig = plt.figure()
#fig.set_dpi(100)
fig.set_size_inches(Width, Height)

# Setup Canvas Range
ax = plt.axes(xlim=(0, Width), ylim=(0, Height))
plt.plot([5],[5],'ro')
patch = plt.Circle((cx, -cy), 0.75, color='b', fill=False)

def init():
    patch.center = (cx, cy)    # 設定圓的中心
    ax.add_patch(patch)   # 把圓加入繪圖的行列
    
    
    return patch,

def animate(i):
    x, y = patch.center                     # 取得圓形的中心 x, y 座標
    x = 5 + 3 * np.sin(np.radians(i))       # 計算新的 x 座標
    y = 5 + 3 * np.cos(np.radians(i))      # 計算新的 y 座標
    # x = 3 * np.sin(np.radians(i))
    # y = 3 * np.cos(np.radians(i))
    patch.center = (x, y)                           # 更新圓形的位置座標
    # patch.radius = x/2                                  # 更新圓形的半徑
    
    return patch,

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)

plt.show()
