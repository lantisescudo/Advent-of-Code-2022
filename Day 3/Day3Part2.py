inputfile = "C:\\Users\\Lantis\\Documents\\Advent of Code 2022\\Day 3\\fullinput.txt"
ifilehandle = open(inputfile,"r")

prioritysum = 0

def common_member(a, b, c):
    a_set = set(a)
    b_set = set(b)
    c_set = set(c)
    return (a_set & b_set & c_set).pop()

group = []

for line in ifilehandle:
    group.append(line.strip())
    if (len(group) < 3):
        #Do Nothing, get the next group member
        "Do Nothing"
    else:
        common = common_member(group[0],group[1],group[2])
        if ord(common) > 90:
            prioritysum += ord(common)-96
        else:
            prioritysum += ord(common)-38
        group = []

print(prioritysum)