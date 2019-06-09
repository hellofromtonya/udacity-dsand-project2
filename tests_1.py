#!/usr/bin/env python3

import unittest
from problem_1 import LRU_Cache, CacheNode


class Test_LRU_Cache(unittest.TestCase):
    """
    Test the LRU_Cache methods.
    """

    def test_lrucache_set_new_nodes(self):
        """
        LRU_Cache::set() - test set with new nodes.
        """
        # Set up.
        cache = LRU_Cache(5)
        test_data = {
            'udacity': 1,
            'python': 2,
            100: 'hello world',
            200: 'algorithms'
        }

        # Test set stores each item.
        for key, value in test_data.items():
            self.assertFalse(key in cache.hashtable)
            cache.set(key, value)
            self.assertTrue(key in cache.hashtable)

        # Test each node in the linked list.
        node = cache.head.next
        self.assertEqual(cache.hashtable[200], node)
        self.assertEqual('algorithms', node.value)
        self.assertEqual(200, node.key)
        node = node.next
        self.assertEqual(cache.hashtable[100], node)
        self.assertEqual('hello world', node.value)
        self.assertEqual(100, node.key)
        node = node.next
        self.assertEqual(cache.hashtable['python'], node)
        self.assertEqual(2, node.value)
        self.assertEqual('python', node.key)
        node = node.next
        self.assertEqual(cache.hashtable['udacity'], node)
        self.assertEqual(1, node.value)
        self.assertEqual('udacity', node.key)

        # Test the tail node.
        self.assertEqual(cache.hashtable['udacity'], cache.tail.prev)

        # Clean up.
        cache.clear()

    def test_lrucache_set_existing_nodes(self):
        """
        LRU_Cache::set() - test set with existing nodes.
        """
        # Set up.
        cache = LRU_Cache(5)
        test_data = {
            'udacity': 1,
            'python': 2,
            100: 'hello world',
            200: 'algorithms'
        }
        for key, value in test_data.items():
            cache.set(key, value)

        #
        # Test a node in the middle.
        #

        # Test set overwrites value in the existing node.
        prev_number_items = len(cache.hashtable)
        self.assertEqual(2, cache.hashtable['python'].value)
        cache.set('python', 20)
        self.assertEqual(20, cache.hashtable['python'].value)
        self.assertEqual(prev_number_items, len(cache.hashtable))

        # Test that the node was moved to the MRU position.
        node = cache.head.next
        self.assertEqual(cache.hashtable['python'], node)
        self.assertEqual(20, node.value)
        self.assertEqual('python', node.key)

        # Test the wiring in the rest of the linked list.
        node = node.next
        self.assertEqual(cache.hashtable[200], node)
        self.assertEqual('algorithms', node.value)
        self.assertEqual(200, node.key)
        node = node.next
        self.assertEqual(cache.hashtable[100], node)
        self.assertEqual('hello world', node.value)
        self.assertEqual(100, node.key)
        node = node.next
        self.assertEqual(cache.hashtable['udacity'], node)
        self.assertEqual(1, node.value)
        self.assertEqual('udacity', node.key)
        self.assertEqual(cache.hashtable['udacity'], cache.tail.prev)

        #
        # Test the last node.
        #

        # Test set overwrites value in the existing node.
        prev_number_items = len(cache.hashtable)
        self.assertEqual(1, cache.hashtable['udacity'].value)
        cache.set('udacity', 10)
        self.assertEqual(10, cache.hashtable['udacity'].value)
        self.assertEqual(prev_number_items, len(cache.hashtable))

        # Test that the node was moved to the MRU position.
        node = cache.head.next
        self.assertEqual(cache.hashtable['udacity'], node)
        self.assertEqual(10, node.value)
        self.assertEqual('udacity', node.key)
        node = node.next
        self.assertEqual(cache.hashtable['python'], node)
        self.assertEqual(20, node.value)
        self.assertEqual('python', node.key)

        # Test the wiring in the rest of the linked list.
        node = node.next
        self.assertEqual(cache.hashtable[200], node)
        self.assertEqual('algorithms', node.value)
        self.assertEqual(200, node.key)
        node = node.next
        self.assertEqual(cache.hashtable[100], node)
        self.assertEqual('hello world', node.value)
        self.assertEqual(100, node.key)
        self.assertEqual(cache.hashtable[100], cache.tail.prev)

        # Clean up.
        cache.clear()

if __name__ == '__main__':
    unittest.main()
