import matplotlib.pyplot as plt
import numpy as np
costs=[1,8,15,7,5,14,43,40]
costs=sorted(costs)
print(costs)
#[1, 5, 7, 8, 14, 15, 40, 43]

data = [1, 8, 15, 7, 5, 14, 43, 40]
labels = ["Los Angeles 1984", "Seoul 1988", "Barcelona 1992", "Atlanta 1996", "Sydney 2000", "Athens 2003", "Beijing 2008", "London 2012"]
plt.bar(range(len(data)), data, width=0.5)
plt.xticks(range(len(data)),labels,rotation=18)
plt.ylabel("Cost (in $ billions")
plt.show()


