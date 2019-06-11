#!/usr/bin/env python3

import unittest
from problem_3 import HuffmanNode, huffman_encoding, huffman_decoding, map_frequency, _build_priority_queue, build_tree, map_codes


class Test_HuffmanCoding(unittest.TestCase):

    def test_map_frequency_should_return_empty_dict_when_falsey_given(self):
        """
        Test _map_frequency() should return an empty dictionary when a falsey input is given.
        """
        expected = dict()
        self.assertDictEqual(expected, map_frequency(''))
        self.assertDictEqual(expected, map_frequency(False))
        self.assertDictEqual(expected, map_frequency(None))

    def test_map_frequency_should_map_character_counts(self):
        """
        Test _map_frequency() should return a frequency map for the given string input.
        """
        for data, test_data in self.test_data.items():
            actual = map_frequency(data)
            self.assertDictEqual(test_data['frequencies'], actual)

    def test_build_priority_should_return_empty_array_when_input_empty(self):
        """
        Test _map_frequency() should return an empty array when input is empty.
        """
        self.assertListEqual([], _build_priority_queue(dict()))

    def test_build_priority_should_throw_error_when_invalid_input(self):
        """
        Test _build_priority_queue() should throw an exception when an invalid input is given.
        """
        with self.assertRaises(AttributeError) as context:
            _build_priority_queue([])
        self.assertTrue("'list' object has no attribute 'items'" in str(context.exception))

    def test_build_priority_should_return_sorted_array(self):
        """
        Test _build_priority_queue() should return a sorted array for the given frequencies dictionary.
        """
        for data, test_data in self.test_data.items():
            actual = _build_priority_queue(test_data['frequencies'])
            expected = test_data['priority_queue']
            for i in range(len(actual)):
                self.assertEqual(expected[i]['freq'], actual[i][0])
                node = actual[i][1]
                self.assertEqual(expected[i]['freq'], node.freq)
                self.assertEqual(expected[i]['char'], node.char)

    def test_build_tree_should_return_none_when_empty_priority_queue_given(self):
        """
        Test build_tree() should return None when an empty priority queue is given.
        """
        self.assertIsNone(build_tree([]))

    def test_build_tree_should_build_huffman_tree(self):
        """
        Test build_tree() should build a Huffman Tree from the given priority queue.
        """
        for data, test_data in self.test_data.items():
            pq = _build_priority_queue(test_data['frequencies'])
            tree = build_tree(pq)

            actual = self._traverse_in_level_order(tree)
            expected = test_data['tree_order']
            for i, node in enumerate(actual):
                self.assertEqual(expected[i][0], actual[i][0])
                self.assertEqual(expected[i][1], actual[i][1])

    def test_map_codes_should_map_given_tree(self):
        """
        Test map_codes() should map the given tree.
        """
        for data, test_data in self.test_data.items():
            freq = map_frequency(data)
            pq = _build_priority_queue(freq)
            tree = build_tree(pq)

            self.assertEqual(test_data['map'], map_codes(tree, '', {}))

    def test_huffman_encoding_should_return_empties_when_no_data_given(self):
        """
        Test huffman_encoding() should return empty tuple when no data is given.
        """
        expected = ('', None)
        self.assertTupleEqual(expected, huffman_encoding(''))
        self.assertTupleEqual(expected, huffman_encoding(None))
        self.assertTupleEqual(expected, huffman_encoding(False))
        self.assertTupleEqual(expected, huffman_encoding({}))

    def test_huffman_encoding_should_encode_given_data(self):
        """
        Test huffman_encoding() should encode the given data.
        """
        for data, test_data in self.test_data.items():
            encoding, tree = huffman_encoding(data)
            self.assertEqual(test_data['encoding'], encoding)


    def _traverse_in_level_order(self, tree):
        """Helper function to fetch the tree's order."""
        order = []

        def _traverse(node):
            if node is not None:
                order.append((node.freq, node.char))

            if node.left_child:
                _traverse(node.left_child)

            if node.right_child:
                _traverse(node.right_child)

        _traverse(tree)
        return order

    @classmethod
    def setUpClass(cls):
        cls.test_data = {
            'ab ba': {
                'frequencies': {
                    'a': 2,
                    'b': 2,
                    ' ': 1,
                },
                'priority_queue': [
                    {'freq': 1, 'char': ' '},
                    {'freq': 2, 'char': 'a'},
                    {'freq': 2, 'char': 'b'},
                ],
                'tree_order': [
                    (5, None),
                    (2, 'b'),
                    (3, None), (1, ' '), (2, 'a')
                ],
                #      5
                #  2       3
                # 'a'    1   2
                #       ' ' 'a'
                'map': {'b': '0', ' ': '10', 'a': '11'},
                'encoding': '11010011',
            },
            'Huffman coding': {
                'frequencies': {
                    'H': 1,
                    'u': 1,
                    'f': 2,
                    'm': 1,
                    'a': 1,
                    'n': 2,
                    ' ': 1,
                    'c': 1,
                    'o': 1,
                    'd': 1,
                    'i': 1,
                    'g': 1,
                },
                'priority_queue': [
                    {'freq': 1, 'char': 'H'},
                    {'freq': 1, 'char': 'u'},
                    {'freq': 1, 'char': 'm'},
                    {'freq': 1, 'char': 'a'},
                    {'freq': 1, 'char': ' '},
                    {'freq': 1, 'char': 'c'},
                    {'freq': 1, 'char': 'o'},
                    {'freq': 1, 'char': 'd'},
                    {'freq': 1, 'char': 'i'},
                    {'freq': 1, 'char': 'g'},
                    {'freq': 2, 'char': 'f'},
                    {'freq': 2, 'char': 'n'},
                ],
                'tree_order': [
                    (14, None),
                    (6, None), (2, None), (1, 'i'), (1, 'g'), (4, None), (2, 'f'), (2, 'n'),
                    (8, None), (4, None), (2, None), (1, 'H'), (1, 'u'), (2, None), (1, 'm'), (1, 'a'), (4, None), (2, None), (1, ' '), (1, 'c'), (2, None), (1, 'o'), (1, 'd')
                ],
                #                  14
                #            .            .
                #        6                         8
                #      .   .                   .        .
                #    2       2             4               4
                #   . .     . .          .   .           .   .
                #  1   1   1   1       2      2       2       2
                # 'i' 'g' 'f' 'n'    . .     . .     . .     . .
                #                   1   1   1   1   1   1   1   1
                #                  'H' 'u' 'm' 'a' ' ' 'c' 'o' 'd'
                'map': {'i': '000', 'g': '001', 'f': '010', 'n': '011', 'H': '1000', 'u': '1001', 'm': '1010', 'a': '1011', ' ': '1100', 'c': '1101', 'o': '1110', 'd': '1111'},
                'encoding': '10001001010010101010110111100110111101111000011001',
            },
            'ABRACADABRA': {
                'frequencies': {
                    'A': 5,
                    'B': 2,
                    'R': 2,
                    'C': 1,
                    'D': 1,
                },
                'priority_queue': [
                    {'freq': 1, 'char': 'C'},
                    {'freq': 1, 'char': 'D'},
                    {'freq': 2, 'char': 'B'},
                    {'freq': 2, 'char': 'R'},
                    {'freq': 5, 'char': 'A'},
                ],
                'tree_order': [
                    (11, None),
                    (5, 'A'),
                    (6, None), (2, None), (1, 'C'), (1, 'D'), (4, None), (2, 'B'), (2, 'R')
                ],
                #           11
                #      .          .
                #  5                   6
                # 'A'               .       .
                #              2               4
                #           .     .          .    .
                #         1         1      1         1
                #        'C'       'D'    'B'       'R'
                'map': {'A': '0', 'C': '100', 'D': '101', 'B': '110', 'R': '111'},
                'encoding': '01101110100010101101110',
            },
            'Mississippi': {
                'frequencies': {
                    'M': 1,
                    'i': 4,
                    's': 4,
                    'p': 2,
                },
                'priority_queue': [
                    {'freq': 1, 'char': 'M'},
                    {'freq': 2, 'char': 'p'},
                    {'freq': 4, 'char': 'i'},
                    {'freq': 4, 'char': 's'},
                ],
                'tree_order': [
                    (11, None),
                    (4, 's'),
                    (7, None), (3, None), (1, 'M'), (2, 'p'), (4, 'i')
                ],
                #         11
                #     .        .
                #  4               7
                # 's'          .      .
                #            3           4
                #           . .         'i'
                #          1   2
                #         'M' 'p'
                'map': {'s': '0', 'M': '100', 'p': '101', 'i': '11'},
                'encoding': '100110011001110110111',
            },
            'Sally sells seashells down by the seashore.': {
                'frequencies': {
                    'S': 1,
                    'a': 3,
                    'l': 6,
                    'y': 2,
                    ' ': 6,
                    's': 7,
                    'e': 6,
                    'h': 3,
                    'd': 1,
                    'o': 2,
                    'w': 1,
                    'n': 1,
                    'b': 1,
                    't': 1,
                    'r': 1,
                    '.': 1,
                },
                'priority_queue': [
                    {'freq': 1, 'char': 'S'},
                    {'freq': 1, 'char': 'd'},
                    {'freq': 1, 'char': 'w'},
                    {'freq': 1, 'char': 'n'},
                    {'freq': 1, 'char': 'b'},
                    {'freq': 1, 'char': 't'},
                    {'freq': 1, 'char': 'r'},
                    {'freq': 1, 'char': '.'},
                    {'freq': 2, 'char': 'y'},
                    {'freq': 2, 'char': 'o'},
                    {'freq': 3, 'char': 'a'},
                    {'freq': 3, 'char': 'h'},
                    {'freq': 6, 'char': 'l'},
                    {'freq': 6, 'char': ' '},
                    {'freq': 6, 'char': 'e'},
                    {'freq': 7, 'char': 's'},
                ],
                'tree_order': [
                    (43, None),
                    (18, None), (8, None), (4, None), (2, 'y'), (2, 'o'), (4, None), (2, None), (1, 'S'), (1, 'd'), (2, None), (1, 'w'), (1, 'n'), (10, None), (4, None), (2, None), (1, 'b'), (1, 't'), (2, None), (1, 'r'), (1, '.'), (6, 'l'),
                    (25, None), (12, None), (6, ' '), (6, 'e'), (13, None), (6, None), (3, 'a'), (3, 'h'), (7, 's')
                ],
                #                                          43
                #                               .                     .
                #                       18                                   25
                #          8                         10                12        13
                #    4           4              4             6       6   6     6      7
                #  2   2     2       2      2       2        'l'     ' ' 'e'  3   3   's'
                # 'y' 'o'  1   1   1   1   1   1   1   1                     'a' 'h'
                #         'S' 'd' 'w' 'n' 'b' 't' 'r' '.'
                'map': {'y': '0000', 'o': '0001', 'S': '00100', 'd': '00101', 'w': '00110', 'n': '00111', 'b': '01000', 't': '01001', 'r': '01010', '.': '01011', 'l': '011', ' ': '100', 'e': '101', 'a': '1100', 'h': '1101', 's': '111'},
                'encoding': '00100110001101100001001111010110111111001111011100111110110101101111110000101000100110001111000100000001000100111011011001111011100111110100010101010101011',
            },
        }


if __name__ == '__main__':
    unittest.main()
