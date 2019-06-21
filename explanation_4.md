# Explanation for Problem 4: Active Directory

This document provides an explanation for the design decisions and implementation.

## Summary

Variable conventions:
* Let "g" represent the number of groups.
* Let "u" represent the number of users.

* Data Structure: an array (list) for the groups and hashtable (dictionary) for the users.
* Worst Case Efficiencies for `_is_user_in_group()`: Time is O(g) and space is O(1).
* Groups space complexity is O(g + u).

## Data Structures

I changed the `users` attribute in the given `Group` class structure from an array (list) to a hashtable (dictionary).  Why?

With an array, the implementation would need to iterate through each user for each group.  The original design would incur a time complexity of O(u x g), where `u` represents the number users and `g` represents the number of groups.

By switching the users to a hashtable, we get the following:

* lookups are now O(1)
* user name or ID is the key
* the value is `None` (not used or needed)  

## Efficiency

* Time complexity is O(g)
* Space complexity is O(g + u)

In the worst case, a user does not exist but `is_user_in_group()` has to traverse all the entire group hierarchy.  By using a hashtable for the users, we get O(1) look for each group in the hierarchy.  The time efficiency is not impacted by the number of users, but rather solely by the number of groups.

```python
def is_user_in_group(user, group):
    def _is_user_in_group(user, group, result=None):
        if result is not None:                  # O(1)
            return result

        if user in group.get_users():           # O(1)
            return True

        for subgroup in group.get_groups():     # O(g) where g is the number of subgroups in the hierarchy.
            result = _is_user_in_group(user, subgroup)
            if result:
                return result

        return False

    return _is_user_in_group(user, group)       # O(g)
```

Let's walk through the recursive call stack to visualize the time efficiency.  Let's consider a hierarchy that looks like this:

```
                Group 0
                   |
           --------------------
          |        |           |
        user1   Group 1     Group 2
                   |           |
                 user2     --------
                          |        |
                        user3   Group 3
                                   |
                               --------
                              |        |
                            user4   Group 4
                                       |
                                   ---------
                                  |         |
                                user5     user6

```

The worst case is searching for a user that does not exist or one that's in Group 4.  In either edge case, `_is_user_in_group` will traverse all of the groups:

```
`is_user_in_group('user5', group0) -returns True-->
    \                         |
     \                         ----------------------|  
    _is_user_in_group('user5', group1) -returns True--
        \                         |
         \                         ----------------------|  
         _is_user_in_group('user5', group2) -returns True-- 
             \                         |
              \                         ----------------------|                                           
             _is_user_in_group('user5', group3) -returns True--
                 \                         |
                  \                         ----------------------|
                 _is_user_in_group('user5', group4) -returns True--
```

## Design Considerations

* Specifically chose `None` as the value in the users dictionary, as it only uses 16 bytes, whereas `True` or `1` use 28 bytes each.
* Considered using a LRU cache for faster user lookups.  However, doing so would increase space complexity.
