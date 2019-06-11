#!/usr/bin/env python3

import unittest
from problem_3 import huffman_encoding, huffman_decoding, map_frequency, build_priority_queue


class Test_HuffmanCoding(unittest.TestCase):

    def test_map_frequency_should_return_empty_dict_when_falsey_given(self):
        """
        Test map_frequency() should return an empty dictionary when a falsey input is given.
        """
        expected = dict()
        self.assertDictEqual(expected, map_frequency(''))
        self.assertDictEqual(expected, map_frequency(False))
        self.assertDictEqual(expected, map_frequency(None))

    def test_map_frequency_should_map_character_counts(self):
        """
        Test map_frequency() should return a fequency map for the given string input.
        """
        actual = map_frequency('ab ba')
        expected = {
            'a': 2,
            'b': 2,
            ' ': 1,
        }
        self.assertDictEqual(expected, actual)

        actual = map_frequency('Huffman coding')
        expected = {
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
        }
        self.assertDictEqual(expected, actual)

        actual = map_frequency('ABRACADABRA')
        expected = {
            'A': 5,
            'B': 2,
            'R': 2,
            'C': 1,
            'D': 1,
        }
        self.assertDictEqual(expected, actual)

        actual = map_frequency('Mississippi')
        expected = {
            'M': 1,
            'i': 4,
            's': 4,
            'p': 2,
        }
        self.assertDictEqual(expected, actual)

        actual = map_frequency('Sally sells seashells down by the seashore.')
        expected = {
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
        }
        self.assertDictEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
