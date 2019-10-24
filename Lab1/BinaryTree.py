class Node:
    def __init__(self, val, pos):
        self.__val = val
        self.__pos = pos
        self.__left = None
        self.__right = None

    def getValue(self):
        return self.__val

    def getLeftChild(self):
        return self.__left

    def getRightChild(self):
        return self.__right

    def getPosition(self):
        return self.__pos

    def setLeftChild(self, child):
        self.__left = child

    def setRightChild(self, child):
        self.__right = child


class BST:
    def __init__(self):
        self.__root = None
        self.__counter = 0

    def getRoot(self):
        return self.__root

    def addElem(self, value):
        node = Node(value, self.__counter)
        if self.__root is None:
            self.__root = node
        else:
            current = self.__root
            last = current
            while current is not None:
                last = current
                if current.getValue() == node.getValue():
                    return current.getPosition()
                if node.getValue() < current.getValue():
                    current = current.getLeftChild()
                else:
                    if node.getValue() > current.getValue():
                        current = current.getRightChild()
            #if node.getValue() == last.getValue():
            #    return last.getPosition()
            if node.getValue() < last.getValue():
                last.setLeftChild(node)
            else:
                last.setRightChild(node)
        self.__counter += 1
        return node.getPosition()
