#!/usr/bin/env python3

import sys


class HuffmanNode:
    def __init__(self, freq, char):
        self.freq = freq
        self.char = char
        self.left_child = None
        self.right_child = None


def map_frequency(data):
    """
    Maps the character frequencies (counts) into a dictionary (hashtable).

    :param data: String to be mapped.
    :return: dictionary with char as key and frequency as the value.
    """
    frequencies = dict()

    if not bool(data):
        return frequencies

    for char in data:                          # O(n)
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    return frequencies


def build_priority_queue(frequencies):
    """
    Builds the priority queue for the given frequencies dictionary.

    :param frequencies: dictionary of character frequencies
    :return: list (array) of a sorted priority queue
    """
    priority_queue = []
    for char, freq in frequencies.items():       # O(n)
        node = HuffmanNode(freq, char)
        priority_queue.append((freq, node))

    _sort_pq(priority_queue)
    return priority_queue


def _sort_pq(priority_queue):
    """Sort is O(n log n)"""
    priority_queue.sort(key=lambda tup: tup[0])


def build_tree(priority_queue):
    # The steps to build the tree are as follows:
    #
    # while pq.size() > 1:
    #   1. Pop the 1st 2 nodes out of the priority queue.
    #   2. Sum the frequencies.
    #   3. Make a new parent node with the sum of the child frequencies.
    #   4. Enqueue it back into the priority queue.
    # when done, the last item in the pq is the root of the tree.
    tree = None

    while len(priority_queue) > 1:
        left_child = priority_queue.pop(0)
        right_child = priority_queue.pop(0)
        parent = HuffmanNode(left_child[1].freq + right_child[1].freq, None)
        parent.left_child = left_child[1]
        parent.right_child = right_child[1]

        priority_queue.append((parent.freq, parent))
        _sort_pq(priority_queue)

    root = priority_queue.pop()
    return root[1]


def map_codes(node, code='', code_mappings={}):
    """
    Map the codes of the Huffman Tree by recursively walking root to leaf.

    :param node: Current HuffmanNode
    :param code: The current code of 1s and 0s.
    :param code_mappings: Dictionary of code mappings
    :return: Dictionary of code mappings where char is the key and the code is the value.
    """

    if type(node.left_child) is HuffmanNode:
        map_codes(node.left_child, code + '0', code_mappings)
    else:
        code_mappings[node.char] = code

    if type(node.right_child) is HuffmanNode:
        map_codes(node.right_child, code + '1', code_mappings)
    else:
        code_mappings[node.char] = code

    return code_mappings


def huffman_encoding(data):
    """
    Encodes the given string data using the Huffman Coding algorithm.

    :param data: String to be encoded.
    :return: tuple - encoded data, Huffman Tree
    """

    # Step 1: Map the frequencies.
    frequencies = map_frequency(data)

    # Step 2: build and sort the priority queue.
    priority_queue = build_priority_queue(frequencies)

    # Step 3: Build the Huffman Tree.
    tree = build_tree(priority_queue)

    # Step 4: Map the codes from the Huffman Tree.
    code_mappings = map_codes(tree)

    # Step 5: Encode the original data using the code mappings from the Huffman Tree.
    encoding = ''
    for char in data:
        encoding += code_mappings[char]

    return encoding, tree


def huffman_decoding(data, tree):
    """
    Decode the given encoded (compressed) data using the given Huffman Tree.

    :param data: the encoded data to be decoded.
    :param tree: the Huffman Tree used to encode the original, uncompressed data
    :return: string - the decoded data string
    """
    decoded = ''
    node = tree

    for bit in data:

        # Walk to the left child.
        if int(bit) == 0:
            if type(node.left_child) is HuffmanNode:
                node = node.left_child

        # Walk to the right child.
        else:
            if type(node.right_child) is HuffmanNode:
                node = node.right_child

        # If leaf, capture the char and rewind to the root.
        if node.left_child is None and node.right_child is None:
            decoded += node.char
            node = tree

    return decoded


if __name__ == '__main__':

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
