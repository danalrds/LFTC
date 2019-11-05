def separate(str):
    return str.replace('{', '').replace('}', '').split(',')


def loadData():
    lines = ''
    with open("automata.txt", "r")as f:
        x = f.readlines()
        for line in x:
            lines = lines + line
    content = lines.split(" ")
    states = separate(content[0])
    alphabet = separate(content[1])
    transitions = content[2].replace('{', '').replace('}', '').split(';')
    initialState = content[3]
    finalStates = separate(content[4])
    return states, alphabet, transitions, initialState, finalStates


def showAll(states, alphabet, transitions, initialState, finalStates):
    print("Finite set of states Q:")
    print(states)
    print("Alphabet:")
    print(alphabet)
    print("Transitions:")
    print(transitions)
    print("Initial state:", initialState)
    print("Final states:")
    print(finalStates)
    print()
    print()



states, alphabet, transitions, initialState, finalStates = loadData()
showAll(states, alphabet, transitions, initialState, finalStates)


def convertFAToRg(states, alphabet, transitions, initialState, finalStates):
    nonTerminals = states
    terminals = alphabet
    rules = []
    for t in transitions:
        lhs = t.split("=")[0]
        lhs = lhs.replace("delta(", "").replace(")", "")
        leftParts = lhs.split(",")
        rhs = t.split("=")[1]
        rules.append(leftParts[0] + "->" + leftParts[1] + rhs)
        if initialState in finalStates:
            rules.append(leftParts[0] + "->" + leftParts[1])
    if initialState in finalStates:
        rules.append(initialState + "->" + "E")
    print("Set of nonTerminals:")
    print(nonTerminals)
    print("Set of terminals:")
    print(terminals)
    print("Set of rules:")
    print(rules)
    print("InitialState:", initialState)


convertFAToRg(states, alphabet, transitions, initialState, finalStates)
