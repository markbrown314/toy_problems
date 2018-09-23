# BST implementation using Eytzinger Layout
class binary_search_tree:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise TypeError("input not a list")
        self.node_list = elements
    def len(self):
        return len(self.node_list)
    def right_child(self, pos):
        return 2*pos+2
    def left_child(self, pos):
        return 2*pos+1
    def parent(self, pos):
        return (pos-1)/2
    def next_pos(self, current_pos, value):
        if value <= self.node_list[current_pos]:
            return self.left_child(current_pos)
        else: 
            return self.right_child(current_pos)
    def grow(self, pos):
        if pos < len(self.node_list):
            return False
        add_list = [ None for x in range((pos - len(self.node_list))+1)]
        self.node_list += add_list
        return True
    def insert(self, value):
        pos = 0
        while self.node_list[pos] != None:
            pos = self.next_pos(pos, value)
            if pos >= self.len():
                self.grow(pos)
        self.node_list[pos] = value
        return True
    def search(self, value):
        pos = 0
        it = 0 # debug iteration count
        while value != self.node_list[pos]:
            it += 1
            pos = self.next_pos(pos, value)
            if pos >= self.len() or self.node_list[pos] == None:
                return None
        print ("iterations", it) # debug
        return self.node_list[pos]

# Test code
bst = binary_search_tree([8,4,12,2])
bst.insert(6)
bst.insert(10)
bst.insert(14)

print(bst.search(8))
print(bst.search(4))
print(bst.search(14))
print(bst.search(3.14))

print(bst.node_list)
