from parsing import *
from closuregoto import *


def printClosure(closure):
    print("closure")
    for item in closure:
        print(item)


def doIt(productions):
    item = Item('S\'', 'S', 0)
    item2 = Item('S\'', 'S', 1)
    item3 = Item('S\'', 'aA', 1)
    item4 = Item('S\'', 'aA', 2)
    item5 = Item('A', 'bA', 1)
    for p in productions:
        print(p)
    map = {}
    map[0] = closure(productions, item)
    map[1] = goto(0, 'S', map, productions)
    map[2] = goto(0, 'a', map, productions)
    map[3] = goto(2, 'A', map, productions)
    map[4] = goto(2, 'b', map, productions)
    map[5] = goto(2, 'c', map, productions)
    map[6] = goto(4, 'A', map, productions)
    printClosure(map[6])


p0 = Production('S\'', 'S')
p1 = Production('S', 'aA')
p2 = Production('A', 'bA')
p3 = Production('A', 'c')
productions = [p1, p2, p3]

non_terminals = ['S', 'A']
terminals = ['a', 'b', 'c']
g = Parser(non_terminals, terminals, productions, 'S')
g.canonical_collection()
g.build_actions()
g.parse('abbc')
g.build_parse_tree()
print('Parse tree:')
g.tree_root.bfs()
