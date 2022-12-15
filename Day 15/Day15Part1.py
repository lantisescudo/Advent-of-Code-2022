import re

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


points = set()

rowcheck = 2000000

for s in sensors:
    if s[1] == rowcheck:
        continue

    distleft = s[2] - abs(rowcheck-s[1])
    if distleft >= 0 and (s[0],rowcheck) not in beacons:
        points.add((s[0]))
    
    if distleft < 0:
        "Do nothing"
    else:
        for i in range(distleft+1):
            for op in [1,-1]:
                newpoint = s[0]+(i*op)
                if (newpoint,rowcheck) not in beacons:
                    points.add(newpoint)

print(len(points))
