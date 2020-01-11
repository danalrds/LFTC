from domain import *


def closure(productions, element):
    print('closure(' + str(element) + ')')
    closure = [element]
    changed = True
    while changed:
        changed = False
        for item in closure:
            rhs = item.rhs[item.dot:]
            if len(rhs) > 0:
                for prod in productions:
                    # print('prod', prod)
                    # print('xdd', prod.lhs, rhs)
                    if prod.lhs == rhs[0]:
                        if Item(prod.lhs, prod.rhs, 0) not in closure:
                            changed = True
                            closure.append(Item(prod.lhs, prod.rhs, 0))
    print(closure)
    return closure


def goto(state, elem, map, productions):
    print('goto(' + str(state) + ',' + str(elem) + ')')
    res = map[state]
    for item in res:
        rhs = item.rhs[item.dot:]
        if elem in rhs and rhs.index(elem) == 0:
            newItem = Item(item.lhs, item.rhs, item.dot + 1)
            return closure(productions, newItem)
    return []
