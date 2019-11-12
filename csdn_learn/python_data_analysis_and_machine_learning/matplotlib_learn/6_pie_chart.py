import numpy as np
import matplotlib.pyplot as plt

m = 51212.
f = 40742.
m_perc = m/(m+f)
f_perc = f/(m+f)

colors = ["navy", "lightcoral"]
labels = ["Male", "Female"]

plt.figure(figsize=(6, 6))
#explode: 控制图模块之间缝隙大小 control gap size
paches, texts, autotexts = plt.pie([m_perc,f_perc], labels=labels, autopct="%1.f%%",explode=[0, 0.05],colors=colors)

for text in texts+autotexts:
    text.set_fontsize(20)
for text in autotexts:
    text.set_color("white")

plt.show()


####################### 设置子图布局 set submap layout
##total 3 rows, total 3 columns
ax1 = plt.subplot2grid((3,3),(0,0))
ax2 = plt.subplot2grid((3,3),(1,0))
ax3 = plt.subplot2grid((3,3),(0,2), rowspan=3)
ax4 = plt.subplot2grid((3,3),(2,0), colspan=2)
ax5 = plt.subplot2grid((3,3),(0,1), rowspan=2)
plt.show()

####################### 图里再嵌套图 nested graph
import numpy as np
x = np.linspace(0, 10, 1000)
y1 = x**2
y2 = np.sin(x**2)
fig, ax = plt.subplots() # the same as below
#fig, ax  = plt.subplots((1, 1))

left, bottom, width, height = (0.22, 0.45, 0.3, 0.35)
ax1 = fig.add_axes([left, bottom, width, height])

ax.plot(x, y1)
ax1.plot(x, y2)

plt.show()


######################
















