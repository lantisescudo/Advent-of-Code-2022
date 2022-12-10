inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 10\\fullinput.txt"
ifilehandle = open(inputfile,"r")

register = 1
cyclecount = 0
rowstring = ""
crtpos = 0

adding = False
line = ifilehandle.readline()
while line:
    cyclecount += 1

    if (register in [crtpos-1,crtpos,crtpos+1]):
        rowstring = rowstring + "#"
    else:
        rowstring = rowstring + "."

    tokens = line.split()
    if tokens[0] == "noop":
        line = ifilehandle.readline()
    elif tokens[0] == "addx" and adding == False:
        adding = True
    else:
        adding = False
        register += int(tokens[1])
        line = ifilehandle.readline()

    crtpos += 1
    if (crtpos == 40):
        crtpos = 0
        print(rowstring)
        rowstring = ""

