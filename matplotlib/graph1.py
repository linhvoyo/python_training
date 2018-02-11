"""
graph1
Make a simple sawtooth pattern
"""

from pylab import *

x_data = [0, 1, 2,  3, 4, 5, 6]
y_data = [0, 1, 0, -1, 0, 1, 0]

plot(x_data, y_data)

xlabel("This is the x label")
ylabel("This is the y label")
title("Here is the title")

grid(True)

show()