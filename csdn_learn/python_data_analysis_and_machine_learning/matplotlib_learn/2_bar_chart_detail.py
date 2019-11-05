import numpy as np
import matplotlib.pyplot as plt

mean_values = [1, 2, 3]
variance = [0.1, 0.25, 0.5]
bar_label = ["bar1","bar2","bar3"]

x_pos = list(range(len(bar_label)))
#将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
"""
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 返回一个对象
>>> zipped
zip object at 0x103abc288>
>>> list(zipped)  # list() 转换为列表
[(1, 4), (2, 5), (3, 6)]
>>>max_z = max(zipped) #out:
(3, 6)
>>>x, y = max_z #out: 3, 6
"""
#画误差棒 draw deviation bar
plt.bar(x_pos, mean_values, yerr=variance, alpha=0.3)
max_y = max(zip(mean_values, variance))
plt.ylim([0, max_y[0]+max_y[1]*1.2]) # 设置y轴范围 set the y-axis range
plt.ylabel("variable y")
#添加x轴对应坐标显示信息, add x axis corresponding coordinate display information
plt.xticks(x_pos, bar_label)
plt.show()



x1 = np.array([1, 2, 3])
x2 = np.array([2, 2, 3])
bar_label = ["bar1","bar2","bar3"]
fig = plt.figure(figsize= (8, 6)) #设置画图及其大小set the graph and its size(width, height)
y_pos = np.arange(len(x1)) #out: [0 1 2] matrix object
print(y_pos)
y_pos = [x for x in y_pos]
plt.barh(y_pos, x1, color="g", alpha=0.5)
plt.barh(y_pos, -x1, color="b", alpha=0.5)
plt.xlim(-max(x2) - 1, max(x1) + 1) # 设置x轴范围 set the x-axis range
plt.ylim( -1, max(x1) + 1)
plt.show()



green_data = [1, 2, 3]
blue_data = [3, 2, 1]
red_data = [2, 3, 3]
labels = ["group 1", "group 2", "group 3"]
pos = list(range(len(green_data))) #out: [0, 1, 2] list object
width = 0.2
fig, ax = plt.subplots(figsize=(8, 6))
plt.bar(pos, green_data, width, alpha=0.5, color="g", label=labels[0])
plt.bar([p+width for p in pos], blue_data, width, alpha=0.5, color="b", label=labels[1])
plt.bar([p+width*2 for p in pos], red_data, width, alpha=0.5, color="r", label=labels[2])
plt.show()



