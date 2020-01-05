class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

    def bfs(self):
        queue = [self]
        index = 0
        while len(queue) > 0:
            length = len(queue)
            print('Row', index)
            for i in range(length):
                front = queue.pop(0)
                print(front)
                for node in front.children:
                    queue.append(node)
            index += 1
