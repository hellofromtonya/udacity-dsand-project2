#!/usr/bin/env python3


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.values = dict()

    def append(self, value):
        # Bail out if the value is already in the set.
        if not self._is_distinct(value):
            return

        new_node = Node(value)
        self.values[str(value)] = new_node

        if self.head is None:
            self.head = new_node
        elif self.tail is None:
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node

    def _is_distinct(self, value):
        return str(value) not in self.values

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        node = self.head
        output = ''
        while node:
            output += str(node.value) + ' -> '
            node = node.next

        return output


def union(setA, setB):
    """A ∪ B: Returns a linked list with distinct values that are in set A, set B, or both."""
    map = dict()
    result = LinkedList()

    for node in setA:
        map[str(node.value)] = node
        result.append(node)

    for node in setB:
        value = str(node.value)
        if value not in map:
            map[value] = node
            result.append(node)

    return result


def intersection(setA, setB):
    """A ∩ B: Returns a linked list with distinct values that are in both set A and B."""
    # Convert setA into a map.
    map = dict()
    for node in setA:
        map[str(node.value)] = node

    # Walk through setB.  Append each value that is in both setA and setB.
    result = LinkedList()
    for node in setB:
        value = str(node.value)
        if value in map:
            result.append(node)
            # remove the value from the map to ensure no duplicate values.
            del map[value]

    return result


if __name__ == '__main__':

    def run_test_case_1():
        print('Test case 1...')
        setA = LinkedList()
        setB = LinkedList()

        result = union(setA, setB)
        print('None found' if result.size() == 0 else result)    # None found
        result = intersection(setA, setB)
        print('None found' if result.size() == 0 else result)    # None found

        setB.append(5)
        result = union(setA, setB)
        print('None found' if result.size() == 0 else result)    # 5 ->
        result = intersection(setA, setB)
        print('None found' if result.size() == 0 else result)    # None found

        setA.append(8)
        result = union(setA, setB)
        print('None found' if result.size() == 0 else result)    # 8 -> 5 ->
        result = intersection(setA, setB)
        print('None found' if result.size() == 0 else result)    # None found

        setA.append(5)
        result = union(setA, setB)
        print('None found' if result.size() == 0 else result)    # 8 -> 5 ->
        result = intersection(setA, setB)
        print('None found' if result.size() == 0 else result)    # 5 ->

    def run_test_case_2():
        print('\nTest case 2...')
        setA = LinkedList()
        setB = LinkedList()

        for value in [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]:
            setA.append(value)

        for value in [6, 32, 4, 9, 6, 1, 11, 21, 1]:
            setB.append(value)

        print(union(setA, setB))            # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
        print(intersection(setA, setB))     # 4 -> 6 -> 21 ->

    def run_test_case_3():
        print('\nTest case 3...')
        setA = LinkedList()
        setB = LinkedList()

        for value in [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]:
            setA.append(value)

        for value in [1, 7, 8, 9, 11, 21, 1]:
            setB.append(value)

        print(union(setA, setB))            # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
        result = intersection(setA, setB)
        print('None found' if result.size() == 0 else result)    # None found

    run_test_case_1()
    run_test_case_2()
    run_test_case_3()
