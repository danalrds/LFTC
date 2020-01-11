class Production:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        to_string = self.lhs + '->'
        for x in self.rhs:
            to_string += x + ' '
        return to_string

    def __eq__(self, other):
        return self.lhs == other.lhs and self.rhs == other.rhs

    def __repr__(self):
        return str(self)


class Item(Production):
    def __init__(self, lhs, rhs, dot):
        Production.__init__(self, lhs, rhs)
        self.dot = dot

    def __str__(self):
        to_string = self.lhs + '->'
        for i in range(len(self.rhs)):
            if i == self.dot:
                to_string += '.'
            to_string += self.rhs[i] + ' '
        if len(self.rhs) == self.dot:
            to_string += '.'
        return to_string

    def __eq__(self, other):
        return self.lhs == other.lhs and self.rhs == other.rhs and self.dot == other.dot

    def get_production(self):
        return Production(self.lhs, self.rhs)

    def __repr__(self):
        return str(self)
