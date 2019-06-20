# Explanation for Problem 6: Union and Intersection of 2 Linked Lists

This document provides an explanation for the design decisions and implementation.

## Summary

* Data Structures:  Linked list for the sets and a hashtable (dictionary) for mapping distinct values in sets.
* Efficiency:
    * A ∪ B `union`:  O(a + b) for time and space complexities, where a is the length of set A and b is the length of set B.
    * A ∩ B `intersection`: O(a) for both time and space complexities, where a is the length of set A.

## Data Structures

This design uses 2 data structures:

* Linked list for the sets
* Hashtable for mapping the distinct values

## Efficiencies

The Linked List tracks both the `head` and `tail` to speed up the time complexity of the `append` functionality.  This implementation changes each `append` from O(len(r)) to O(1).

### Efficiencies of A ∪ B

The time and time complexities are both O(a + b), where a is the length of set A and b is the length of set B.  Why?

In the worst case, all values are distinct in both sets.

1. Both sets are traversed.
2. `map` will grow by the total number of nodes in each set.
3. The union linked list also grows by the total number of nodes in each set.

```python
def union(setA, setB):
    """A ∪ B: Returns a linked list with distinct values that are in set A, set B, or both."""
    map = dict()                            # O(a + b) => O(len(a) + len(b))
    result = LinkedList()

    for node in setA:                       # O(len(a))
        value = str(node.value)
        if value not in map:                    # O(1)
            map[value] = node                   # O(1)
            result.append(node)                 # O(1)

    for node in setB:                       # O(len(b))
        value = str(node.value)
        if value not in map:                    # O(1)
            map[value] = node                   # O(1)
            result.append(node)                 # O(1)

    return result                           # O(a + b) => O(len(a) + len(b))
```

### Efficiencies of A ∩ B

The time and time complexities are both O(a), where a is the length of set A.  Why?

In the worst case, all values are distinct in set A and set B is a subset of A.

1. Both sets are traversed.
2. `map` will grow by the total number of nodes in set A.
3. The intersection linked list also grows by the total number of nodes in set A.

```python
def intersection(setA, setB):
    map = dict()                                    # O(len(a))
    for node in setA:                               # O(len(a))
        map[str(node.value)] = node                     # O(1)

    result = LinkedList()
    for node in setB:                               # O(len(b))
        value = str(node.value)                     
        if value in map:                                # O(1)
            result.append(node)                         # O(1)
            # remove the value from the map to ensure no duplicate values.
            del map[value]

    return result                                   # O(len(a))
```

## Design Considerations

By definition, ["a set is a collection of distinct objects"](https://en.wikipedia.org/wiki/Set_(mathematics)).  The implementation ensures no duplicates are included from either the union or intersection functions.
