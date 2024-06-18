import numpy as np
import matplotlib.pyplot as plt

##generating random ages 

ages = np.random.normal(15,1.5,500)
##print(ages)
plt.hist(ages,bins=[ages.min(),13,16,ages.max()],cumulative=True)
plt.show()

