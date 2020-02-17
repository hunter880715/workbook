# coding: GBK
import matplotlib.pyplot as plt

x_zhou = list(range(1, 101))
y_zhou = [x**2 for x in x_zhou]
plt.scatter(x_zhou, y_zhou, s=40)
plt.x_zhou("Value", fintsize=14)
plt.axis([0, 110, 0, 11000])

plt.show()
