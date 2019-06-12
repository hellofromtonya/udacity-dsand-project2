#!/usr/bin/env python3

import unittest
from problem_3 import HuffmanNode, huffman_encoding, huffman_decoding, map_frequency, build_tree, map_codes


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
            for index, map in enumerate(actual):
                actual_freq, actual_char, actual_node = map
                expected_freq, expected_char = test_data['frequencies'][index]

                self.assertEqual(expected_freq, actual_freq)
                self.assertEqual(expected_char, actual_char)
                self.assertEqual(expected_freq, actual_node.freq)
                self.assertEqual(expected_char, actual_node.char)

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
            freq = map_frequency(data)
            tree = build_tree(freq)

            actual = self._get_tree_order(tree)
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
            tree = build_tree(freq)

            self.assertDictEqual(test_data['map'], map_codes(tree, '', {}))

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

    def test_huffman_decoding_should_decode(self):
        """
        Test huffman_decoding() should decode the given encoded string.
        """
        for data, test_data in self.test_data.items():
            encoding, tree = huffman_encoding(data)
            self.assertEqual(data, huffman_decoding(encoding, tree))

    def test_huffman_decoding_should_throw_error_when_tree_is_invalid(self):
        """
        Test huffman_decoding() should throw an error when no tree is given.
        """
        with self.assertRaises(AttributeError) as context:
            huffman_decoding('11010011', None)
        self.assertTrue("'NoneType' object has no attribute 'right_child'" in str(context.exception))

    """
    Helpers.
    """

    def _get_tree_order(self, tree):
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
            # Edge case of only 1 character.
            'n': {
                'frequencies': [(0, None, ), (1, 'n', )],
                'tree_order': [
                    (1, None),
                    (0, None),
                    (1, 'n')
                ],
                #      1
                #  0      1
                #        'n'
                'map': {None: '0', 'n': '1'},
                'encoding': '1',
            },
            'ab ba': {
                'frequencies': [
                    (2, 'a', ),
                    (2, 'b', ),
                    (1, ' ', )
                ],
                'tree_order': [
                    (5, None),
                    (2, 'b'),
                    (3, None), (1, ' '), (2, 'a')
                ],
                #      5
                #  2       3
                # 'b'    1   2
                #       ' ' 'a'
                'map': {'b': '0', ' ': '10', 'a': '11'},
                'encoding': '11010011',
            },
            'Huffman coding': {
                'frequencies': [
                    (1, 'H', ),
                    (1, 'u', ),
                    (2, 'f', ),
                    (1, 'm', ),
                    (1, 'a', ),
                    (2, 'n', ),
                    (1, ' ', ),
                    (1, 'c', ),
                    (1, 'o', ),
                    (1, 'd', ),
                    (1, 'i', ),
                    (1, 'g', )
                ],
                'tree_order': [
                    (14, None),
                    (6, None), (2, 'n'), (4, None), (2, None), (1, ' '), (1, 'H'), (2, None), (1, 'a'), (1, 'c'),
                    (8, None), (4, None), (2, None), (1, 'd'), (1, 'g'), (2, None), (1, 'i'), (1, 'm'), (4, None), (2, None), (1, 'o'), (1, 'u'), (2, 'f')
                ],
                #                     14
                #            .                .
                #        6                           8
                #      .   .                     .        .
                #    2        4               4                4
                #   'n'     .    .          .   .            .   .
                #          2       2       2      2        2       2
                #         . .     . .     . .     . .     . .     'f'
                #        1   1   1   1   1   1   1   1   1   1
                #       ' ' 'H' 'a' 'c' 'd' 'g' 'i' 'm' 'o' 'u'
                'map': {'n': '00', ' ': '0100', 'H': '0101', 'a': '0110', 'c': '0111', 'd': '1000', 'g': '1001', 'i': '1010', 'm': '1011', 'o': '1100', 'u': '1101', 'f': '111'},
                'encoding': '01011101111111101101100001000111110010001010001001',
            },
            'ABRACADABRA': {
                'frequencies':  [
                    (5, 'A', ),
                    (2, 'B', ),
                    (2, 'R', ),
                    (1, 'C', ),
                    (1, 'D', )
                ],
                'tree_order': [
                    (11, None),
                    (5, 'A'),
                    (6, None), (2, 'R'), (4, None), (2, None), (1, 'C'), (1, 'D'), (2, 'B')
                ],
                #           11
                #      .          .
                #  5                   6
                # 'A'               .       .
                #              2               4
                #             'R'             .    .
                #                          2         2
                #                         . .       'B'
                #                        1   1
                #                       'C' 'D'
                'map': {'A': '0', 'R': '10', 'C': '1100', 'D': '1101', 'B': '111'},
                'encoding': '01111001100011010111100',
            },
            'Mississippi': {
                'frequencies': [
                    (1, 'M', ),
                    (4, 'i', ),
                    (4, 's', ),
                    (2, 'p', )
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
                'frequencies': [
                    (1, 'S', ),
                    (3, 'a', ),
                    (6, 'l', ),
                    (2, 'y', ),
                    (6, ' ', ),
                    (7, 's', ),
                    (6, 'e', ),
                    (3, 'h', ),
                    (1, 'd', ),
                    (2, 'o', ),
                    (1, 'w', ),
                    (1, 'n', ),
                    (1, 'b', ),
                    (1, 't', ),
                    (1, 'r', ),
                    (1, '.', )
                ],
                'tree_order': [
                    (43, None),
                    (18, None), (8, None), (4, None), (2, None), (1, '.'), (1, 'S'), (2, None), (1, 'b'), (1, 'd'), (4, None), (2, None), (1, 'n'), (1, 'r'), (2, None), (1, 't'), (1, 'w'), (10, None), (4, None), (2, 'o'), (2, 'y'), (6, ' '),
                    (25, None), (12, None), (6, None), (3, 'a'), (3, 'h'), (6, 'e'), (13, None), (6, 'l'), (7, 's')
                ],
                'map': {'.': '00000', 'S': '00001', 'b': '00010', 'd': '00011', 'n': '00100', 'r': '00101', 't': '00110', 'w': '00111', 'o': '0100', 'y': '0101', ' ': '011', 'a': '1000', 'h': '1001', 'e': '101', 'l': '110', 's': '111'},
                'encoding': '00001100011011001010111111011101101110111111011000111100110111011011101100011010000111001000110001001010110011010011010111111011000111100101000010110100000',
            },
        }


if __name__ == '__main__':
    unittest.main()
