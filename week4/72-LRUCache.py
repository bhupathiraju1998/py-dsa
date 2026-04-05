class Node:
    def __init__(self,key,value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value 

class LRUCache:
    def __init__(self,capacity:int):
        self.capacity = capacity 
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail 
        self.tail.prev = self.head
    
    def _remove(self,node):
        prev,next = node.prev,node.next
        prev.next = next 
        next.prev = prev
    
    def _insert(self,node):
        node.next = self.head.next
        node.prev = self.head 
        # Node None<->newnode<->Node A but we need t ohandle none next and node a prev to connect to this new node

        self.head.next.prev = node
        self.head.next = node 

    def get(self,key:int)->int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1
    # head <-> most_recent ... least_recent <-> tail intitution
    
    def put(self,key:int,value:int)->None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key,value)
        self.cache[key] = node
        self._insert(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

if __name__ == "__main__":
    lru = LRUCache(2)

    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))  # 1

    lru.put(3, 3)      # evicts key 2
    print(lru.get(2))  # -1

    lru.put(4, 4)      # evicts key 1
    print(lru.get(1))  # -1
    print(lru.get(3))  # 3
    print(lru.get(4))  # 4
