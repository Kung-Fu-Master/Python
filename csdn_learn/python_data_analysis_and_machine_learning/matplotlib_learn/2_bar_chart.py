import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)#设置相同的seed，每次生成的随机数相同
                 #每次调用都需要seed(0)一下，表示种子相同
x = np.arange(5)

y = np.random.randint(-5, 5, 5)
#y = np.random.randint(low=-5, high=5, size=5) the same as above
#y = np.random.randint(low=-5, high=5, size=(2,3))
#返回随机整数或整型数组，范围区间为[low,high），包含low，不包含high；
#high没有填写时，默认生成随机数的范围是[0，low)


plt.bar(x, y, color="green")
plt.show()

# set two columns 设置两列
fig, axes = plt.subplots(ncols=2)
v_bars = axes[0].bar(x, y, color="red")
h_bars = axes[1].barh(x, y, color="g")

#Figure 0 在坐标y=0处添加横线add a horizontal line at the coordinate y=0
axes[0].axhline(0, color="grey", linewidth=2) 
#Figure 1 在坐标x=0处添加竖线add a vertical line at the coordinate x=0
axes[1].axvline(0, color="grey", linewidth=2)
plt.show()

fig, ax = plt.subplots()
v_bars = ax.bar(x, y, color="lightblue")
ax.axhline(0, color="grey", linewidth=2)
for bar, height in zip(v_bars, y):
    if height < 0:
        bar.set(edgecolor = "darkred", color = "green", linewidth=3)
plt.show()

#np.random.rand()函数
#   返回一个或一组服从“0~1”均匀分布的随机样本值。随机样本取值范围是[0,1)，不包括1.
#np.random.randn()函数
#   返回一个或一组服从标准正态分布的随机样本值,均值为0, 标准差为1

"""
##沿着指定轴的元素累加和所组成的数组，其形状应与输入数组a一致
**arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
**沿着axis=0轴计算
**result1=arr.cumsum(0)   #array([[ 1,  2,  3],[ 5,  7,  9],[12, 15, 18]], dtype=int32)
**沿着axis=1轴计算
**result2=arr.cumsum(1)   #array([[ 1,  3,  6],[ 4,  9, 15],[ 7, 15, 24]], dtype=int32)
**arr.cumsum()并不是arr.cumsum(0)和arr.cumsum(1)的并集，而是将arr重塑为一维数组后的，再计算cumsum()的结果
**arr.cumsum()#array([ 1,  3,  6, 10, 15, 21, 28, 36, 45], dtype=int32)
"""
x = np.random.randn(100).cumsum()
y = np.linspace(0, 10, 100) #创建一维等差数组,包含起始值and终值

fig, ax = plt.subplots()
#在x轴和y轴之间进行填充颜色fill color between the x and y axes
ax.fill_between(x, y, color="lightblue")
plt.show()

x = np.linspace(0, 10, 200)
y1 = 2 * x + 1
y2 = 3 * x + 1.2
y_mean = 0.5*x*np.cos(2*x) + 2.5*x + 1.1
fig, ax = plt.subplots()
#在y1和y2之间进行填充 Fill between y1 and y2
ax.fill_between(x, y1, y2, color="red")
ax.plot(x, y_mean,color="black")
plt.show()


