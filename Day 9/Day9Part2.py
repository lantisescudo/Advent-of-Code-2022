inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 9\\fullinput.txt"
ifilehandle = open(inputfile,"r")

knots = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

def movetail (lead, trail):
    if (abs(lead[0]-trail[0]) > 1) and (abs(lead[1]-trail[1]) > 1):
        if lead[1] > trail[1] and lead[0] > trail[0]:
            trail = (lead[0]-1, lead[1]-1)
        elif lead[0] > trail[0]:
            trail = (lead[0]-1,lead[1]+1)
        elif lead[1] > trail[1]:
            trail = (lead[0]+1,lead[1]-1)
        else:
            trail = (lead[0]+1,lead[1]+1)
    elif (abs(lead[0]-trail[0]) > 1):
        if lead[1] == trail[1]:
            if lead[0] > trail[0]:
                trail = (trail[0]+1, trail[1])
            else:
                trail = (trail[0]-1, trail[1])
        else:
            if lead[0] > trail[0]:
                trail = (trail[0]+1,lead[1])
            else:
                trail = (trail[0]-1,lead[1])
    elif (abs(lead[1]-trail[1]) > 1):
        if lead[0] == trail[0]:
            if lead[1] > trail[1]:
                trail = (trail[0], trail[1]+1)
            else:
                trail = (trail[0],trail[1]-1)
        else:
            if lead[1] > trail[1]:
                trail = (lead[0],trail[1]+1)
            else:
                trail = (lead[0],trail[1]-1)

    return trail

tposlist = set()

tposlist.add(knots[9])

for line in ifilehandle:
    tokens = line.split()
    head = knots[0]
    for i in range(int(tokens[1])):
        if tokens[0] == "U":
            head = (head[0],head[1]+1)
        if tokens[0] == "D":
            head = (head[0],head[1]-1)
        if tokens[0] == "R":
            head = (head[0]+1,head[1])
        if tokens[0] == "L":
            head = (head[0]-1,head[1])
        
        knots[0] = head

        for j in range(len(knots)):
            if j == 0:
                "Do Nothing"
            else:
                knots[j] = movetail(knots[j-1],knots[j])
        
        if knots[9] not in tposlist:
            tposlist.add(knots[9])

        print(knots)

print(len(tposlist))
            