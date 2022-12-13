from collections import deque

inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 13\\fullinput.txt"
ifilehandle = open(inputfile,"r")

pairs = []

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
            return True
        elif left > right:
            return False
        else:
            return None
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left],right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left,[right])
    else:
        if len(left) == 0 and len(right) > 0:
            return True
        elif len(left) > 0 and len(right) == 0:
            return False
        else:
            for i in range(len(left)):
                if i >= len(right):
                    return False
                check = compare(left[i],right[i])
                if check is None:
                    continue
                else:
                    return check
            return True
    

#Parse into pairs
reading = True
while reading:
    line = ifilehandle.readline()
    parseline = deque(line)
    pairleft = parselist()
    
    line = ifilehandle.readline()
    parseline = deque(line)
    pairright = parselist()

    pairs.append([pairleft,pairright])

    line = ifilehandle.readline()
    if line == "":
        reading = False

correctindexes = []
#Compare

for i in range(len(pairs)):
    if compare(pairs[i][0],pairs[i][1]):
        correctindexes.append(i+1)

print(correctindexes)
print(sum(correctindexes))
