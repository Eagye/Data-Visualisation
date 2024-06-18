import numpy as np
import matplotlib.pyplot as plt

## Finding the number of interest in programming languages

x = ["C++","java","python","c#","Go","javascript"]
y = [30,40,15,80,88,12]

plt.bar(x,y, color="y",align='edge', width=1.0,edgecolor="black",lw=5,)
plt.show()