# importing the required module 
import matplotlib.pyplot as plt 
  
# x axis values 
x = [10,100,1000,4000,6000] 
# corresponding y axis values 
y = [0.77,0.91,4.21,5.24,4.31] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Number of GET requests') 
# naming the y axis 
#plt.xticks([2,4,8,16,32,64,128,256,512,1024])
plt.ylabel('response time(seconds)') 
  
# giving a title to my graph 
 
plt.grid()
# function to show the plot 
plt.show()