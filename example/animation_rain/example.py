#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

# 建立一個 fig 用來放我的 Ring 
fig = plt.figure(figsize=(6,6), facecolor='white')
ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)


# Ring 的數量
n = 50
size_min = 50
size_max = 50*50

# 50 個 Ring 的初始位置： P 陣列裡面放了 50 筆, 平均散佈位置 (x, y) 資訊
P = np.random.uniform(0,1,(n,2))    # 產生 50 筆位置資料, 範圍: 0 ~ 1 (不含)

# 50 個 Ring 的初始顏色： C 陣列裡面放了 50 筆顏色資料, 從 0 ~ 1
C = np.ones((n,4)) * (0,0,0,1)        # 產生一個陣列 (50, 4), 只有第四個元素是 1, 其他都是 0
C[:,3] = np.linspace(0,1,n)             # 開始填入透明值 (第四個位置), 從最透明 (0) ~ 實心 (1)


# 50 個 Ring 的初始大小： S 陣列裡面從小到大放 1, 2, 3, ..., 50
S = np.linspace(size_min, size_max, n)

# 把 50 個 Ring 用 Scatter 方式繪製出來 
# scatter(X, Y, 點的大小, 點裡面的顏色值, 點邊緣的顏色值, 表面顏色值)
scat = ax.scatter(P[:,0], P[:,1], s=S, lw = 0.5, edgecolors = C, facecolors='None')

# 設定圖形的座標軸: 範圍固定為 0 ~ 1 且 確保移除軸上的 ticks
ax.set_xlim(0,1), ax.set_xticks([])
ax.set_ylim(0,1), ax.set_yticks([])


# 更新每一個 Ring 的資訊
# 1. 越來越透明
# 2. 越來越大
# 3. 位置

def update(frame):
    global P, C, S

    # 更新 C 陣列: 設定每一個點以 1/50 分之一的速度, 變淡
    C[:,3] = np.maximum(0, C[:,3] - 1.0/n)

    # 更新 S 陣列: 每一個 Ring 的大小, 以 1/50 的速度增加大小
    S += (size_max - size_min) / n

    # 對每一個 index frame 重新 reset Ring 的資料
    # 下面這段 code 輪流的把每一個 Ring, 一個一個掃過, 設定回初值.
    # 原文: Reset ring specific ring (relative to frame number)
    i = frame % 50
    P[i] = np.random.uniform(0,1,2)    # reasslgin location
    S[i] = size_min  # small
    C[i,3] = 1            # most opaq

    # 根據 C, P 陣列, 重新繪製 Ring 到視窗上
    scat.set_edgecolors(C)
    scat.set_sizes(S)
    scat.set_offsets(P)

    # Return the modified object
    return scat,

anim = animation.FuncAnimation(fig, update, interval=10, blit=True, frames=200)

plt.show()

