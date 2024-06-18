import numpy as np
import matplotlib.pyplot as plt

langs = ["Twi","Fante","English","French","Spanish","Ga","Chinese","Japanes"]
votes =[30,1020,5000,899,798,999,1011,5896]

## to bring out sections in the pie chat
explodes=[0.5,0,0,0,0,0,0,0]

plt.pie(votes,labels=langs, explode=explodes)
plt.show()