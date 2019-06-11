# Explanation for Problem 3: Huffman Coding

This document provides an explanation for the design decisions and implementation.

## Data Structures

* Priority queue with a heap for ordering and building the tree
* Custom node for the Huffman Nodes
* Binary tree for the Huffman Tree
* Dictionary for the frequencies map
* Dictionary for the code mappings

## Efficiencies


## Design Considerations



## Summary


## Scratchpad

The current design is not optimized as it's using slower data structures:

* Priority queue uses an array instead of a heap.
* 

TODO:

1. Build the test suite.
2. Analysis the time and space efficiencies to generate improvement tasks.
3. Replace the priority queue's container with a heap.
4. Replace the sort function and optimize with heapify and a binary heap to get down to O(log n) instead of O(n log n).
    - Look at the implementation of combining a hashtable with the binary heap to reduce further, [ref](https://youtu.be/wptevk0bshY?t=665)
