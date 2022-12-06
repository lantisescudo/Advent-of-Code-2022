from collections import deque

inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 6\\fullinput.txt"
ifilehandle = open(inputfile,"r")

count = 0

marker = deque()

data = ifilehandle.read()

for char in data:
    if len(marker) < 13:
        marker.append(char)
        count +=1
    else:
        marker.append(char)
        count += 1
        seen = set()
        dup = False
        for item in marker:
            if item in seen:
                marker.popleft()
                dup = True
                break
            else:
                seen.add(item)
        
        if not dup:
            print(count)
            break
        
