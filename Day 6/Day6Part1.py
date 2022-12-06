from collections import deque

inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 6\\fullinput.txt"
ifilehandle = open(inputfile,"r")

count = 0

marker = deque()

data = ifilehandle.read()

for char in data:
    if len(marker) < 3:
        marker.append(char)
        count +=1
    else:
        marker.append(char)
        count += 1
        if ((marker[0] == marker[1]) or (marker[0] == marker[2]) or (marker[0] == marker[3]) or (marker[1] == marker[2]) or (marker[1] == marker[3]) or (marker[2] == marker[3])):
            marker.popleft()
        else:
            print(count)
            break
