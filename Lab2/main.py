def checkOneWithEpsilon(rules, initialState):
    for rule in rules:
        parts = rule.split("->")
        lhs = parts[0]
        rightParts = parts[1]
        for rhs in rightParts:
            if lhs == initialState and rhs == "E":
                return True
    return False


def obtainTransitions(nonTerminals, terminals, rules):
    transitions = []
    for rule in rules:
        parts = rule.split("->")
        lhs = parts[0]
        rightParts = parts[1].split("|")
        for rhs in rightParts:
            if rhs in terminals:
                transitions.append("delta(" + lhs + "," + rhs + ")=K")
            if len(rhs) > 1 and rhs[0] in terminals and rhs[1] in nonTerminals:
                transitions.append("delta(" + lhs + "," + rhs[0] + ")=" + rhs[1])
    return set(transitions)


def convertRGToFA(nonTerminals, terminals, rules, initialState):
    QSetOfStates = nonTerminals
    QSetOfStates.add("K")
    alphabet = terminals
    finalStates = ["K"]
    if checkOneWithEpsilon(rules, initialState):
        finalStates.append(initialState)
    transitions = obtainTransitions(nonTerminals, terminals, rules)
    print("Finite set of states Q:")
    print(QSetOfStates)
    print("Alphabet:")
    print(alphabet)
    print("Transitions:")
    print(transitions)
    print("Initial state:", initialState)
    print("Final states:")
    print(finalStates)


def checkRule(nonTerminals, terminals, rule):
    parts = rule.split("->")
    lhs = parts[0]
    rhs = parts[1]
    if lhs not in nonTerminals:
        return False
    rightParts = rhs.split("|")
    for part in rightParts:
        if part == "E":
            continue
        if "^" in part:
            return False
        if part[0] in nonTerminals and part[1] in nonTerminals:
            return False
        if len(part) > 1 and part[0] in terminals and part[1] in terminals:
            return False
    return True


def checkGrammar(nonTerminals, terminals, rules):
    ok = True
    for rule in rules:
        if not checkRule(nonTerminals, terminals, rule):
            ok = False
            break
    if ok:
        print("Grammar is regular")
    else:
        print("Grammar is not regular")
    return ok


def showAll(nonTerminals, terminals, rules, initial):
    print("Set of nonTerminals:")
    print(nonTerminals)
    print("Set of terminals:")
    print(terminals)
    print("Set of rules:")
    print(rules)
    print("InitialState:", initialState)
    for nt in nonTerminals:
        print("Rules for ", nt)
        showRulesForNnTerminal(rules, nt)
    print()
    print()


def showRulesForNnTerminal(rules, nonTerminal):
    for rule in rules:
        if nonTerminal in rule and rule.split("->")[0] == nonTerminal:
            print(rule)


def separate(str):
    return str.replace('{', '').replace('}', '').split(',')


def loadData():
    lines = ''
    with open("grammar.txt", "r")as f:
        x = f.readlines()
        for line in x:
            lines = lines + line
    content = lines.split(" ")
    nonTerminals = separate(content[0])
    terminals = separate(content[1])
    rules = separate(content[2])
    initialState = content[3]
    return set(nonTerminals), set(terminals), set(rules), initialState


nonTerminals, terminals, rules, initialState = loadData()
showAll(nonTerminals, terminals, rules, initialState)
ok = checkGrammar(nonTerminals, terminals, rules)

if ok:
    convertRGToFA(nonTerminals, terminals, rules, initialState)
