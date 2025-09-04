import sys
import math

input = sys.argv
# input example 5,2 4,5 for dist
# input example 5,2 4,5 m for mid
x1,y1 = input[1].split(',')
x2,y2 = input[2].split(',')

def dist_func(x1,y1,x2,y2):
    """Prints out the distance of two points on a cartesian plane

    Keyword arguments:
    
    x1 (int): x coordinate of point 1
    y1 (int): y coordinate of point 1
    x2 (int): x coordinate of point 2
    y2 (int): y coordinate of point 2
    """
    dist = math.sqrt((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2)
    print(f"distance: {dist}")


def mid_point_func(x1,y1,x2,y2):
        """Prints out the mid point coordinate of two points on a cartesian plane

    Keyword arguments:
    
    x1 (int): x coordinate of point 1
    y1 (int): y coordinate of point 1
    x2 (int): x coordinate of point 2
    y2 (int): y coordinate of point 2
    """
    mx = (int(x1) + int(x2)) / 2
    ym = (int(y1) + int(y2)) / 2
    print("midpoint is: {}. {}".format(mx,ym))

print(input,len(input))
print(f"x1: {x1}\ny1: {y1}\nx2: {x2}\ny2: {y2}")

if len(input) == 3:
    dist_func(int(x1),int(y1),int(x2),int(y2))
elif len(input) == 4:
    mid_point_func(int(x1),int(y1),int(x2),int(y2))
