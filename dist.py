import sys
import math

input = sys.argv
# input example 5,2 4,5 for dist
# input example 5,2 4,5 m for mid
x1,y1 = input[1].split(',')
x2,y2 = input[2].split(',')

def dist_func(x1,y1,x2,y2):
    dist = math.sqrt((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2)
    print(f"distance: {dist}")

print(input,len(input))
print(f"x1: {x1}\ny1: {y1}\nx2: {x2}\ny2: {y2}")

if len(input) == 3:
    dist_func(x1,y1,x2,y2)
