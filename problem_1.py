#!/usr/bin/env python3


class CacheNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.hashtable = dict()

        # Buffered dummy head and tail.
        self.head = CacheNode(0, 0)
        self.tail = CacheNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """If cached, moves the node to the front (MRU) position in the linked list and then returns the value.
                Else, returns -1."""
        if key not in self.hashtable:
            return -1

        node = self.hashtable[key]
        self._move_to_front(node)
        return node.value

    def set(self, key, value):
        """If the key exists, changes the node's value and moves the node to the front (MRU) position in the
        linked list. Else, creates a new node and adds it into the cache."""
        if key in self.hashtable:
            node = self.hashtable[key]
            node.value = value
            self._move_to_front(node)
        else:
            node = CacheNode(key, value)
            self._add(node)
            self.hashtable[key] = node

    def _move_to_front(self, node):
        """Move the given node to the front (MRU) position in the linked list."""
        # Bail out if the node is already in position.
        if node == self.head.next:
            return

        self._remove(node)
        self._add(node)

    def _remove(self, node):
        """Removes the given node from the linked list."""
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def _add(self, node):
        """Adds a node the front (MRU) position in the linked list), i.e. after the head."""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def clear(self):
        """Empties the cache."""
        self.hashtable.clear()
        self.head = CacheNode(0, 0)
        self.tail = CacheNode(0, 0)


if __name__ == '__main__':
    # Initialize
    cache = LRU_Cache(5)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)

    print(cache.get(1))  # returns 1
    print(cache.get(2))  # returns 2
    print(cache.get(9))  # returns -1 because 9 is not present in the cache

    cache.set(5, 5)
    cache.set(6, 6)

    print(cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
