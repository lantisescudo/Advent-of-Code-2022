inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 8\\fullinput.txt"
ifilehandle = open(inputfile,"r")

treegrid = []

for line in ifilehandle:
    row = []
    for char in line.strip():
        row.append(int(char))
    treegrid.append(row)

visgrid = []
for i in range(len(treegrid)):
    row = []
    for j in range(len(treegrid[i])):
        if i == 0 or i == (len(treegrid)-1) or j == 0 or j == (len(treegrid[i])-1):
            row.append('Y')
        else:
            row.append('N')
    visgrid.append(row)

for i in range(len(treegrid)):
    maxheight = 0
    for j in range(len(treegrid[i])):
        if treegrid[i][j] > maxheight:
            maxheight = treegrid[i][j]
            visgrid[i][j] = 'Y'
            if maxheight == 9:
                break

for i in reversed(range(len(treegrid))):
    maxheight = 0
    for j in reversed(range(len(treegrid[i]))):
        if treegrid[i][j] > maxheight:
            maxheight = treegrid[i][j]
            visgrid[i][j] = 'Y'
            if maxheight == 9:
                break

for j in range(len(treegrid[0])):
    maxheight = 0
    for i in range(len(treegrid)):
        if treegrid[i][j] > maxheight:
            maxheight = treegrid[i][j]
            visgrid[i][j] = 'Y'
            if maxheight == 9:
                break

for j in reversed(range(len(treegrid[0]))):
    maxheight = 0
    for i in reversed(range(len(treegrid))):
       if treegrid[i][j] > maxheight:
            maxheight = treegrid[i][j]
            visgrid[i][j] = 'Y'
            if maxheight == 9:
                break

count = 0

for i in range(len(treegrid)):
    for j in range(len(treegrid[0])):
        if visgrid[i][j] == 'Y':
            count += 1

print(count)