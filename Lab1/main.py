from BinaryTree import BST
import re


def loadCodificationTable():
    map = {}
    reservedWords = []
    separators = [" ", "\n"]
    operands = []
    with open("codification.txt", "r")as f:
        line = f.readline()
        i = 1
        while line != "":
            x = line.strip()
            map[x] = i
            if i > 2:
                reservedWords.append(x)
            i += 1
            line = f.readline()
    with open("operands.txt", "r")as f:
        line = f.readline()
        while line != "":
            x = line.strip()
            map[x] = i
            operands.append(x)
            i += 1
            line = f.readline()
    with open("separators.txt", "r")as f:
        line = f.readline()
        while line != "":
            x = line.strip()
            separators.append(x)
            i += 1
            line = f.readline()
    return map, reservedWords, separators, operands


def loadProgramText():
    text = ""
    with open("text1.txt", "r")as f:
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
    map, reserved, separators, operands = loadCodificationTable()
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
        sep = ""
        while i < length and text[i] in separators:
            if text[i] == "'":
                if sep != '':
                    pif.append((map[sep], -1))
                    sep = ""
                assert (text[i + 2] == "'")
                position = bstConstants.addElem("'" + text[i + 1] + "'")
                pif.append((2, position))
                print('then branch', position, text[i + 1])
                i += 2
            else:
                if text[i] not in ignorable:
                    if possibleSeparator(sep + text[i], operands):
                        sep += text[i]
                    else:
                        if sep != '':
                            code = map[sep]
                            pif.append((code, -1))
                        sep = text[i]
            i += 1
        if sep in operands:
            pif.append((map[sep], -1))
    print('IDENTIFIERS:')
    printBST(bstIdentifiers.getRoot())
    print('CONSTANTS')
    printBST(bstConstants.getRoot())
    print('PIF')
    for x in pif:
        print(x[0])
    return pif, bstIdentifiers, bstConstants


def possibleSeparator(prefix, operands):
    for op in operands:
        if op.find(prefix) == 0:
            return True
    return False


def validIdentifier(word):
    return word[0] in "abcdefghijklmnopqrstuvwxyz" and len(word) <= 250


def validNumber(word):
    # RE_INT = re.compile(r'^[-+]?([1-9]\d*|0)$')
    return re.match("^[-+]?([1-9]\d*|0)$", word)


pif, ist, cst = solve()
# map, reserved, separators, operands = loadCodificationTable()
# print(operands)
# print(reserved)
# print(separators)
# print(map)
