class Production:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return self.lhs + ' -> ' + self.rhs

    def __eq__(self, other):
        return self.lhs == other.lhs and self.rhs == other.rhs

    def __repr__(self):
        return str(self)


class Item(Production):
    def __init__(self, lhs, rhs, dot):
        Production.__init__(self, lhs, rhs)
        self.dot = dot

    def __str__(self):
        return self.lhs + ' -> ' + self.rhs[0:self.dot] + '.' + self.rhs[self.dot:]

    def __eq__(self, other):
        return self.lhs == other.lhs and self.rhs == other.rhs and self.dot == other.dot

    def get_production(self):
        return Production(self.lhs, self.rhs)

    def __repr__(self):
        return str(self)
