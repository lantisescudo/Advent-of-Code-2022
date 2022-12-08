from treelib import Node, Tree

class DataObj(object):
    def __init__(self,dir,size):
        self.dir = dir
        self.size = size

inputfile = "C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2022\\Day 7\\fullinput.txt"
ifilehandle = open(inputfile,"r")

tree = Tree()
pointer = None

tree.create_node(tag="/",data=DataObj(True,0))
pointer = tree.root

listing = False
for line in ifilehandle:
    tokens = line.split()

    if tokens[0] != "$" and listing == False:
        exit(-1)
    elif tokens[0] == "$" and tokens[1] == "ls":
        listing = True
    elif tokens[0] == "$" and tokens[1] == "cd":
        listing = False
        if tokens[2] == "/":
            pointer = tree.get_node(tree.root)
        elif tokens[2] == "..":
            pointer = tree.parent(pointer.identifier)
        else:
            for n in tree.children(pointer.identifier):
                if n.tag == tokens[2]:
                    pointer = n
                    break
    elif tokens[0] == "$":
        exit(-2)
    else:
        if tokens[0] == "dir":
            isdir = True
        else:
            isdir = False

        if not isdir:
            size = int(tokens[0])
            nodedata = DataObj(isdir,size)
            tree.create_node(tag=tokens[1],data=nodedata,parent=pointer)
            traverse = pointer
            while True:
                data = traverse.data
                data.size = data.size + size
                if traverse.tag == "/":
                    break
                else:
                    traverse = tree.parent(traverse.identifier)
        else:
            size = 0
            nodedata = DataObj(isdir,size)
            tree.create_node(tag=tokens[1],parent=pointer.identifier,data=nodedata)

tree.show(data_property="size")

spaceavailable = 70000000 - tree.get_node(tree.root).data.size
neededsize = 30000000 - spaceavailable
candidates = []

for n in tree.all_nodes():
    if n.data.dir == False:
        "Do Nothing"
    elif n.data.size > neededsize:
        candidates.append(n.data.size)
    else:
        "Do Nothing"

print(min(candidates))
