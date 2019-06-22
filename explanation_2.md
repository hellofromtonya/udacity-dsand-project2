# Explanation for Problem 2: File Recursion

This document provides an explanation for the design decisions and implementation.

## Summary

1. Efficiency: worst case of O(d + f) time and a O(n) space.
2. Data structure: array, more specifically a Python list.

## Data Structures

This problem uses a list data structure as the container to hold the found files.

## Efficiency

The space efficiency in the worst case is also O(n) where all files in path match.

### Time Efficiency

Let `d` represent the number of directories:

* root directory + all subdirectories
* represents the number of times `_find_files()` is invoked

Let `f` represent the files within each directory:

* represents the total number of files within the given filesystem path

Our time complexity then is a sum of `d` and `f` which is expressed as O(d + f).

Let's visualize it using the given test directory for this problem:

```
_find_files('testdir') f = 2
      |  
      |-  _find_files('subdir1') f = 2
      |     
      |-  _find_files('subdir2') f = 1
      |  
      |-  _find_files('subdir3') f = 0
      |         |  
      |          -  _find_files('subsubdir1') f = 2
      |     
      |-  _find_files('subdir4') f = 1 
      |     
       -  _find_files('subdir5') f = 2        
``` 

The total number of entries for the test directory is 17 which is comprised of:

* d = 7
* f = 10

For the given known test directory, the time complexity is O(7 + 10) = O(17).

For an unknown test directory, we compute the time complexity as O(d + f):

    O(total number of directories + the total number of files)


#### Analyzing the code
   

```python
def find_files(suffix, path):
    if not bool(path):                                  # O(1)
        return []

    if not bool(suffix):                                # O(1)
        suffix = None

    def _find_files(path, files):
        for entry in os.listdir(path):                  # O(e) where e is the number of entries in the path.
            fullpath = os.path.join(path, entry)            # O(1)
            if os.path.isdir(fullpath):                     # O(1)
                files = _find_files(fullpath, files)        # O(e), where e is the number of entries in this new path.   

            elif os.path.isfile(fullpath) and (suffix is None or entry.endswith(suffix)):   # O(1)
                files.append(fullpath)                                                      # O(1)

        return files

    return _find_files(path, [])    # O(d + f)
```

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
