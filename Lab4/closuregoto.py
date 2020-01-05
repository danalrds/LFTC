from domain import *


def closure(productions, element):
    closure = [element]
    changed = True
    while changed:
        changed = False
        for item in closure:
            rhs = item.rhs[item.dot:]
            for prod in productions:
                if prod.lhs == rhs:
                    if Item(prod.lhs, prod.rhs, 0) not in closure:
                        changed = True
                        closure.append(Item(prod.lhs, prod.rhs, 0))
    return closure


def goto(state, elem, map, productions):
    res = map[state]
    for item in res:
        rhs = item.rhs[item.dot:]
        if rhs.find(elem) == 0:
            newItem = Item(item.lhs, item.rhs, item.dot + 1)
            return closure(productions, newItem)
    return []
