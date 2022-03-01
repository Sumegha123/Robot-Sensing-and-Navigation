import matplotlib.pyplot as plt
import csv
import numpy as np

x=[]
y=[]

x1=[]
y1=[]

x2=[]
y2=[]

x3=[]
y3=[]

x4=[]
y4=[]
#input file
with open('data2.csv','r') as csvfile:  
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots) 
    for row in plots:
    	# altitude vs sequence
 #   	x.append(float(row[1])) #sequence
#    	y.append(float(row[11])) #altitude

    	 # easting vs northing
    	x.append(float(row[7])) #easting
    	y.append(float(row[8])) #northing
    

i=0;
with open('data2.csv','r') as csvfile:  
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots) 
    for row in plots:
        i=i+1
    	# altitude vs sequence
 #   	x.append(float(row[1])) #sequence
#    	y.append(float(row[11])) #altitude

    	 # easting vs northing
        if i<49:
            x1.append(float(row[7])) #easting
            y1.append(float(row[8])) #northing

m,c = np.polyfit(x1,y1,1)
bestfit1 = [elem*m +c for elem in x1]

i=0
with open('data2.csv','r') as csvfile:  
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots) 
    for row in plots:
    	# altitude vs sequence
 #   	x.append(float(row[1])) #sequence
#    	y.append(float(row[11])) #altitude

    	 # easting vs northing
    	i=i+1
    	if i>48 and i<64:
    	    x2.append(float(row[7])) #easting
    	    y2.append(float(row[8])) #northing
    
m,c = np.polyfit(x2,y2,1)
bestfit2 = [elem*m +c for elem in x2]
 
i=0 
with open('data2.csv','r') as csvfile:  
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots) 
    for row in plots:
        i=i+1
    	# altitude vs sequence
 #   	x.append(float(row[1])) #sequence
#    	y.append(float(row[11])) #altitude

    	 # easting vs northing
        if i>63 and i<93:
            x3.append(float(row[7])) #easting
            y3.append(float(row[8])) #northing

m2,c2 = np.polyfit(x3,y3,1)
bestfit3 = [elem*m2 +c2 for elem in x3]
    	
i=0
with open('data2.csv','r') as csvfile:  
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots) 
    for row in plots:
        i=i+1
    	# altitude vs sequence
 #   	x.append(float(row[1])) #sequence
#    	y.append(float(row[11])) #altitude

    	 # easting vs northing
        if i>92 and i<127:
    	     x4.append(float(row[7])) #easting
    	     y4.append(float(row[8])) #northing
    	
m3,c3 = np.polyfit(x4,y4,1)
bestfit4 = [elem*m3 +c3 for elem in x4]
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


#m,c = np.polyfit(x,y,1)
#bestfit = [elem*m +c for elem in x]


#mx = [mean_ for elem in x]
#dx = [dev for elem in x]

plt.scatter(x, y, color = 'g',s=10)
plt.plot(x1,bestfit1,linestyle='dashed', label = "Best fit line",color = 'red')
plt.plot(x2,bestfit2,linestyle='dashed',color = 'red')
plt.plot(x3,bestfit3,linestyle='dashed',color = 'red')
plt.plot(x4,bestfit4,linestyle='dashed',color = 'red')

#labels
plt.xlabel('Utm_Easting(in m)')
plt.ylabel('Utm_Northing(in m)')

#plt.xlabel('Sequence number')
#plt.ylabel('GPS Quality indicator')

 #error in easting vs northing
error1 = np.zeros(len(y1))
for i in range(len(y1)):
    error1[i] = abs(y1[i]-bestfit1[i])
    
max_error1 = np.max(error1)
min_error1 = np.min(error1)
print (max_error1)
print (min_error1)
# mean = np.mean(y)
# print(mean)

error2 = np.zeros(len(y2))
for i in range(len(y2)):
    error2[i] = abs(y2[i]-bestfit2[i])
    
max_error2 = np.max(error2)
min_error2 = np.min(error2)
print (max_error2)
print (min_error2)

error3 = np.zeros(len(y3))
for i in range(len(y3)):
    error3[i] = abs(y3[i]-bestfit3[i])
    
max_error3 = np.max(error3)
min_error3 = np.min(error3)
print (max_error3)
print (min_error3)

error4 = np.zeros(len(y4))
for i in range(len(y4)):
    error4[i] = abs(y4[i]-bestfit4[i])
    
max_error4 = np.max(error4)
min_error4 = np.min(error4)
print (max_error4)
print (min_error4)

#plt.title('GPS quality indicato vs sequence number')
plt.title('Utm_Easting vs Northing')
plt.legend()
plt.grid()
plt.savefig("plots/"+'best_fit_obs_moving.png', dpi =300)
plt.show()


