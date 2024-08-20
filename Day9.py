# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:40:31 2024

@author: rushi
"""

##MATPLOTLIB
#it is a package inside that there is a pyplot

#write a python program to draw a line with suitable label in the
import matplotlib.pyplot as plt
x = range(1,51)
y = [value * 3 for value in x]
print("value of x : ")
print(*range(1,51))

print("values of Y (thrice of X ):")
print(y)

plt.plot(x,y)
plt.xlabel("x axis")
plt.xlabel("y axis")
plt.title("Draw a line")


#----------------------------------------------------------------
import matplotlib.pyplot as plt
x=[100,200,300]
y=[11,12,13]
#plot the lines and/or markers to the axis
plt.plot(x,y)
#set the x axis label to the current axis
plt.xlabel('x - axis')
#set the y axis label to the current axis
plt.ylabel('y - axis')
#set a tite
plt.title('sample graph!')
#display the figure
plt.show()

#-----------------------------------------------------------------
#Two or more lines 
#suitabe legend

import matplotlib.pyplot as plt
x1=[34,23,64]
y1=[34,22,72]

x2=[43,64,12]
y2=[32,43,22]

#ploting the line 1 points
plt.plot(x1,y1,label = "line1")
plt.plot(x2,y2,label = "line2")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("draw a line")
plt.legend()
plt.show()


#---------------------------------------------------------------
import matplotlib.pyplot as plt
x1=[34,23,40]
y1=[34,22,21]

x2=[43,33,12]
y2=[32,43,22]

#ploting the line 1 points
plt.plot(x1,y1,color='violet',linewidth = 3 , label = "line1")
plt.plot(x2,y2,color='yellow',linewidth = 5,label = "line2")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("draw a line")
plt.legend()
plt.show()





