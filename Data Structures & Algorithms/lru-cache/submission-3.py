class Node:
    def __init__(self, key,val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None



class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def insert_node(self,node: Node) -> None:
        if self.size == 0:
            self.head.next = node
            node.prev = self.head
            node.next = self.tail
            self.tail.prev = node
        
        else:
            curr_tail = self.tail.prev
            curr_tail.next = node
            node.prev = curr_tail
            node.next = self.tail
            self.tail.prev = node

    def pop_node(self, node: Node):
        if node == self.head or node == self.tail:
            return None

        node.prev.next = node.next    
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        return node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            n = self.pop_node(node)
            self.insert_node(n)
            return n.val
        
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            n = self.pop_node(node)
            self.insert_node(n)
        
        else:
            if self.size < self.cap:
                node = Node(key,value)
                self.insert_node(node)
                self.cache[key] = self.tail.prev
                self.size+=1
            
            else:
                del_node = self.pop_node(self.head.next)
                del self.cache[del_node.key]
                node = Node(key,value)
                self.insert_node(node)
                self.cache[key] = self.tail.prev








        
