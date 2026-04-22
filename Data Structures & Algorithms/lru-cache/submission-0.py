class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    '''
    We store key:value pairs in a doubly linked list, removing and inserting nodes to reflect 
    new key:value pairs, eviction, or recent use. The DLL is a spectrum from left (LRU) to right (MRU)

    Our logic is to remove and insert Nodes right before the right node when recently used, and to evict
    Nodes right after the left node, as those were least recently accessed.
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity

        # key = key, value = Node object
        self.cache = {}

        # sentinel nodes of DLL, left side means least recently used, right side means most
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # connect left and right to form a doubly linked list
        self.left.next = self.right
        self.right.prev = self.left

    # insert recently used nodes right before self.right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev

    # remove a node in-place, used for either eviction, updating value, or pre-insertion when accessed
    def remove(self, node):
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = prev

    # update DLL to reflect recent access, return value if exists
    def get(self, key: int) -> int:
        if key in self.cache:
            # before returning the value, update DLL to reflect recent use of this key:val
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    # add/update
    def put(self, key: int, value: int) -> None:
        # remove from DLL if key:val pair already in cache
        if key in self.cache:
            self.remove(self.cache[key])
        # overwrite old value with new one
        self.cache[key] = Node(key, value)
        # add back to DLL
        self.insert(self.cache[key])

        # if capacity has been reached, access lru and remove from DLL and cache
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
