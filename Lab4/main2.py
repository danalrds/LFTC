from domain import Production
from parsing import Parser


def read_part_grammar():
    non_terminals, terminals = [], []
    file_name = 'grammar.txt'
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline().strip()
        while line != 'TERMINALS':
            non_terminals.append(line)
            line = f.readline().strip()
        final_terminal = int(f.readline())
        terminals = [str(x) for x in range(final_terminal+1)]
        f.readline()
        initial_state = f.readline().strip()
    return non_terminals, terminals, initial_state


def read_productions():
    print('READ Productions:')
    productions = []
    file_name = 'productions.txt'
    with open(file_name, 'r') as f:
        line = f.readline().strip()
        while line != 'END':
            lhs = line[:line.find('->')]
            rhs = line[line.find('->') + 2:]
            rhs = rhs.split(' ')
            # print(lhs, rhs)
            p = Production(lhs, rhs)
            productions.append(p)
            line = f.readline().strip()
    for p in productions:
        print(p)
    return productions


def read_pif():
    text = ""
    sequence = []
    with open("pif.txt", "r")as f:
        line = f.readline().strip()
        while line != "":
            sequence.append(line)
            line = f.readline().strip()
    return sequence


non_terminals, terminals, initial_state = read_part_grammar()
# print(non_terminals)
# print(terminals)
# print(initial_state)
productions = read_productions()
g = Parser(non_terminals, terminals, productions, initial_state)
g.canonical_collection()
g.build_actions()
sequence = read_pif()
g.parse(sequence, g.parse_table)
g.build_parse_tree()
print('Parse tree:')
g.tree_root.bfs()
