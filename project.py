#this code involes a robot considered as R in a grid with obstacles in it
#the robot reaches the end of the grid surpassing the all the obstacles ahead of it


import random

rows, cols = 4, 5

# A grid of 4*5
grid = [['o' for _ in range(cols)] for _ in range(rows)]

# Number of 'X' to place,considering 'X' as obstacles
num_x = 5
num_y= 1


for _ in range(num_x): #'X' osbstacles are randomly placed in the grid
    while True:
        i = random.randint(0, rows - 1)
        j = random.randint(0, cols - 1)
        if grid[i][j] == 'o':
            grid[i][j] = 'X'
            break
        
for _ in range(0,1):
    while True:
        i = random.randint(0, rows - 1)
        j = random.randint(0, cols - 1)
        if grid[i][j] == 'o':
            grid[i][j] = 'R'
            break
        
# Print the grid
for row in grid:
    print(' '.join(row))
print()
    
    
def find_r_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'R':
                return (i, j)
    return None
    
p,q=find_r_position(grid)
print(p,q)

ev=p%2
print(ev)
if (ev==0):
 for i in range(p,p+1):
    for j in range(q,cols):
     while grid[i][j]=='o':
        grid[i][j]='R'
else:
 for i in range(p,p+1):
    for j in range(q-1,-1,-1):
      while grid[i][j]=='o':
        grid[i][j]='R'
        
for row in grid:
    print(' '.join(row))
print()


while(p<3):
    p=p+1
    even=p%2
    if even==0:
     for i in range(p,p+1):
       for j in range(0,cols):
         while grid[i][j]=='o':
            grid[i][j]='R'
            for row in grid:
               print(' '.join(row))
         print()
    
    else:
     for i in range(p,p+1):
       for j in range(cols-1,-1,-1):
         while grid[i][j]=='o':
            grid[i][j]='R'
            for row in grid:
               print(' '.join(row))
         print()
         
