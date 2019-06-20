# Explanation for Problem 2: File Recursion

This document provides an explanation for the design decisions and implementation.

## Summary

1. Efficiency: worst case of O(n) time and a O(n) space.
2. Data structure: array, more specifically a Python list.

## Data Structures

This problem uses a list data structure as the container to hold the found files.

## Efficiency

The time efficiency for this function is O(n), where `n` is dependent upon the number of subdirectories and files.

The space efficiency in the worst case is also O(n) where all files in path match. 

## Design Considerations

### Why a list and not a dictionary or set?

We need a container to hold the found files.  A container could be a list, dictionary, or set.  I chose to use a list as the container because:

1. There are no lookups in the function.
2. The function requires a list to be returned. Using a dictionary or set would require O(n) conversion to append each item into the final list.
3. The code is adding items into the container, which is O(1) time for all 3 data structures. 

## Design Considerations

### Falsey Checks

To make the code more readable and understandable, checks for falsey are done by typecasting to boolean first.  I find the intent is better understood as "checking for falsey" conditions.

### No Path Given

If no path is given, the function bails out, returning an empty list.  This design pattern is handled via a guard clause which checks for any falsey value being passed as the `path`.

```python
if not bool(path):
    return []
```

### No Suffix Given

If no suffix is given, the function finds and returns all files.  Though not a requirement per the rubic, `find_files()` should process a request to find all files.  It is a valid edge case.

If a falsey is given as the suffix, the code initializes the `suffix` to `None`.  

```python
if not bool(suffix):
    suffix = None
```

Why? 

Lets look at the suffix checker:

```python
def _matches_suffix(file):
    """Checks if the given file ends with the expected suffix."""
    return suffix is None or file.endswith(suffix)
```

Notice that the first check is for `None`.  If the suffix is `None`, then a `True` is returned, meaning call suffixes are a match.  Using `None` streamlines this conditional check as it doesn't have to do another falsey check.  

Why does it streamline?  Recall that the falsey check first converts to `bool` and then checks whether `True` or `False`.  By setting a falsey to `None`, the code does not have to do the `bool` typecast over and over again.  


### Nested Functions Design

Notice that `_find_files()` is nested within the `find_files()`.  Why?  In this design, `_find_files()` is tightly coupled to `find_files()` as it is the recursive worker.  It is intended only for its parent function and not to be reused as a helper for potentially other functions within a package.

With this design, the nested function has access to the given `suffix` without having to specifically pass it with each recursive call.
