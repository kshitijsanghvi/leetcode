class Node:
    def __init__(self, key= None, value = None, prev = None, next = None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.d = defaultdict(int)
        self.n = capacity
        self.count = 0
        
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        node = self.d[key]
        if node:
            self.remove(node)
            self.append(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        node = self.d[key]
        if node:
            self.remove(node)
            self.append(node)
            node.val = value
        else:
            self.count += 1
            self.d[key] = node = Node(key = key, value = value)
            self.append(node)
            
            if self.count > self.n:
                self.d[self.head.next.key] = None
                self.count -= 1
                self.pop()

            
        
    def append(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def pop(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)