#!/usr/bin/env python3

from hashlib import sha256
from datetime import datetime


class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        hash_str = str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8')

        return sha256(hash_str).hexdigest()

    def __str__(self):
        return ' {}\t| {}\t| {}\t | {}'.format(self.index, self.data, self.timestamp, self.hash)


class Blockchain:

    def __init__(self):
        self.blocks = dict()
        self.head = Block(-1, None, None, -1)
        self.tail = Block(-1, None, None, self.head.hash)

    def insert(self, data):
        """Register a new block into the blockchain. Returns the block."""
        block = Block(len(self.blocks) + 1, datetime.now(), data, self.tail.previous_hash)

        self.tail.previous_hash = block.hash
        self.blocks[block.hash] = block

        return block

    def get(self, hash):
        """Get the block via its hash."""
        if hash in self.blocks:
            return self.blocks[hash]

    def __iter__(self):
        if len(self.blocks) == 0:
            return

        block = self.blocks[self.tail.previous_hash]
        while block:
            if block.index == -1:
                break
            yield block
            if block.previous_hash not in self.blocks:
                break
            block = self.blocks[block.previous_hash]

    def __repr__(self):
        if len(self.blocks) == 0:
            return 'Blockchain is empty.\n'

        output = ''
        for block in self:
            output += str(block) + "\n"

        return output


if __name__ == '__main__':
    def run_test_1():
        print('Running test 1....')
        blockchain = Blockchain()
        block1 = blockchain.insert('Block 1')
        block2 = blockchain.insert('Block 2')

        print(blockchain.get(block1.hash))              # Should print block1.
        print(blockchain.get(block1.previous_hash))     # Should print None (as it's the dummy head block.
        print(blockchain.get(block2.hash))              # Should print block2.
        print(blockchain.get(block2.previous_hash))     # Should print block1.
        print()

    def run_test_2():
        print('Running test 2....')
        blockchain = Blockchain()
        print(blockchain)       # Should print "Blockchain is empty."
        for n in range(50):
            blockchain.insert('Some information {}'.format(n))

        print(blockchain)       # Should print the entire blockchain.

        # Walk the blockchain.
        for block in blockchain:
            print('{}: {}'.format(block.index, block.hash)) # Should print each block's index and hash.

    run_test_1()
    run_test_2()
