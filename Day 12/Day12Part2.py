inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 12\\testinput.txt"
ifilehandle = open(inputfile,"r")

grid = []

rownum = -1

startpos = []
finishpos = []

for line in ifilehandle:
    rownum += 1
    row = []
    colnum = -1
    for char in line.strip():
        colnum += 1
        if char == 'S':
            height = 0
        elif char == 'E':
            height = 25
            startpos = (rownum,colnum)
        else:
            height = ord(char)-97

        row.append(height)
    
    grid.append(row)

stepcount = 0
poslist = [startpos]
walking = True
visited = []

while walking:
    destinations = []
    stepcount += 1
    for item in poslist:
        visited.append(item)
        #Up
        if (item[0] != 0) and (grid[item[0]-1][item[1]] >= (grid[item[0]][item[1]]-1)):
            target = (item[0]-1,item[1])
            if grid[target[0]][target[1]] == 0:
                walking = False
                break
            elif (target not in destinations) and (target not in visited):
                destinations.append(target)
        #Down
        if (item[0] != len(grid)-1) and (grid[item[0]+1][item[1]] >= (grid[item[0]][item[1]]-1)):
            target = (item[0]+1,item[1])
            if grid[target[0]][target[1]] == 0:
                walking = False
                break
            elif (target not in destinations) and (target not in visited):
                destinations.append(target)
        #Left
        if (item[1] != 0) and (grid[item[0]][item[1]-1] >= (grid[item[0]][item[1]]-1)):
            target = (item[0],item[1]-1)
            if grid[target[0]][target[1]] == 0:
                walking = False
                break
            elif (target not in destinations) and (target not in visited):
                destinations.append(target)
        #Right
        if (item[1] != len(grid[0])-1) and (grid[item[0]][item[1]+1] >= (grid[item[0]][item[1]]-1)):
            target = (item[0],item[1]+1)
            if grid[target[0]][target[1]] == 0:
                walking = False
                break
            elif (target not in destinations) and (target not in visited):
                destinations.append(target)
        
        if finishpos in destinations:
            walking = False
            break
    
    poslist = destinations

print(stepcount)
