inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 10\\fullinput.txt"
ifilehandle = open(inputfile,"r")

register = 1
cyclecount = 0
signalstrength = 0

adding = False
line = ifilehandle.readline()
while line:
    cyclecount += 1

    if (cyclecount % 40) == 20:
        signalstrength += (cyclecount * register)
        print(register)

    tokens = line.split()
    if tokens[0] == "noop":
        line = ifilehandle.readline()
    elif tokens[0] == "addx" and adding == False:
        adding = True
    else:
        adding = False
        register += int(tokens[1])
        line = ifilehandle.readline()

    if cyclecount > 220:
        break

print(signalstrength)