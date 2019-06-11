#!/usr/bin/env python3

import sys


class HuffmanNode:
    def __init__(self, freq, char):
        self.freq = freq
        self.char = char
        self.left_child = None
        self.right_child = None


class HuffmanCoding:
    def __init__(self, data, tree=None):
        self.frequency = dict()
        self.pq = []            # Priority queue: Change to a head implementation or use the built-in one.
        self.tree = tree
        self.data = data

    def encode(self):
        # Step 1: Map the frequencies
        self.map_frequency()

        # Step 2: build and sort the priority queue
        self.build_priority_queue()

        # Step 3: Build the tree
        self.build_tree()

        # Step 4: Encode the original data using the tree.
        return self.generate_encode()

    def decode(self, code):
        """Decode the given code."""
        decoded = ''
        node = self.tree
        for bit in code:
            # Go left
            if int(bit) == 0:
                if type(node.left_child) is HuffmanNode:
                    node = node.left_child

            # Go right
            else:
                if type(node.right_child) is HuffmanNode:
                    node = node.right_child

            # If leaf, capture the char and rewind to the root.
            if node.left_child is None and node.right_child is None:
                decoded += node.char
                node = self.tree

        return decoded

    def map_frequency(self):
        for char in self.data:                          # O(n)
            if char in self.frequency:
                self.frequency[char] += 1
            else:
                self.frequency[char] = 1

    def build_priority_queue(self):
        for char, freq in self.frequency.items():       # O(n)
            node = HuffmanNode(freq, char)
            self.pq.append((freq, node))
        self._sort_pq()                                 # O(n log n) Ouch

    def _enqueue(self, freq, node):
        self.pq.append((freq, node))
        self._sort_pq()                                 # O(n log n) Ouch

    def build_tree(self):
        # The steps to build the tree are as follows:
        #
        # while pq.size() > 1:
        #   1. Pop the 1st 2 nodes out of the priority queue.
        #   2. Sum the frequencies.
        #   3. Make a new parent node with the sum of the child frequencies.
        #   4. Enqueue it back into the priority queue.
        # when done, the last item in the pq is the root of the tree.

        while len(self.pq) > 1:
            left_child = self.pq.pop(0)
            right_child = self.pq.pop(0)
            parent = HuffmanNode(left_child[1].freq + right_child[1].freq, None)
            parent.left_child = left_child[1]
            parent.right_child = right_child[1]
            self._enqueue(parent.freq, parent)

        root = self.pq.pop()
        self.tree = root[1]

    def generate_encode(self):
        """Encode the original string data."""
        code_mappings = self._map_codes(self.tree)
        code = ''
        for char in self.data:
            code += code_mappings[char]

        return code

    def _map_codes(self, node, code='', code_mappings={}):
        """Recursively walk all the nodes, building the codes map."""
        if type(node.left_child) is HuffmanNode:
            self._map_codes(node.left_child, code + '0', code_mappings)
        else:
            code_mappings[node.char] = code

        if type(node.right_child) is HuffmanNode:
            self._map_codes(node.right_child, code + '1', code_mappings)
        else:
            code_mappings[node.char] = code

        return code_mappings

    def _sort_pq(self):
        """Sort is O(n log n)"""
        self.pq.sort(key=lambda tup: tup[0])


if __name__ == '__main__':

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    hc = HuffmanCoding(a_great_sentence)
    encoded_data = hc.encode()

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = hc.decode(encoded_data)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
