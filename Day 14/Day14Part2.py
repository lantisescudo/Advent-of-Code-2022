inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 14\\fullinput.txt"
ifilehandle = open(inputfile,"r")

xoffset = 1000
xmax = 0
ymax = 0

rocks = []
occupied = set()

def sandfill (y,x):
    if (y,x) in occupied:
        return
    if y == (ymax+2):
        return
    for i in [-1, 0, 1]:
        sandfill(y+1, x+i)
    occupied.add((y,x))

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

for r in range(len(rocks)):
    for point in range(len(rocks[r])):
        if point == len(rocks[r])-1:
            "Do Nothing"
        elif rocks[r][point][0] == rocks[r][point+1][0]:
            for i in range(min([rocks[r][point][1],rocks[r][point+1][1]]),max([rocks[r][point][1],rocks[r][point+1][1]])+1):
                newpoint = (i,rocks[r][point][0])
                if newpoint not in occupied:
                    occupied.add(newpoint)
        else:
            for i in range(min([rocks[r][point][0],rocks[r][point+1][0]]),max([rocks[r][point][0],rocks[r][point+1][0]])+1):
                newpoint = (rocks[r][point][1],i)
                if newpoint not in occupied:
                    occupied.add(newpoint)

dropping = True
sandcount = 0

startcount = len(occupied)
sandfill(0,500)
sandcount = len(occupied)-startcount

print(sandcount)
