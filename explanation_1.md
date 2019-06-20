# Explanation for Problem 1: LRU Cache

This document provides an explanation for the design decisions and implementation.

## Summary

1. Efficiency: worst case of O(1) time and a O(n) space.
2. Data structures: hashtable (via dictionary) and doubly linked list

## Data Structures

The design uses two data structures:

| Data Structure | Time Complexity | Space Complexity |
| -------------- | --------------- | ---------------- |
| Hashtable via Python's dictionary | O(1) | O(n) |
| Doubly linked list | O(n) | O(n) |

## Design Considerations

### Why a doubly linked list?

The doubly linked list is used to track the order of the nodes, where the head is the most recently used (MRU) position and the tail is the least recently used (LRU) position. 

1. Sequentially organizes the nodes, as each node is pointing to its previous and next node in the chain.
2. Nodes can easily be removed, moved, and added. 
3. We gain O(1) time complexity when moving or removing a node because each node points to its previous node.  With a single linked list, we would have to traverse back around the entire chain to find the previous node, i.e. O(n) time complexity.

### Why a dictionary?

Python's dictionary handles key/value pairs and provides a O(1) lookup. It simplifies the LRU Cache's code as we do not need to build a hashing function or collision handler.  Rather, the dictionary takes care of these features for us.

### Data Structures Working Together

For all the advantages of the doubly linked list, moving a node from the middle to the front (MRU) position would be O(n) in the worst case, as we'd have to traverse the linked list to find the node to be moved.

A lookup in a hashtable/dictionary is O(1) time.  In the design, the hashtable stores the key and its node.  When we need to get or move the node, we look up the key in the hashtable to gain direct access to its node in the linked list.  No traversal is required.

```
Hashtable       Doubly Linked List
 ----                ------
| 1  |  ------      | head |
 ----         |      ------
              |       | |   most recently used (MRU)
 ----         |      ------  
| 2  | ------------>|  2   |
 ----         |      ------
         --------     | |   
 ----   |     |  |   ------  
| 3  | ----   |  -->|  4   |
 ----   |  |  |      ------
        |   ----      | |  
 ----   |     | |    ------  
| 4  | --     |  -->|  3   |
 ----         |      ------
              |       | |  
 ----         |      ------  
| 5  | --      ---->|  1   |
 ----    |           ------
         |            | |  least recently used (LRU)
         |           ------  
          --------->|  5   |
                     ------
                      | |
                     ------
                    | tail |
                     ------
```
                     
### Dummy Head and Tail Nodes

To reduce code complexity, a dummy head and tail node is used.  How is the complexity reduced? It eliminates checking if there's a head or tail and then setting or resetting either as needed.  This technique is a common approach.

### Guard Clause for Falsey Key

If a falsey value is given for the key, the `set()` or `get()` method bails out, returning `-1`.  This design pattern is handled via a guard clause which checks for any falsey value being passed as the `key`.

To make the code more readable and understandable, checks for falsey are done by typecasting to boolean first.  I find the intent is better understood as "checking for falsey" conditions.

## Reset via `clear` Method

A `clear` method is provided to aid in testing.
