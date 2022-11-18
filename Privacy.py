import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')


x=np.array([2,1,4,3,4,5,3,3,5,2,4,3,2,5,4,1,2,1,1,3,1,2,1,5,2,3,1,3,2,1,3,4,3,2,4,3])
y=np.array([2,1,1,2,2,4,3,3,3,2,3,3,1,3,2,0,2,0,1,1,1,1,0,3,1,2,1,3,2,1,1,3,1,1,3,3])
z=np.array([2,1,1,1,2,3,2,2,3,1,2,2,1,2,0,0,2,0,1,0,1,0,0,2,0,2,1,1,1,0,1,2,0,1,2,1])

ax1.scatter(x,y,z)

plt.show()

