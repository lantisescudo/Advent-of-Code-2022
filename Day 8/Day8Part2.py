inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 8\\fullinput.txt"
ifilehandle = open(inputfile,"r")

treegrid = []

for line in ifilehandle:
    row = []
    for char in line.strip():
        row.append(int(char))
    treegrid.append(row)

scoregrid = []
for i in range(len(treegrid)):
    row = []
    for j in range(len(treegrid[i])):
        row.append(0)
    scoregrid.append(row)

maxscore = 0

for i in range(len(treegrid)):
    for j in range(len(treegrid[0])):
        height = treegrid[i][j]

        if i==0 or j==0 or i==len(treegrid)-1 or j==len(treegrid[i])-1:
            continue

        scores = [1,1,1,1]
        #Walk right
        y=j+1
        while y < len(treegrid[i])-1 and (treegrid[i][y] < height):
            scores[0] += 1
            y += 1
        #Walk left
        y=j-1
        while y > 0 and (treegrid[i][y] < height):
            scores[1] += 1
            y -= 1
        #Walk down
        x=i+1
        while x < len(treegrid)-1 and (treegrid[x][j] < height):
            scores[2] += 1
            x += 1
        #Walk up
        x=i-1
        while x > 0 and (treegrid[x][j] < height):
            scores[3] += 1
            x -= 1

        scoregrid[i][j] = scores[0] * scores[1] * scores[2] * scores[3]
        if scoregrid[i][j] > maxscore:
            maxscore = scoregrid[i][j]
        

print(maxscore)