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
        terminals = [str(x) for x in range(final_terminal)]
        f.readline()
        initial_state = f.readline().strip()
    return non_terminals, terminals, initial_state


def read_productions():
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
    return productions


non_terminals, terminals, initial_state = read_part_grammar()
# print(non_terminals)
# print(terminals)
# print(initial_state)
productions = read_productions()
g = Parser(non_terminals, terminals, productions, initial_state)
g.canonical_collection()
