import numpy as np
import matplotlib.pyplot as plt

## Generating years and weights 

years = [2000 + x for x in range(100)]
weights =[45 + x for x in range(100)]

print(years,weights)

plt.plot(years,weights, c="r")
plt.show()