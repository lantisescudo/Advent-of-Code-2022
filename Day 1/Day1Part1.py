inputfile = "C:\\Users\\Lantis\\Documents\\Advent of Code 2022\\Day 1\\fullinput.txt"
ifilehandle = open(inputfile,"r")

elves = []

currentelf = []
for line in ifilehandle:
    if line == "\n":
        elves.append(currentelf)
        currentelf = []
    else:
        currentelf.append(int(line))

elves.append(currentelf)

elfsums = []
for e in elves:
    elfsums.append(sum(e))

print(max(elfsums))
