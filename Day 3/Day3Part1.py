inputfile = "C:\\Users\\Lantis\\Documents\\Advent of Code 2022\\Day 3\\fullinput.txt"
ifilehandle = open(inputfile,"r")

prioritysum = 0

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    return (a_set & b_set).pop()

for line in ifilehandle:
    common = common_member(line[len(line.strip())//2:],line[:len(line.strip())//2])
    if ord(common) > 90:
        prioritysum += ord(common)-96
    else:
        prioritysum += ord(common)-38

print(prioritysum)