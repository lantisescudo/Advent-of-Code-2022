inputfile = "C:\\Users\\Lantis\\Documents\\Advent of Code 2022\\Day 4\\fullinput.txt"
ifilehandle = open(inputfile,"r")

overlaps = 0

for line in ifilehandle:
    line = line.strip()
    pair = line.split(',')
    pair_a = pair[0].split('-')
    pair_b = pair[1].split('-')
    elf_a = [int(pair_a[0]),int(pair_a[1])]
    elf_b = [int(pair_b[0]),int(pair_b[1])]
    
    if not(((elf_a[0] < elf_b[0]) and (elf_a[1] < elf_b[0])) or ((elf_a[0] > elf_b[0]) and (elf_b[1] < elf_a[0]))):
        overlaps +=1

print(overlaps)