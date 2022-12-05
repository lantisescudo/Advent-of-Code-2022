import re

inputfile = "C:\\Users\\Lantis\\Documents\\Advent of Code 2022\\Day 5\\fullinput.txt"
ifilehandle = open(inputfile,"r")

blocks = [[],[],[],[],[],[],[],[],[]]
instructions = []

blockcomplete = False
for line in ifilehandle:
    if line == '\n':
        "Blank line, do nothing"
    elif (line[1] == '1'):
        blockcomplete = True
    elif blockcomplete:
        parse = re.search("move (\d+) from (\d) to (\d)",line)
        instructions.append([int(parse.group(1)),int(parse.group(2))-1,int(parse.group(3))-1])
    else:
        if (line[1] != ' '):
            blocks[0].append(line[1])
        if (line[5] != ' '):
            blocks[1].append(line[5])
        if (line[9] != ' '):
            blocks[2].append(line[9])
        if (line[13] != ' '):
            blocks[3].append(line[13])
        if (line[17] != ' '):
            blocks[4].append(line[17])
        if (line[21] != ' '):
            blocks[5].append(line[21])
        if (line[25] != ' '):
            blocks[6].append(line[25])
        if (line[29] != ' '):
            blocks[7].append(line[29])
        if (line[33] != ' '):
            blocks[8].append(line[33])

for stack in range(len(blocks)):
    blocks[stack].reverse()

for move in instructions:
    for x in range(move[0]):
        blocks[move[2]].append(blocks[move[1]].pop())

ends = []
for stack in blocks:
    ends.append(stack.pop())

print(ends)

"Wait"