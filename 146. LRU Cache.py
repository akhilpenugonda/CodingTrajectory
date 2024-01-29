class LRUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Use sentinel nodes for better handling of edge cases
        self.left = self.Node(0, 0)
        self.right = self.Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = self.Node(key, value)
        self._add(self.cache[key])
        if len(self.cache) > self.capacity:
            node = self.left.next
            self._remove(node)
            del self.cache[node.key]


    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.right.prev
        nxt = self.right
        p.next = nxt.prev = node
        node.next = nxt
        node.prev = p