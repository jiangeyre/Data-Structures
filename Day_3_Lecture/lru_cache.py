import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.ordering = DoublyLinkedList()
        self.size = 0
        self.limit = limit
        self.storage = {}

    def __len__(self):
        return self.size

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # check to see that the key is in our cache
        if key in self.storage:
            # fetch the DLL node which is the value of this key
            node = self.storage[key]
            self.ordering.move_to_front(node)

            return node.value[1] # get second value in the tuple
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # check if key is in the cache
        if key in self.storage:
            node = self.storage[key]
            # overwrite the old value
            node.value = (key, value)
            # move this node to the tail
            self.ordering.move_to_end(node)

            return
        if self.size is self.limit:
            # evict the least recently used element
            oldest_key = self.ordering.head.value[0]
            del self.storage[oldest_key]
            # remove the head node from the DLL
            self.ordering.remove_from_head()
            self.size -= 1

        # key is not in the self.storage and we still have room in our cache
        # add the key and value    
        self.ordering.add_to_tail((key, value))
        self.storage[key] = self.ordering.tail
        self.size += 1 
