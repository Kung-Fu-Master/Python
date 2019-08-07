import os
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1,4,9,16,25]

#plt.plot(input_values, squares, linewidth=5)
plt.title("Square Numbers", fontsize=20)
plt.xlabel("X axis", fontsize=15)
plt.ylabel("y axis", fontsize=15)

#plt.scatter(2, 4, s=200)
x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]
#plt.scatter(x_value, y_value, s=100)
#plt.scatter(x_value, y_value, c="blue", edgecolor="none", s=100)
#plt.scatter(x_value, y_value, c=(0.8,0,0), edgecolor="none", s=100)

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
#plt.scatter(x_values, y_values, edgecolor="none", s=40)
#plt.axis([0,1100,1,1100000]) #

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors="none", s=40)

plt.tick_params(axis="both", labelsize=15)
plt.savefig("squares_plot.png", bbox_inches='tight')
plt.show()