import numpy as np
import matplotlib.pyplot as plt

###basic picture
plt.plot([1,2,3,4,5], [1,2,3,4,5]) #paint x axis & y axis
#plt.show()

plt.xlabel("xlabel", fontsize=16)
plt.ylabel("ylabel")
plt.title("Draw", fontsize=20)
#plt.show()


plt.plot([1,2,3,4,5], [1,4,9,16,25], "-.", marker="o", color="r") #paint x axis & y axis
#print(help(plt.plot))
#plt.show()

tang_numpy = np.arange(0, 10, 0.5)
plt.plot(tang_numpy, tang_numpy**2, "r--", #draw multiple lines
         tang_numpy, tang_numpy**3, "bs",
         tang_numpy, tang_numpy**4, "go")
#plt.show()

x = np.linspace(-10, 10)
y = np.sin(x)
plt.plot(x, y,linewidth=2.0) #linewidth: specify line thickness
#plt.show()

###marker:key point; markerfacecolor:key point color; markersize: key point size
plt.plot(x, y, color='b', linestyle=":", marker="o", markerfacecolor="red",markersize=10)
plt.text(1, 0.5, "text") ### add text information at coordinates (1, 0.5)
plt.text(10, 0.75, "text1")
plt.grid(True) ###add grid
plt.annotate("annotate", xytext=(-5.0, 0.0), xy=(10, 0.75), 
            arrowprops=dict(facecolor="red", shrink=0.01,headlength=20, headwidth=20))
#plt.show()
plt.cla() ### 清除axes，即当前 figure 中的活动的axes，但其他axes保持不变
plt.clf() ### 清除当前 figure 的所有axes，但是不关闭这个 window，所以能继续复用于其他的 plot
plt.close("all")

line = plt.plot(x, y)
###set the properties of the line; alpha: degree of transparency
plt.setp(line, color="r", linewidth=2.0, alpha=0.5)
#plt.show()

### 211 tow rows and 1 column, the last number 1 indicates the first image in the subgraph
plt.subplot(211)
plt.plot(x, y, color="r")
plt.subplot(212)
plt.plot(x, y, color="r")
#plt.show()

plt.subplot(321)
plt.plot(x, y, color="r")
plt.subplot(326)
plt.plot(x, y, color="r")
plt.show()



"""采用多种style use a variety of styles
x = np.linspace(-10, 10)
y = np.sin(x)
#plt.style.use("dark_background")
#plt.style.use("bmh")
#plt.style.use("ggplot")
plt.style.use(["bmh","ggplot"])
plt.plot(x, y,linewidth=2.0) #linewidth: specify line thickness
plt.show()

plt.xkcd()
plt.plot(x, y)
plt.show()
"""



"""消除x轴y轴坐标eliminate x-axis yaxis coordinates
x = range(10)
y = range(10)
#当前的图表和子图可以使用plt.gcf()和plt.gca()获得，分别表示Get Current Figure和Get Current Axes。
#在pyplot模块中，许多函数都是对当前的Figure或Axes对象进行处理，
#比如说：plt.plot()实际上会通过plt.gca()获得当前的Axes对象ax，然后再调用ax.plot()方法实现真正的绘图。
ax = plt.gca()
plt.plot(x, y)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
plt.show()
"""


"""消除x轴y轴坐标eliminate x-axis yaxis coordinates
import math
x = np.random.normal(loc=0.0, scale=1.0, size=300)
width = 0.5
bins = np.arange(math.floor(x.min()) - width, math.ceil(x.max()) + width, width)

ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tick_params(bottom="off", top="off", left="off", right="off")

plt.hist(x, alpha=0.5, bins=bins)

plt.grid()

plt.show()
"""


"""添加x坐标信息，并旋转右对齐 add x-axis coordinate information and rotate right alignment
x = range(10)
y = range(10)
labels = ["information" for i in range(10)]
fig, ax = plt.subplots()
plt.plot(x, y)

#x轴坐标信息右对齐x-axis coordinate information is right aligned
ax.set_xticklabels(labels, rotation=45, horizontalalignment="right")

plt.show()
"""

x = np.arange(10)
for i in range(1, 4):
    #label="":当前线的所属类别的信息information about the category of the current line
    plt.plot(x, i*x**2, label="Group %d" %i, marker="o")
#在图中加入上面的label标识add the above label to the figure
#framealpha:透明度 transparency 
#plt.legend(loc="best", framealpha=0.1)
plt.legend(loc="upper right", framealpha=0.01)
#plt.legend(loc="upper left") 
plt.show()


###设置全局变脸参数，使所有图的title fontsize=30
import matplotlib as mpl
mpl.rcParams["axes.titlesize"] = "30"

fig = plt.figure()
ax = plt.subplot(111)
x = np.arange(10)
for i in range(1, 4):
    plt.plot(x, i*x**2, label="Group %d"%i)
#在图外加入上面的label标识 add the above label to the outside of the figure
#bbox_to_anchor:labels 存放位置，参数需要根据自己需要调节,labels storage location, parameters need to be adjust
#ncol: labels 分成三列来放置 labels are placed in three columns
#framealpha:透明度 transparency 
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3, framealpha=0.01)
#ax.legend(loc="upper center", bbox_to_anchor=(1.07, 1), ncol=1, framealpha=0.1)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_title("title information") # 不指定fontsize的话会默认为上面的全局参数fontsize=30
ax.set_title("title information", fontsize=20)
plt.show()











