import matplotlib.pyplot as plt
import numpy as np
def get_points_on_line(start:int,end:int,num:int) :
    # if the amount of requested points is 1 return the given start value
    if num == 1:
        return [start]
    # calculate the step size
    step_size = (end - start)/(num-1)
    # initalize the points list with start alredy in it so you dont recalulate known values
    points = [start]
    # iterate through all the requested unknown values
    for i in range(1,num-1):
        # calculate the point and append it to the points list
        point = start + step_size * i
        points.append(point)
    # append end so you dont recalculate given values
    points.append(end)
    return points


x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y,"k-")
plt.plot(x,y,"ro")
plt.title("A")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
