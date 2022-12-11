inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 11\\fullinput.txt"
ifilehandle = open(inputfile,"r")

monkeys = []

currmonkey = None

for line in ifilehandle:
    line = line.strip()
    tokens = line.split()
    if len(tokens) == 0:
        "Blank Line, skip"
    elif tokens[0] == "Monkey":
        currmonkey = int(tokens[1][0])
        monkeys.insert(currmonkey, dict())
        monkeys[currmonkey]['inspectcount'] = 0
    elif tokens[0] == "Starting":
        items = []
        for i in range(2,len(tokens)):
            items.append(int(tokens[i].replace(',','')))
        monkeys[currmonkey]['items'] = items
    elif tokens[0] == "Operation:":
        if tokens[4] == "+":
            monkeys[currmonkey]['operation'] = "add"
            monkeys[currmonkey]['opval'] = int(tokens[5])
        elif tokens[5] == "old":
            monkeys[currmonkey]['operation'] = "square"
        else:
            monkeys[currmonkey]['operation'] = "mult"
            monkeys[currmonkey]['opval'] = int(tokens[5])
    elif tokens[0] == "Test:":
        monkeys[currmonkey]['testval'] = int(tokens[3])
    elif tokens[1] == "true:":
        monkeys[currmonkey]['truetarget'] = int(tokens[5])
    elif tokens[1] == "false:":
        monkeys[currmonkey]['falsetarget'] = int(tokens[5])

modproduct = 1
for m in range(len(monkeys)):
    modproduct *= monkeys[m]['testval']

for round in range(10000):
    for turn in range(len(monkeys)):
        for item in monkeys[turn]['items']:
            monkeys[turn]['inspectcount'] += 1

            if monkeys[turn]['operation'] == "square":
                newvalue = (item * item)
            elif monkeys[turn]['operation'] == "mult":
                newvalue = (item * monkeys[turn]['opval'])
            else:
                newvalue = (item + monkeys[turn]['opval'])

            if newvalue > modproduct:
                newvalue %= modproduct

            if (newvalue % monkeys[turn]['testval']) == 0:
                target = monkeys[turn]['truetarget']
            else:
                target = monkeys[turn]['falsetarget']

            monkeys[target]['items'].append(newvalue)

        monkeys[turn]['items'] = []

counts = []
for i in range(len(monkeys)):
    counts.append(monkeys[i]['inspectcount'])

print(counts)
counts.sort(reverse=True)
print(counts[0] * counts[1])