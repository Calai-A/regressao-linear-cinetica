import numpy as np
from matplotlib import pyplot as plt

a=[]
b=[3,4,10,12]
a.append(1)
a.append(2)
a.append(3)
print(a)
a[2] = (a[1]+a[2])
print(a)
print(b)
a = np.array(a)
b = np.asarray(b)
print(a)
print(b)

plt.plot(a,b)
plt.show()