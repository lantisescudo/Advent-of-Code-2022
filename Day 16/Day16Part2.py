import re
import copy

inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 16\\fullinput.txt"
ifilehandle = open(inputfile,"r")

pattern = "Valve (\\w+) has flow rate=(\\d+); tunnels? leads? to valves? (.+)"

valves = dict()
flowvalves = set()
maxflow = 0

for line in ifilehandle:
    grps = re.search(pattern,line).groups()

    currvalve = dict()
    currvalve['flow'] = int(grps[1])
    currvalve['destlist'] = grps[2].split(", ")
    currvalve['distance'] = dict()

    valves[grps[0]] = currvalve
    if currvalve["flow"] > 0:
        flowvalves.add(grps[0])
        maxflow += currvalve["flow"]


paths = []
seenpositions = set()
paths.append({"epos": 'AA',"mpos": 'AA', "epath":['AA'], "mpath":['AA'],"open":set(), "pressure":0})

timeremain = 26
currentmax = 0

while timeremain > 0:
    nextpaths = []
    roundseen = dict()
    for p in paths:
        currentpressure = p["pressure"]
        for o in p["open"]:
            currentpressure += valves[o]['flow']

        if currentpressure > currentmax:
            currentmax = currentpressure

        if (len(p["open"]) == len(flowvalves)):
            p["pressure"] = currentpressure
            nextpaths.append(p)
            continue

        if (timeremain == 1):
            continue

        if (currentpressure + (timeremain * maxflow)) < currentmax:
            continue

        enext = copy.copy(valves[p["epos"]]['destlist'])
        enext.append(p["epos"])
        mnext = copy.copy(valves[p["mpos"]]['destlist'])
        mnext.append(p["mpos"])

        for e in enext:
            for m in mnext:
                olist = copy.copy(p["open"])
                if m == p["mpos"] and (p["mpos"] not in p["open"]) and (valves[p["mpos"]]['flow'] != 0):
                    olist.add(m)
                if e == p["epos"] and (p["epos"] not in p["open"]) and (valves[p["epos"]]['flow'] != 0):
                    olist.add(e)
                if (e,m,tuple(olist)) not in seenpositions:
                    if (e,m,tuple(olist)) not in roundseen or roundseen[(e,m,tuple(olist))] < currentpressure:
                        newepath = copy.copy(p["epath"])
                        newepath.append(e)
                        newmpath = copy.copy(p["mpath"])
                        newmpath.append(m)
                        if newepath != newmpath:
                            nextpaths.append({"epos": e,"mpos": m, "open":olist, "epath": newepath, "mpath": newmpath, "pressure":currentpressure})
                            roundseen[(e,m,tuple(olist))] = currentpressure

    for r in roundseen.keys():
        seenpositions.add(r)

    paths = nextpaths
    timeremain -= 1

    maxpressure = 0
    maxmpath = None
    maxepath = None
    for p in paths:
        if p["pressure"] > maxpressure:
            maxpressure = p["pressure"]
            maxmpath = p["mpath"]
            maxepath = p["epath"]

    print(timeremain)
    print(maxpressure)
    print(maxmpath)
    print(maxepath)

"wait"
