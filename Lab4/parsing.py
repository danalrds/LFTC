from closuregoto import *
from nodetree import Node


def printClosure(closure):
    print("closure")
    for item in closure:
        print(item)


def findKey(map, value):
    for key in map.keys():
        if map[key] == value:
            return key
    return None


class Parser:
    def __init__(self, non_terminals, terminals, productions, initial_state):
        self.productions = productions
        self.initial_state = initial_state
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.nrStates = 0
        self.parse_table = {}
        self.actions = {}
        self.map = {}
        self.output_stack = []
        self.tree_root = Node(self.initial_state)

    def canonical_collection(self):
        self.productions.insert(0, Production('S\'', [self.initial_state]))
        symbols = self.non_terminals + self.terminals
        self.map[0] = closure(self.productions, Item('S\'', [self.initial_state], 0))
        index = 0
        while index <= self.nrStates:
            state = self.map[index]
            print('INDEX', index)
            print('STATE', state)
            for symbol in symbols:
                result = goto(index, symbol, self.map, self.productions)
                if len(result) > 0:
                    foundKey = findKey(self.map, result)
                    if not foundKey:
                        self.nrStates += 1
                        # check nothing else here before
                        self.map[self.nrStates] = result
                        self.parse_table[(index, symbol)] = self.nrStates
                    else:
                        # check nothing else here before
                        self.parse_table[(index, symbol)] = foundKey
            index += 1
        self.nrStates += 1
        # for x in map.keys():
        #    print(x)
        #    printClosure(self.map[x])
        print('PARSE TABLE:')
        for x in self.parse_table.keys():
            print(x, self.parse_table[x])

    def build_actions(self):
        for x in self.parse_table.keys():
            # check only Shift can be there before
            self.actions[x[0]] = 'Shift'
        for index in range(self.nrStates):
            if index not in self.actions:
                state = self.map[index][0]
                if state.get_production() in self.productions:
                    # check nothing else here
                    found_index = self.productions.index(state.get_production())
                    if found_index == 0:
                        self.actions[index] = 'Accept'
                    else:
                        self.actions[index] = found_index
        print('ACTIONS:')
        for key in self.actions:
            print(str(key) + ' :  ' + str(self.actions[key]))

    def parse(self, sequence):
        work_stack, input_stack = [0], sequence
        accept = False
        while not accept:
            print('Work stack')
            print(work_stack)
            top = work_stack[0]
            if self.actions[top] == 'Shift':
                # check for empty stack
                char = input_stack.pop(0)
                print('top WS', top, 'symbol', char)
                if (top, char) not in self.parse_table:
                    raise Exception('State not in can coll')
                result = self.parse_table[(top, char)]
                work_stack = [result, char] + work_stack

            elif self.actions[top] == 'Accept':
                if len(input_stack) == 0:
                    accept = True
                else:
                    raise Exception('Still things on input stack')
            else:
                reduce_action = self.actions[top]
                lhs = self.productions[reduce_action].lhs
                rhs = self.productions[reduce_action].rhs
                if len(work_stack) < 2 * len(rhs):
                    raise Exception('Not enough things on the stack!')
                # check if pop sequence is right
                right_work_stack = work_stack[:2 * len(rhs)]
                work_stack = work_stack[2 * len(rhs):]
                top = work_stack[0]
                # check if exists
                newSymbol = self.parse_table[(top, lhs)]
                work_stack = [newSymbol, lhs] + work_stack
                self.output_stack.insert(0, reduce_action)
        print('Output stack:')
        print(self.output_stack)

    def build_parse_tree(self, node):
        if len(self.output_stack) > 0:
            print(node)
            production_nr = self.output_stack.pop(0)
            rhs = self.productions[production_nr].rhs
            for x in rhs:
                node.children.append(Node(x))
            for x in node.children:
                if x.value in self.non_terminals:
                    self.build_parse_tree(x)

    def build_parse_tree(self):
        queue = [self.tree_root]
        while len(queue) > 0:
            node = queue.pop(0)
            production_nr = self.output_stack.pop(0)
            rhs = self.productions[production_nr].rhs
            for x in rhs:
                new_node = Node(x)
                node.children.append(new_node)
                if x in self.non_terminals:
                    queue.append(new_node)
