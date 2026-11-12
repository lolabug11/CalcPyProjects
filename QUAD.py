# Math Calculations
from math import *
def f_of_x(formula:tuple,x:int|float, mode:int):
    if mode == 1:
        a = formula[0]
        b = formula[1]
        c = formula[2]
        return (a * x**2) + (b*x) + c
    elif mode == 2:
        #todo
        a = formula[0]
        h = formula[1]
        k = formula[2]
        return a*(x-h)**2 + k
    elif mode == 3:
        a = formula[0]
        p = formula[1]
        q = formula[2]
        return a * (x - p) * (x - q)
def get_good_num(formula:tuple, vertex:tuple,current_points:list) :
    if vertex[0] < 0 or vertex[0] == 0:
        add = True
        x_test = vertex[0] + 1
    else:
        add = False
        x_test = vertex[0] - 1
    result = 0.1

    while ".0" not in str(result) and x_test >  -20 and x_test < 20:

        print(x_test)
        y = f_of_x(formula,x_test,1)
        print(y)
        if ".0"  in str(y) and (x_test,y) not in current_points:
            point = (x_test,y)
            return point
        if add:
            x_test += 1
        else:
            x_test -= 1
    return False
def get_reflection(vertex:tuple,point_to_reflect:tuple):
    if point_to_reflect:
        distance_from_vertex = abs(vertex[0] - point_to_reflect[0])
        if point_to_reflect[0] < vertex[0]:
            new_x = vertex[0] + distance_from_vertex
        elif point_to_reflect[0] > vertex[0]:
            new_x = vertex[0] - distance_from_vertex
        else:
            new_x = "ERROR SMTH BROKE"
        new_point = (new_x,point_to_reflect[1])
        return new_point
    else:
        return False
while True:
    cho = int(input("Mode:\n> "))
    if cho == 1:
        points = []
        a = int(input("a:\n> "))
        b = int(input("b:\n> "))
        c = int(input("c:\n> "))
        point_of_sym = -b / (2*a)
        vertex = (point_of_sym, (a*point_of_sym**2) + (b * point_of_sym) + c, 0)
        points.append(vertex)
        y_intercept = (0,c)
        points.append(y_intercept)
        if y_intercept == vertex:
            print("The vertex is on the y axis: DO IT YOURSELF!!!")
        else:
            points.append(get_reflection(vertex,y_intercept))
        points.append(get_good_num((a,b,c),vertex,points))
        points.append(get_reflection(vertex,points[-1]))
        for point in points:
            print("( " + str(point[0]) + " , " + str(point[1]) + " )")
    elif cho == 2:
        a = float(input("What is the a term?\n> "))
        h = float(input("What is the h term?\n> "))
        h *= -1
        k = float(input("What is the k term?\n> "))
        b = -2*a*h
        c = f_of_x((a,h,k),0,2)
        print("Your vertex equation is", str(a) +"x^2 +",str(b)+"x +",str(c))
    elif cho == 3:
        a = float(input("What is the a term?\n> "))
        p = float(input("What is the p term?\n> ")) * -1
        q = float(input("What is the q term?\n> ")) * -1
        c = f_of_x((a,p,q), 0,3)
        b = a * ((p *-1) - q)
        print("You intercept form quadratic is equivelent to " + str(a)+"x^2 +",str(b)+"x +",str(c) )
    elif cho == 4:
        a = float(input("What is your a Term?\n> "))
        b = float(input("What is your b Term?\n> "))
        c = float(input("What is your c Term?\n> "))
        x_of_vertex = -1 * b / 2*a
        y_of_vertex = f_of_x((a,b,c),x_of_vertex,1)
        print("Your Vertex form equation is " + a +"(x -", str(x_of_vertex) +") + " + k)
