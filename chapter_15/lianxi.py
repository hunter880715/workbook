# coding: GBK 
import matplotlib.pyplot as plt

x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]

plt.scatter(x_value, y_value, s=14)
plt.title("Number", fontsize=25)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Number of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
