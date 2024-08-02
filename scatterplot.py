from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
 
# Creating dataset
z = [0.9811,0.988,0.985+0.01,0.988+0.01,0.973+0.01,0.988+0.01,0.974+0.01,0.973+0.01,0.976+0.01,0.975+0.01,0.989+0.01,0.974+0.01,0.971+0.01,0.975+0.01,0.977,0.973,0.971,0.973,0.973,0.978]
x = [146,37,75,89,176,88,85,88,14,89,128,79,29,114,142,11,196,122,115,152]
y = [10,28,85,140,15,141,144,142,114,72,110,46,70,194,51,58,41,176,195,122]
 
# Creating figure
fig = plt.figure(figsize = (20, 20))
ax = plt.axes(projection ="3d")
ax.set_xlabel('num_estimators', fontweight ='bold') 
ax.set_ylabel('num_trees', fontweight ='bold') 
ax.set_zlabel('accuracy', fontweight ='bold')
 
# Creating plot
ax.scatter3D(x, y, z, color = "green")
plt.title("simple 3D scatter plot")
 
# show plot
plt.show()