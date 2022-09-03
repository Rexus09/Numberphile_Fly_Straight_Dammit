import matplotlib.pyplot as plt
import numpy as np
import sys
#Execute this file with "python3 numberphile.py 1000" to graph the first 1k points
#DEFAULTS###
colours = ["b","g","r","c","m","y","k","w"]
x_limit = 800
commands = []
color = "k."
############
try:
    commands.append(sys.argv[-1])
    commands.append(sys.argv[-2])
except Exception as x:
    print(x)
    #exit()
for command in commands:
    if command in colours:
        color = command + "."
    elif command == "-h":
        print("===============\n|| Weird Graph Help ||\n====================================================\nTo run this program you dont need any arguments\nThe only parameter you can change is the number of points computed\nex. (you want to graph 1000 points) →  python3 numberphyle.py 1000\nThe default number of pts to graph is 800\n====================================================")
        exit()
    elif command == "numberphile.py":
        print("Type -h for help on the next execution")
        print("Change color with:'b' as blue 'g' as green 'r' as red'c' as cyan'm' as magenta'y' as yellow'k' as black'w' as white")
    else:
        try:
            x_limit = int(command)
        except Exception as e:
            print("\n=========================================================================\n|| You cant enter that type of data in here ! try again or leave blank ||\n=========================================================================\n")
            exit()
def GCD(x, y):
    for i in range(1, min(x, y)+ 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd

nums_array = [i for i in range(x_limit)] #Numbers from 0 to x_limit [0,1,2...,x-1]
points_array = [1, 1] # Starting array

#For every integer [1,2,3...] we want to compute:
#We compute the GCD between nums_array[n] and the last number in points_array
#If the gcd is != 1 (they have a gcd), they do operation 1, otherwise, operation 2
for n in range(2,len(nums_array)): #Check video
    gcd_calculation = GCD(n, points_array[-1])
    if gcd_calculation != 1: 
        points_array.append( int(points_array[-1] / gcd_calculation ) )
    else:
        points_array.append(points_array[-1]+n+1)
#Plot the numbers into matplotlib
fig = plt.figure()
ax = fig.gca()
plt.title('Numberphile Graph', fontsize = 14, fontweight ='bold')
for x in nums_array:
    ax.plot(x, points_array[x],color) #Point(x, f(x))
plt.grid()
plt.show()