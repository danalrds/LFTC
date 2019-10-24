from BinaryTree import BST


def loadCodificationTable():
    map = {}
    reservedWords = []
    separators = [" ", "\n"]
    with open("codification.txt", "r")as f:
        line = f.readline()
        i = 1
        while line != "":
            x = line.strip()
            map[x] = i
            if i > 2:
                reservedWords.append(x)
            if i > 10:
                separators.append(x)
            i += 1
            line = f.readline()
    return map, reservedWords, separators


def loadProgramText():
    text = ""
    with open("cmmdc.txt", "r")as f:
        line = f.readline()
        while line != "":
            text = text + line
            line = f.readline()
    return text


def printBST(node):
    if node is None:
        return
    else:
        print(node.getValue(), node.getPosition())
        printBST(node.getLeftChild())
        printBST(node.getRightChild())


def solve():
    map, reserved, separators = loadCodificationTable()
    text = loadProgramText()
    ignorable = [" ", "\n"]
    pif = []
    bstIdentifiers = BST()
    bstConstants = BST()
    i = 0
    length = len(text)
    while i < length:
        word = ""
        while text[i] not in separators:
            word += text[i]
            i += 1

        if word in reserved:
            code = map[word]
            pif.append((code, -1))
        elif validIdentifier(word):
            position = bstIdentifiers.addElem(word)
            pif.append((1, position))
        elif validNumber(word):
            position = bstConstants.addElem(word)
            pif.append((2, position))
        else:
            raise Exception("Invalid token!")

        while i < length and text[i] in separators:
            current = text[i]
            if text[i] == "'":
                assert(text[i + 2] == "'")
                position = bstConstants.addElem("'"+text[i + 1]+"'")
                pif.append((2, position))
                i += 2
            elif current not in ignorable:
                code = map[current]
                pif.append((code, -1))
            i += 1
    printBST(bstIdentifiers.getRoot())
    print("*" * 10)
    printBST(bstConstants.getRoot())
    print("*" * 10)
    for x in pif:
        print(x)
    return pif, bstIdentifiers, bstConstants


def validIdentifier(word):
    return word[0] in "abcdefghijklmnopqrstuvwxyz"


def validNumber(word):
    try:
        int(word)
        return True
    except ValueError:
        return False


pif, ist, cst = solve()
