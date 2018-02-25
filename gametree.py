class GameTree:
    def __init__(self, ref):
        self.links = []
        self.ref = ref

    def add(self, node):
        if type(node) is not type(self):
            raise TypeError("node needs to be ", type(self))
        if node is self:
            raise ValueError("circular reference to self")
        for link in self.links:
            if link is node:
                raise ValueError("node is already in link list")
        self.links.append(node)
