# importing mplot3d toolkits, numpy and matplotlib
#from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas

plot = pandas.read_csv('data2.csv')

fig = plt.figure(figsize=(10, 10))

ax = fig.add_subplot(111, projection='3d')

x = plot['field.utm_easting'].values
y = plot['field.utm_northing'].values
z = plot['field.altitude'].values

ax.set_xlabel('Utm_Easting(in m)')
ax.set_ylabel('Utm_Northing(in m)')
ax.set_zlabel('Altitude(in m)')

plt.title('Utm_Easting vs Northing vs Altitude for obstructed moving data')
ax.scatter(x, y, z, c='r', marker='o')
plt.savefig("plots/"+'eastnorth_obs_moving_3d.png', dpi =300)
plt.show()
