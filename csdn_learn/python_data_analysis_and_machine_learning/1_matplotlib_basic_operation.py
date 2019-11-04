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
plt.show()
plt.cla() ### 清除axes，即当前 figure 中的活动的axes，但其他axes保持不变
plt.clf() ### 清除当前 figure 的所有axes，但是不关闭这个 window，所以能继续复用于其他的 plot
plt.close("all")

line = plt.plot(x, y)
###set the properties of the line; alpha: degree of transparency
plt.setp(line, color="r", linewidth=2.0, alpha=0.5)
plt.show()

### 211 tow rows and 1 column, the last number 1 indicates the first image in the subgraph
plt.subplot(211)
plt.plot(x, y, color="r")
plt.subplot(212)
plt.plot(x, y, color="r")
plt.show()

plt.subplot(321)
plt.plot(x, y, color="r")
plt.subplot(326)
plt.plot(x, y, color="r")
plt.show()

