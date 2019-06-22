#!/usr/bin/env python3

import unittest
from problem_1 import LRU_Cache, CacheNode


class Test_LRU_Cache(unittest.TestCase):
    """
    Test the LRU_Cache methods.
    """

    def test_set_should_return_neg1_when_0_capacity(self):
        """
        LRU_Cache::set() should return -1 and not set the value when the cache's capacity is 0.
        """
        cache = LRU_Cache(0)
        self.assertEqual(-1, cache.set(1, 1))
        self.assertEqual(0, len(cache.hashtable))

    def test_get_should_return_neg1_when_0_capacity(self):
        """
        LRU_Cache::get() should return -1 when the cache's capacity is 0.
        """
        cache = LRU_Cache(0)
        cache.set(1, 1)
        self.assertEqual(-1, cache.get(1))

    def test_set_should_return_neg1_when_falsey_key_given(self):
        """
        LRU_Cache::set() should return -1 when a falsey key is given.
        """
        cache = LRU_Cache(5)
        self.assertEqual(-1, cache.set('', 1))
        self.assertEqual(-1, cache.set(None, 1))
        self.assertEqual(-1, cache.set(False, 1))
        self.assertEqual(-1, cache.set([], 1))
        self.assertEqual(-1, cache.set({}, 1))
        self.assertEqual(0, len(cache.hashtable))

    def test_set_should_cache_the_new_node(self):
        """
        LRU_Cache::set() should cache (add) the new node.
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

    def test_set_should_overwrite_existing_nodes(self):
        """
        LRU_Cache::set() should overwrite existing nodes and move the node to the front (MRU) position
        of the linked list.
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

    def test_get_should_return_neg1_when_falsey_key_given(self):
        """
        LRU_Cache::get() should return -1 when a falsey key is given.
        """
        # Set up.
        cache = LRU_Cache(5)

        self.assertEqual(-1, cache.get(''))
        self.assertEqual(-1, cache.get(False))
        self.assertEqual(-1, cache.get(None))
        self.assertEqual(-1, cache.get([]))
        self.assertEqual(-1, cache.get({}))

    def test_get_shouild_return_neg1_when_not_cached(self):
        """
        LRU_Cache::get() should return -1 when the key is not cached.
        """
        # Set up.
        cache = LRU_Cache(5)

        self.assertEqual(-1, cache.get('does_not_exist'))

    def test_get_should_return_value_and_move_node_to_front(self):
        """
        LRU_Cache::get() should return the value and move the node to the front (MRU) position
        of the linked list.
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

        # Test -1 is returned if the key does not exist.
        self.assertEqual(-1, cache.get('does_not_exist'))

        # Test getting the value and that the node was moved to the front (MRU) position.
        self.assertEqual('hello world', cache.get(100))
        node = cache.head.next
        self.assertEqual(cache.hashtable[100], node)
        self.assertEqual('hello world', node.value)
        self.assertEqual(100, node.key)

        self.assertEqual(2, cache.get('python'))
        node = cache.head.next
        self.assertEqual(cache.hashtable['python'], node)
        self.assertEqual(2, node.value)
        self.assertEqual('python', node.key)

        self.assertEqual(1, cache.get('udacity'))
        node = cache.head.next
        self.assertEqual(cache.hashtable['udacity'], node)
        self.assertEqual(1, node.value)
        self.assertEqual('udacity', node.key)

        self.assertEqual('algorithms', cache.get(200))
        node = cache.head.next
        self.assertEqual(cache.hashtable[200], node)
        self.assertEqual('algorithms', node.value)
        self.assertEqual(200, node.key)

        # Clean up.
        cache.clear()

    def test_set_should_remove_lru_node_when_overcapacity(self):
        """
        LRU_Cache::set() should remove the LRU node when overcapacity.
        """
        # Set up.
        cache = LRU_Cache(4)
        test_data = {
            'udacity': 1,
            'python': 2,
            100: 'hello world',
            200: 'algorithms'
        }
        for key, value in test_data.items():
            cache.set(key, value)

        # Check the before states.
        self.assertEqual(cache.hashtable['udacity'], cache.tail.prev)
        self.assertEqual(len(cache.hashtable), cache.capacity)

        cache.set(300, 'overcapacity')

        # Test that the previous last node has been removed.
        self.assertEqual(len(cache.hashtable), cache.capacity)
        self.assertFalse('udacity' in cache.hashtable)
        self.assertEqual(-1, cache.get('udacity'))
        self.assertEqual(cache.hashtable['python'], cache.tail.prev)

        # Retest each node in the linked list.
        node = cache.head.next
        self.assertEqual(cache.hashtable[300], node)
        self.assertEqual(cache.hashtable[200], node.next)
        self.assertEqual(cache.hashtable[100], node.next.next)
        self.assertEqual(cache.hashtable['python'], node.next.next.next)

        # Clean up.
        cache.clear()


if __name__ == '__main__':
    unittest.main()
