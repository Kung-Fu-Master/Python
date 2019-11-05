import numpy as np
import matplotlib.pyplot as plt

"""basic histogram
data = np.random.normal(0, 20, 1000)
bins = np.arange(-100, 100, 5)

plt.hist(data, bins=bins)
plt.xlim([min(data)-5, max(data)+5])

plt.show()


import random
#random.gauss(mean_value, standard_deviation), 标准差和均值
data1 = [random.gauss(15, 10) for i in range(500)]
data2 = [random.gauss(5, 5) for i in range(500)]

bins = np.arange(-50, 50, 2.5)

plt.hist(data1, bins=bins, label="class 1", alpha=0.3)
plt.hist(data2, bins=bins, label="class 2", alpha=0.3)
plt.legend(loc="best")
plt.show()
"""


""" scatter plot
#均值 mean value
mu_vec1 = np.array([0, 0])
#协方差 covariance
cov_mat1 = np.array([[2, 0], [0, 2]])

x1_samples = np.random.multivariate_normal(mu_vec1, cov_mat1, 100)
x2_samples = np.random.multivariate_normal(mu_vec1+0.2, cov_mat1+0.2, 100)
x3_samples = np.random.multivariate_normal(mu_vec1+0.4, cov_mat1+0.4, 100)

plt.figure(figsize=(8, 6))
plt.scatter(x1_samples[:, 0], x1_samples[:, 1], marker="x", color="blue", alpha="0.3", label="x1")
plt.scatter(x2_samples[:, 0], x2_samples[:, 1], marker="o", color="red", alpha="0.3", label="x2")
plt.scatter(x3_samples[:, 0], x3_samples[:, 1], marker="^", color="green", alpha="0.3", label="x3")

plt.legend(loc="best")

plt.show()
"""


"""散点图上添加坐标信息add coordinate information on the scatter plot
x_coords = [0.13, 0.22, 0.39, 0.59, 0.68, 0.74, 0.93]
y_coords = [0.75, 0.34, 0.44, 0.52, 0.80, 0.25, 0.55]

plt.figure(figsize=(8, 6))
plt.scatter(x_coords, y_coords, marker="s", s=30)

for x, y in zip(x_coords, y_coords):
    #在与坐标xy=(,)偏差为xytext=(,)的位置处添加text信息，并居中
    plt.annotate("(%s,%s)"%(x,y), xy=(x, y), xytext=(0, -15), textcoords= "offset points", ha="center")

plt.show()
"""


### 按距指定坐标距离依次从小到大画图Draw from small to large in order from the specified coordinate distance
mu_vec1 = np.array([0, 0])
cov_mat1 = np.array([[1, 0], [0, 1]])
X = np.random.multivariate_normal(mu_vec1, cov_mat1, 500)
fig = plt.figure(figsize=(8,6))
R = X**2
R_sum = R.sum(axis=1)

plt.scatter(X[:, 0], X[:, 1], color="grey", marker="o", s=20*R_sum, alpha=0.5)
plt.show()




