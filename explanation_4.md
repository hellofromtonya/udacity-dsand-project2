# Explanation for Problem 4: Active Directory

This document provides an explanation for the design decisions and implementation.

## Summary

* Data Structure is a dictionary for a map of users
* Efficiencies: O(1)

## Data Structures

* Hashtable (via dictionary): user's map, where the user's name or ID is the key and the value is the user's object.

## Efficiency

* Time complexity is O(1)
* Space complexity is O(n)

The user's map provides a time complexity of O(1) where we can query a user and check if that user belongs to the specific group.

The user's map increases the space complexity as the user's ID or username is recorded as the key in the map with a link to the user's object in memory.

Therefore, space complexity will be:

* g where g is the number of groups
* u where us is the number of users

O(g+u) = O(n) 

## Design Considerations

This implementation uses a mapping for all the users, where each user holds a reference to the groups that she or he is a member of. This approach provides a relationship between a user and his/her groups.
