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
# ======= test =====

# Edge Position
CX=[0,Width/2,Width,Width/2]
CY=[Width/2,0,Height/2,Height]

# Show the Edige Positions
plt.plot(CX, CY,'ro')

# Show initial Circle
init_radius=2
patch1 = plt.Circle((CX[0], -CY[0]), init_radius, color='g', fill=True)
patch2 = plt.Circle((CX[1], -CY[1]), init_radius, color='r', fill=True)
patch3 = plt.Circle((CX[2], -CY[2]), init_radius, color='b', fill=True)
patch4 = plt.Circle((CX[3], -CY[3]), init_radius, color='y', fill=True)


def init():
    patch.center = (cx, cy)    # 設定圓的中心
    ax.add_patch(patch)   # 把圓加入繪圖的行列
    #ax.add_patch(PATCH)
    
    # setup edge
    patch1.center = (CX[0], CY[0])
    ax.add_patch(patch1)

    patch2.center = (CX[1], CY[1])
    ax.add_patch(patch2)

    patch3.center = (CX[2], CY[2])
    ax.add_patch(patch3)

    patch4.center = (CX[3], CY[3])
    ax.add_patch(patch4)
    
    return patch,

def animate(i):
    x, y = patch.center                     # 取得圓形的中心 x, y 座標
    x = 5 + 3 * np.sin(np.radians(i))       # 計算新的 x 座標
    y = 5 + 3 * np.cos(np.radians(i))      # 計算新的 y 座標
    patch.center = (x, y)                  # 更新圓形的位置座標
    patch.radius = x/2                     # 更新圓形的半徑

    patch1.radius = np.random.uniform(0.75,Height/2,1)
    patch2.radius = np.random.uniform(0.75,3,1)
    patch3.radius = np.random.uniform(0.75,3,1)
    patch4.radius = np.random.uniform(0.75,3,1)
    return patch, patch1, patch2, patch3, patch4

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)

plt.show()
