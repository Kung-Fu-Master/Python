import numpy as np
import matplotlib.pyplot as plt

tang_data = [np.random.normal(0,std,100) for std in range(1,4)]

fig = plt.figure(figsize=(8,6))
#notch=False: 用基本形状, 不用特别形状with basic ships, no special shapes
#sym: 离群点用方框来表示 outliers are respresented by boxes
#vert=True: 垂直画盒图vertical picture box diagram
#patch_artist=True 才能进行颜色的填充 to fill the color
bplot = plt.boxplot(tang_data, notch=False, sym="s", vert=True, patch_artist=True)
#bplot = plt.boxplot(tang_data, notch=False, sym="s", vert=False)
#对x轴属性进行操作operate on the x-axis properties
plt.xticks([y+1 for y in range(len(tang_data))], ["x1","x2","x3"])
plt.xlabel("X")
#plt.yticks([y+1 for y in range(len(tang_data))], ["x1","x2","x3"])
#plt.ylabel("X")
plt.title("box diagram")

"""把每一个组件的线条都画成黑色draw the lines of each component black
for components in bplot.keys():
    for line in bplot[components]:
        line.set_color("black")
"""

"""填充组件盒子颜色fill component box color
colors = ["pink","lightblue","lightgreen"]
#组件盒子和color进行组合component boxes and color combination
for pathch, color in zip(bplot["boxes"], colors):
    pathch.set_facecolor(color)
"""

plt.show()

###小提琴图 violin diagram
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
tang_data = [np.random.normal(0, std, 100) for std in range(6, 10)]
axes[0].violinplot(tang_data, showmeans=True, showmedians=True)
axes[0].set_title("violin plot")

axes[1].boxplot(tang_data)
axes[1].set_title("box plot")

#加上一些水平线 plus some horizontal lines
for ax in axes:
    ax.yaxis.grid(True)
    #ax.xaxis.grid(True)
    #ax.set_xticks([y+1 for y in range(len(tang_data))], ["x1","x2","x3","x4"])

###每个图x轴添加labels, add labels to each figure x axis
plt.setp(axes, xticks=[y+1 for y in range(len(tang_data))], xticklabels=["x1","x2","x3","x4"])

plt.show()


