class tree_node:
    """ This is a tree node """
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value

    def check_child(self, value):
        if not isinstance(value, tree_node):
            raise ValueError("value is not an instance of tree_node")

    def set_right_child(self, child):
        self.check_child(child)
        self.right_child = child

    def set_left_child(self, child):
        self.check_child(child)
        self.left_child = child

    def __repr__(self):
        rep = "node: " + str(self.value)
        rep += " left: "
        if self.left_child == None:
            rep += "[None]"
        else: rep += str(self.left_child.value)
        rep += " right: "
        if self.right_child == None:
            rep += "[None]"
        else: rep += str(self.right_child.value)
        return rep

    def get_right_child(self): return self.right_child
    def get_left_child(self): return self.left_child

    right = property(get_right_child, set_right_child)
    left = property(get_left_child, set_left_child)
    
#class binary_search_tree:
#    def __init__(self, elements):

a = tree_node(1)
b = tree_node(2)
c = tree_node(3)

a.right = b
a.left = c
print(a)
