inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 9\\fullinput.txt"
ifilehandle = open(inputfile,"r")

tailpos = (0,0)
headpos = (0,0)
tposlist = set()

tposlist.add(tailpos)

for line in ifilehandle:
    tokens = line.split()
    for i in range(int(tokens[1])):
        if tokens[0] == "U":
            headpos = (headpos[0],headpos[1]+1)
        if tokens[0] == "D":
            headpos = (headpos[0],headpos[1]-1)
        if tokens[0] == "R":
            headpos = (headpos[0]+1,headpos[1])
        if tokens[0] == "L":
            headpos = (headpos[0]-1,headpos[1])
        
        if (abs(headpos[0]-tailpos[0]) > 1):
            if headpos[1] == tailpos[1]:
                if headpos[0] > tailpos[0]:
                    tailpos = (tailpos[0]+1, tailpos[1])
                else:
                    tailpos = (tailpos[0]-1, tailpos[1])
            else:
                if headpos[0] > tailpos[0]:
                    tailpos = (tailpos[0]+1,headpos[1])
                else:
                    tailpos = (tailpos[0]-1,headpos[1])
        elif (abs(headpos[1]-tailpos[1]) > 1):
            if headpos[0] == tailpos[0]:
                if headpos[1] > tailpos[1]:
                    tailpos = (tailpos[0], tailpos[1]+1)
                else:
                    tailpos = (tailpos[0],tailpos[1]-1)
            else:
                if headpos[1] > tailpos[1]:
                    tailpos = (headpos[0],tailpos[1]+1)
                else:
                    tailpos = (headpos[0],tailpos[1]-1)
        
        if tailpos not in tposlist:
            tposlist.add(tailpos)

        #print(headpos, tailpos, tposlist)

print(len(tposlist))
            