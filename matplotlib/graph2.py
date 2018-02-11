"""
graph2
Plotting a few hydrophobicicy values
"""

from pylab import *

y_data = [1.8, -3.5, 4.5, -0.7, -0.4, -4.5, -1.6, -3.5, -0.9, 4.5,
          -0.9, 3.8, 1.8, 3.8, -0.4, -0.7, 1.8, 3.8, 1.9, -0.4]

x_data = range(1, len(y_data) + 1)
plot(x_data, y_data, linewidth=1.0)


axis(xmin = 1, xmax = len(y_data))

xlabel("residue number")
ylabel("hydrophobicity")
title("Kyte&Doolittle hydrophobicity")

savefig("ex.png")