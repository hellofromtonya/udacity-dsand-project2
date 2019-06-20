# Explanation for Problem 5: Blockchain

This document provides an explanation for the design decisions and implementation.

## Summary

* Data Structures: LinkedList that uses a hashtable (dictionary) to look up the block for a given hash.
* Efficiencies: O(1) time and O(n) space.


## Data Structures

The design uses two data structures:

| Data Structure | Time Complexity | Space Complexity |
| -------------- | --------------- | ---------------- |
| Hashtable via Python's dictionary | O(1) | O(n) |
| Linked list | O(n) | O(n) |


## Efficiencies

Leveraging the hashtable, this implementation achieves a O(1) for inserting and looking up a block.

| Task | Time Complexity | Space Complexity |
| -------------- | --------------- | ---------------- |
| Inserting a block | O(1) | O(1) |
| Looking up a block | O(1) | O(1) |
| Traversing blocks | O(n) | -- |


## Design Considerations

1. A hashtable is required to lookup or insert blocks in the blockchain.  Why? A block is linked to its previous block via the previous block's hash.  The hashtable lets us lookup the previous block via its hash.
2. A block has a link to its previous block.  Therefore, traversal is from the tail (last block added) to the head (first block added).
3. To simplify the code, this implementation uses dummy head and tail blocks. 
