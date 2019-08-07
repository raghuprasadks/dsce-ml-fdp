#https://bigdata-madesimple.com/step-by-step-approach-to-perform-data-analysis-using-python/

#Simple Plotting example
#%matplotlib inline 
import matplotlib.pyplot as plt #importing matplot lib library
import numpy as np 
x = range(100) 
#print x, print and check what is x
y =[val**2 for val in x] 
#print y
plt.plot(x,y) #plotting x and y

# Using Numpy
#https://www.geeksforgeeks.org/numpy-linspace-python/

x = np.linspace(0, 2*np.pi, 100)
y =np.sin(x)
plt.plot(x,y)

x= np.linspace(-3,2, 200)
Y = x ** 2 - 2 * x + 1.
plt.plot(x,Y)

# plotting multiple plots
x =np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y) 
plt.plot(x,z)
plt.show()

# Matplot lib picks different colors for different plot. 

data = np.loadtxt('numpy.txt')
plt.plot(data[:,0], data[:,1]) # plotting column 1 vs column 2

data1 = np.loadtxt('scipy.txt') # load the file
print(data1.T)

for val in data1.T: #loop over each and every value in data1.T
    plt.plot(data1[:,0], val) #data1[:,0] is the first row in data1.T
    
#Scatter Plots and Bar Graphs
sct = np.random.rand(20, 2)
print(sct)
plt.scatter(sct[:,0], sct[:,1]) # I am plotting a scatter plot.

# simple bar graph
ghj =[5, 10 ,15, 20, 25]
it =[ 1, 2, 3, 4, 5]
plt.bar(ghj, it)

# you can change the thickness of a bar, by default the bar will have a thickness of 0.8 units

ghj =[5, 10 ,15, 20, 25]
it =[ 1, 2, 3, 4, 5]
plt.bar(ghj, it, width =5)

# barh is a horizontal bar graph
ghj =[5, 10 ,15, 20, 25]
it =[ 1, 2, 3, 4, 5]
plt.barh(ghj, it) 

new_list = [[5., 25., 50., 20.], [4., 23., 51., 17.], [6., 22., 52., 19.]]
x = np.arange(4) 
plt.bar(x + 0.00, new_list[0], color ='b', width =0.25)
plt.bar(x + 0.25, new_list[1], color ='r', width =0.25)
plt.bar(x + 0.50, new_list[2], color ='g', width =0.25)

#plt.show()

#Pie charts
y = [5, 25, 45, 65]
plt.pie(y)



    
