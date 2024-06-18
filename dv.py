import numpy as np
import matplotlib.pyplot as plt

## generating random variables
X_data = np.random.random(60)*100
Y_data = np.random.random(60)*100

##print(X_data)

## plotting a scatter plot
plt.scatter(X_data,Y_data, c="green", marker="*")
plt.show()

