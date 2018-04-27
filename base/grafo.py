class Graph_state:
    def __init__(self, line, column, start=False):
        self.line = line
        self.column = column
        self.start = start
        self.children = []
        self.parent = None
        self.goal = False

    def isgoal(self, objective):
        if (objective[0] == self.line) and (objective[1] == self.column):
            self.goal = True

    def add(self, child):
        child.parent = self
        self.children.append(child)

    def __str__(self):
        repre = "(%d,%d)" % (self.line, self.column)
        return repre
