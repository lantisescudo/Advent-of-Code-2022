inputfile = "C:\\Users\\Lantis\\Documents\\Advent of Code 2022\\Day 2\\fullinput.txt"
ifilehandle = open(inputfile,"r")

score = 0

for line in ifilehandle:
    opp = line[0]
    play = line[2]

    if opp == 'A': #Rock
        if play == 'X': #Scissors
            score += 3
        elif play == 'Y': #Rock
            score += (3+1)
        else: #Paper
            score += (6+2)
    elif opp == 'B': #Paper
        if play == 'X': #Rock
            score += 1
        elif play == 'Y': #Paper
            score += (3+2)
        else: #Scissors
            score += (6+3)
    else: #Scissors
        if play == 'X': #Paper
            score += 2
        elif play == 'Y': #Scissors
            score += (3+3)
        else: #Rock
            score += (6+1)

print(score)