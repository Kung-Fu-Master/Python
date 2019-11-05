import numpy as np
import matplotlib.pyplot as plt

data = range(200, 225, 5)
bar_labels = ["a","b","c","d","e"]

fig = plt.figure(figsize=(10, 8))
y_pos = np.arange(len(data))

plt.yticks(y_pos, bar_labels, fontsize=16)

#横着画条形图 horizontal bar chart
bars = plt.barh(y_pos, data, alpha=0.5, color="g")

#添加虚线 add dotted line
plt.vlines(min(data), -1, len(data) + 0.5, linestyle="dashed")

#添加注释 add notes
for b, d in zip(bars, data):
    plt.text(b.get_width()+ b.get_width()*0.05, b.get_y()+b.get_height()/2, 
                "{0:.2%}".format(d/min(data)))
plt.show()



mean_values = range(10, 18)
x_pos = range(len(mean_values))
import matplotlib.colors as col
import matplotlib.cm as cm

cmap1 = cm.ScalarMappable(col.Normalize(min(mean_values), max(mean_values), cm.hot))
cmap2 = cm.ScalarMappable(col.Normalize(0, 20, cm.hot))

plt.subplot(121)
plt.bar(x_pos, mean_values, color=cmap1.to_rgba(mean_values))

plt.subplot(122)
plt.bar(x_pos, mean_values, color=cmap2.to_rgba(mean_values))

plt.show()




patterns = ("_", "+", "x", "\\", "*", "o", "O", ".")
fig = plt.gca()
mean_value = range(1, len(patterns)+1)
x_pos = list(range(len(mean_value)))

bars = plt.bar(x_pos, mean_value, color="white")
for bar, pattern in zip(bars, patterns):
    bar.set_hatch(pattern)
plt.show()









