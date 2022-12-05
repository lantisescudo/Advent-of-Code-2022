inputfile = "C:\\Users\\Lantis\\Documents\\Advent of Code 2022\\Day 2\\fullinput.txt"
ifilehandle = open(inputfile,"r")

score = 0

for line in ifilehandle:
    opp = line[0]
    play = line[2]

    if play == 'X':
        score += 1
    elif play == 'Y':
        score += 2
    elif play == 'Z':
        score +=3
    
    if ((opp == 'A' and play == 'X') or (opp == 'B' and play == 'Y') or (opp == 'C' and play == 'Z')):
        #Draw
        score += 3
    elif ((opp == 'A' and play == 'Y') or (opp == 'B' and play == 'Z') or (opp == 'C' and play == 'X')):
        #Win
        score += 6
    else:
        #((opp == 'A' and play == 'Z') or (opp == 'B' and play == 'X') or (opp == 'C' and play == 'Y')):
        #Loss
        score +=0

print(score)