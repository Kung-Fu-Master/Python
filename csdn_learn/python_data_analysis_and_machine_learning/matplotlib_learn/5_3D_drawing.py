import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)

X, Y = np.meshgrid(x, y)

R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)
#Z = np.sin(np.sqrt(x**2+y**2))
ax.plot_surface(X,Y,Z, 
                rstride=1,  # rstride（row）指定行的跨度
                cstride=1,  # cstride(column)指定列的跨度
                cmap="rainbow") # 设置颜色映射
plt.title("3D图")
#投影 projection
ax.contour(X, Y, Z, zdim='z', offset=-2, cmap="rainbow")
ax.set_zlim(-2, 2)
#plt.show()

###########################
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
#plt.show()



########################### 3D line
fig = plt.figure()
ax = fig.gca(projection="3d")

theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2
x = r * np.sin(theta)
y = r * np.cos(theta)

ax.plot(x, y, z)
#plt.show()


############################# 3D 散点图 Scatter plot

np.random.seed(1)
def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
n= 100

for c, m, zlow, zhigh in [("r", "o", -50,-25),("b","x", -30, -5)]:
    xs = randrange(n, 23, 32) 
    ys = randrange(n, 0, 100) 
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

##指定三维图对着自己的方向
##specify the 3D map to face your direction
ax.view_init(30,10)

plt.show()


################################### 条形图bar chart

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
for c, z in zip(['r','g','b','y'], [30,20,10,0]):
    xs = np.arange(20)
    ys = np.random.rand(20)
    cs = [c]*len(xs)
    ax.bar(xs, ys, zs=z, zdir='y')
    #ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.7)
plt.show()











