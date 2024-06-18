import os
import matplotlib.pyplot as plt
from matplotlib.image import imread
import pandas as pd
import seaborn as sns

df=pd.read_csv("C:/Users/eagye/Desktop/dv/Salary_dataset.csv")

##df.head()
missing_values= df.isnull().sum()

print(missing_values)



# Visualizing missing values using a heatmap
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.show()
