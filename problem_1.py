#!/usr/bin/env python3


class CacheNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache:

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
        if self.capacity == 0:
            return -1

        # Return -1 if a falsey is given for the key or the key is not in the cache.
        if not bool(key) or key not in self.hashtable:
            return -1

        node = self.hashtable[key]
        self._move_to_front(node)
        return node.value

    def set(self, key, value):
        """If the key exists, changes the node's value and moves the node to the front (MRU) position in the
        linked list. Else, creates a new node and adds it into the cache."""
        if self.capacity == 0:
            return -1

        # Return -1 if a falsey is given for the key.
        if not bool(key):
            return -1

        if key in self.hashtable:
            node = self.hashtable[key]
            node.value = value
            self._move_to_front(node)
        else:
            node = CacheNode(key, value)
            self._add(node)
            self.hashtable[key] = node

        # If the cache is overcapacity, remove the last node.
        if len(self.hashtable) > self.capacity:
            self._remove_lru()

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

    def _remove_lru(self):
        """Removes the LRU node (previous to the tail) from the linked list."""
        node = self.tail.prev
        self._remove(node)
        del self.hashtable[node.key]

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

    def run_edge_case_0_capacity():
        print('Running edge case for 0 capacity...')
        cache = LRU_Cache(0)

        print(cache.set(1, 1))      # -1
        print(cache.set(2, 2))      # -1

        print(cache.get(1))         # -1
        print(cache.get(2))         # -1

        print(len(cache.hashtable))  # 0

    def run_edge_case_with_falsey_given():
        print('\nRunning edge case for falsey given...')
        cache = LRU_Cache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        # Test an edge cases.
        print(cache.get(None))      # -1
        print(cache.get(0))         # -1
        print(cache.get(False))     # -1
        print(cache.set('', 2))     # -1

    def run_edge_case_when_not_in_cache():
        print('\nRunning edge case when not in cache...')
        cache = LRU_Cache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        # Test an edge cases.
        print(cache.get(10))        # -1
        print(cache.get(14))        # -1
        print(cache.get(-4))        # -1

        # Test when run over capacity.
        cache.set(5, 5)
        cache.set(6, 6)
        print(cache.get(1))         # -1
        print(cache.get(2))         # 2

    def run_test_last_recently_used():
        print('\nRunning multiple tests....')
        # Initialize
        cache = LRU_Cache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        print(cache.get(1))     # 1
        print(cache.get(2))     # 2
        print(cache.get(9))     # -1 because 9 is not present in the cache

        cache.set(5, 5)
        cache.set(6, 6)
        print(cache.get(3))     # -1 because the cache reached it's capacity and 3 was the least recently used entry
        print(list(cache.hashtable.keys()))  # [1, 2, 4, 5, 6]


    run_edge_case_0_capacity()
    run_edge_case_with_falsey_given()
    run_edge_case_when_not_in_cache()
    run_test_last_recently_used()
