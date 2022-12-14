import numpy

inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 14\\fullinput.txt"
ifilehandle = open(inputfile,"r")

xoffset = 1000
xmax = 0
ymax = 0

rocks = []

for line in ifilehandle:
    items = line.split(" -> ")
    currentrock = []
    for pair in items:
        coords = pair.split(",")
        coords = [int(coords[0]),int(coords[1])]
        currentrock.append(coords)
        if coords[0] < xoffset:
            xoffset = coords[0]
        if coords[0] > xmax:
            xmax = coords[0]
        if coords[1] > ymax:
            ymax = coords[1]
    rocks.append(currentrock)

grid = numpy.zeros((ymax+1,xmax-xoffset+1),int)

for r in range(len(rocks)):
    for point in range(len(rocks[r])):
        if point == len(rocks[r])-1:
            "Do Nothing"
        elif rocks[r][point][0] == rocks[r][point+1][0]:
            for i in range(min([rocks[r][point][1],rocks[r][point+1][1]]),max([rocks[r][point][1],rocks[r][point+1][1]])+1):
                grid[i][rocks[r][point][0]-xoffset] = 1
        else:
            for i in range(min([rocks[r][point][0],rocks[r][point+1][0]])-xoffset,max([rocks[r][point][0],rocks[r][point+1][0]])+1-xoffset):
                grid[rocks[r][point][1]][i] = 1

dropping = True
sandcount = 0
while dropping:
    falling = True
    pos = [0,500-xoffset]
    while falling:
        if pos[0] == len(grid):
            falling = False
            dropping = False
        if grid[pos[0]+1][pos[1]] == 0:
            pos[0] = pos[0]+1
        elif pos[1] == 0:
            falling = False
            dropping = False
        elif grid[pos[0]+1][pos[1]-1] == 0:
            pos[0] += 1
            pos[1] -= 1
        elif pos[1] == len(grid[pos[0]])-1:
            falling = False
            dropping = False
        elif grid[pos[0]+1][pos[1]+1] == 0:
            pos[0] += 1
            pos[1] += 1
        else:
            grid[pos[0]][pos[1]] = 2
            falling = False
            sandcount += 1

print(grid)
print(sandcount)
