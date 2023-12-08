import re
import copy

inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 16\\fullinput.txt"
ifilehandle = open(inputfile,"r")

pattern = "Valve (\\w+) has flow rate=(\\d+); tunnels? leads? to valves? (.+)"

valves = dict()
flowvalves = set()

for line in ifilehandle:
    grps = re.search(pattern,line).groups()

    currvalve = dict()
    currvalve['flow'] = int(grps[1])
    currvalve['destlist'] = grps[2].split(", ")
    currvalve['distance'] = dict()

    valves[grps[0]] = currvalve
    if currvalve["flow"] > 0:
        flowvalves.add(grps[0])


paths = []
seenpositions = set()
paths.append({"path": ['AA'], "open":[], "pressure":0})

timeremain = 30

while timeremain > 0:
    nextpaths = []
    roundseen = set()
    for p in paths:
        for o in p["open"]:
            p["pressure"] += valves[o]['flow']

        if (timeremain == 1):
            continue
        if (len(p["open"]) == len(flowvalves)):
            nextpaths.append(p)
            continue
        endpos = p["path"][-1]
        if (endpos not in p["open"]) and (valves[endpos]['flow'] != 0):
            n = copy.deepcopy(p)
            n["open"].append(endpos)
            n["path"].append(endpos)
            nextpaths.append(n)
            roundseen.add((endpos,tuple(n["open"])))

        for d in valves[endpos]['destlist']:
            if (d,tuple(p["open"])) not in seenpositions:
                n = copy.deepcopy(p)
                n["path"].append(d)
                nextpaths.append(n)
                roundseen.add((d,tuple(n["open"])))
    
    for r in roundseen:
        seenpositions.add(r)
    if timeremain > 1:
        paths = nextpaths
    timeremain -= 1

maxpressure = 0
maxpath = None
for p in paths:
    if p["pressure"] > maxpressure:
        maxpressure = p["pressure"]
        maxpath = p["path"]

print(maxpressure)
print(maxpath)

"wait"