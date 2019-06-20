#!/usr/bin/env python3

import unittest
from datetime import datetime
import problem_5 as p5


class Test_Block(unittest.TestCase):

    def test_calc_hash_should_generate_repeatable_hash(self):
        """
        Test Block:calc_hash() should generate a repeatable hash, i.e. the same hash when the attributes do
        not change.
        """
        block1 = p5.Block(0, datetime.now(), 'Block 1 data', 0)
        orig_hash = block1.calc_hash()
        self.assertEqual(block1.calc_hash(), orig_hash)

    def test_calc_hash_should_generate_unique_hash(self):
        """
        Test Block:calc_hash() should generate a unique hash.
        """
        block1 = p5.Block(1, datetime.now(), 'Block 1 data', 0)
        hash1 = block1.calc_hash()

        block2 = p5.Block(2, datetime.now(), 'Block 2 data', hash1)
        hash2 = block2.calc_hash()
        self.assertNotEqual(hash1, hash2)

        block3 = p5.Block(3, datetime.now(), 'Block 3 data', hash1)
        hash3 = block3.calc_hash()
        self.assertNotEqual(hash1, hash3)
        self.assertNotEqual(hash2, hash3)

    def test_blockchain_insert_should_create_and_insert_block(self):
        """
        Test Blockchain:insert() should create a blockchain.
        """
        blockchain = p5.Blockchain()
        for n in range(1, 11):
            blockchain.insert('Block {} data'.format(n))

        # Walk the blocks in the blockchain.
        index = 10
        for block in blockchain:
            self.assertEqual(index, block.index)
            self.assertEqual('Block {} data'.format(index), block.data)
            index -= 1

    def test_blockchain_get_should_return_requested_block(self):
        """
        Test Blockchain:get() should lookup and return the requested block, i.e. by its hash.
        """
        blockchain = p5.Blockchain()
        block1 = blockchain.insert('Block 1')
        block2 = blockchain.insert('Block 2')
        block3 = blockchain.insert('Block 3')

        self.assertEqual(block1, blockchain.get(block1.hash))
        self.assertIsNone(blockchain.get(block1.previous_hash))
        self.assertEqual(block2, blockchain.get(block2.hash))
        self.assertEqual(block1, blockchain.get(block2.previous_hash))
        self.assertEqual(block3, blockchain.get(block3.hash))
        self.assertEqual(block2, blockchain.get(block3.previous_hash))


if __name__ == '__main__':
    unittest.main()
