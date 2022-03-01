import matplotlib.pyplot as plt
import csv
import numpy as np

x=[]
y=[]

#input file
with open('moving_data.csv','r') as csvfile:  
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots) 
    for row in plots:
    	# altitude vs sequence
    	# x.append(float(row[1])) #sequence
    	# y.append(float(row[6])) #altitude

    	# easting vs northing
    	x.append(float(row[7])) #easting
    	y.append(float(row[8])) #northing


#functions:

# mean
mean_ = np.mean(y)
print("mean: ",mean_) 

# median
median_ = np.median(y)
print("median: ",median_)

# std_deviation
dev = np.std(y)
print("std_dev: ", dev)

# best_fit
m,c = np.polyfit(x,y,1)
bestfit = [elem*m +c for elem in x]

mx = [mean_ for elem in x]
dx = [dev for elem in x]

plt.scatter(x, y, color = 'g',s=10)
plt.plot(x,bestfit,linestyle='dashed', label = "Best fit line",color = 'red')

#labels
plt.xlabel('Utm_Easting(in m)')
plt.ylabel('Utm_Northing(in m)')

#error in easting vs northing
error = np.zeros(len(y))
for i in range(len(y)):
	error[i] = abs(y[i]-bestfit[i])
max_error = np.max(error)
min_error = np.min(error)
print max_error
print min_error
# mean = np.mean(y)
# print(mean)

plt.title('Utm_Easting vs Northing for Stationary data')
plt.legend()
plt.savefig("Plots/"+'eastnorth_station.png', dpi =300)

plt.show()


