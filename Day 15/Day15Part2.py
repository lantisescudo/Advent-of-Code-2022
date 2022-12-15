import re
import array

inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 15\\fullinput.txt"
ifilehandle = open(inputfile,"r")

def distance (p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

pattern = "Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)"

sensors = []
beacons = set()
xmin = None
xmax = None
mindist = 0
maxdist = 0

for line in ifilehandle:
    coords = re.match(pattern,line).groups()
    sensor = (int(coords[0]),int(coords[1]))
    beacon = (int(coords[2]),int(coords[3]))

    dist = distance(sensor,beacon)
    sensors.append((sensor[0],sensor[1],dist))
    beacons.add(beacon)

    if (xmin == None) or (int(coords[0]) < xmin):
        xmin = int(coords[0])
        mindist = xmin - dist
    if (xmax == None) or (int(coords[0]) > xmax):
        xmax = int(coords[0])
        maxdist = xmax + dist

xstart = 0
xend = 4000000
ystart = 0
yend = 4000000

searching = True

xsearch = xstart
ysearch = ystart

while searching:
    inrange = False
    if (xsearch,ysearch) in beacons:
        xsearch += 1
        continue

    remdist = []
    for s in sensors:
        remdist.append(s[2] - distance((s[0],s[1]),(xsearch,ysearch)))
    
    disleft = max(remdist)

    if disleft == 0:
        xsearch += 1
        inrange = True
    elif disleft > 0:
        xsearch += disleft
        inrange = True
    
    if inrange:
        if xsearch > xend:
            ysearch += 1
            xsearch = 0
            continue
    else:
        searching = False
        print(xsearch,ysearch)
        print((xsearch*4000000)+ysearch)

