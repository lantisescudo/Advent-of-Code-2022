from collections import deque
from functools import cmp_to_key

inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 13\\fullinput.txt"
ifilehandle = open(inputfile,"r")

packets = []

parseline = None

def parselist ():
    retlist = []
    parsing = True
    num = ""
    while parsing:
        if len(parseline) == 0:
            return retlist[0]
        char = parseline.popleft()
        if char == '[':
            retlist.append(parselist())
        elif char == ']':
            parsing = False
            if num != "":
                retlist.append(int(num))
            return retlist
        elif char == ',':
            if num != "":
                retlist.append(int(num))
                num = ""
        elif char == '\n':
            return retlist[0]
        else:
            num = num + char

def compare (left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left],right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left,[right])
    else:
        if len(left) == 0 and len(right) > 0:
            return -1
        elif len(left) > 0 and len(right) == 0:
            return 1
        else:
            for i in range(len(left)):
                if i >= len(right):
                    return 1
                check = compare(left[i],right[i])
                if check == 0:
                    continue
                else:
                    return check
            return -1
    

for line in ifilehandle:
    if line == "\n":
        "Do Nothing"
    else:
        parseline = deque(line)
        packets.append(parselist())

packets.append([[2]])
packets.append([[6]])

sortpack = sorted(packets,key=cmp_to_key(compare))

left = 0
right = 0

for i in range(len(sortpack)):
    if sortpack[i] == [[2]]:
        left = i+1
    elif sortpack[i] == [[6]]:
        right = i+1
        break

print(left*right)