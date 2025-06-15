from node import Node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity : int = capacity
        self.cache = {}
        self.head : Node = Node()
        self.tail : Node = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node: Node):
        current_first = self.head.next
        
        node.prev = self.head
        node.next = current_first

        self.head.next = node 
        current_first.prev = node
    
    def _remove_node(self, node):
        left_neighbor = node.prev
        right_neighbor = node.next

        left_neighbor.next = right_neighbor
        right_neighbor.prev = left_neighbor
    
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        return lru_node
    
    def get(self, key):
        node : Node = self.cache.get(key)
        if not node:
            return None
        self._move_to_head(node)
        return node.value
    
    def put(self, key, value):
        existing_node = self.cache.get(key)
        if existing_node:
            existing_node.value = value
            # no need to update the self.cache
            # (it holds the reference to the existing_node) already
            self._move_to_head(existing_node)
            return existing_node.value
        node = Node(key, value)
        self._add_node(node)
        self.cache[key] = node
        # applying LRU eviction policy here.
        if len(self.cache) > self.capacity:
            tail = self._pop_tail()
            del self.cache[tail.key]