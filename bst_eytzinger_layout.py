class binary_search_tree:
    def __init__(self, size):
        if size <= 0:
            return None
        self.node_list = [None for x in range(size)]
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
    def insert(self, value):
        pos = 0
        while self.node_list[pos] != None:
            pos = self.next_pos(pos, value)
            if pos >= self.len():
                return False
        self.node_list[pos] = value
        return True
        
bst = binary_search_tree(10)
bst.insert(8)
bst.insert(4)
bst.insert(12)
bst.insert(2)
bst.insert(6)
bst.insert(10)
bst.insert(14)
print(bst.node_list)
