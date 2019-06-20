#!/usr/bin/env python3

import unittest
import problem_6 as p6


class Test_UnionAndIntersection(unittest.TestCase):

    def test_union_should_return_empty_ll_when_both_sets_are_empty(self):
        """
        Test union() should return an empty linked list when both sets are empty.
        """
        setA = p6.LinkedList()
        setB = p6.LinkedList()

        result = p6.union(setA, setB)
        self.assertEqual(0, result.size())

    def test_union_should_return_ll_with_union_of_a_and_b(self):
        """
        Test union() should return a linked list with the union of sets A and B.
        """
        setA = p6.LinkedList()
        setB = p6.LinkedList()

        setB.append(5)
        result = p6.union(setA, setB)
        self.assertEqual(1, result.size())
        self.assertEqual('5 -> ', str(result))

        setA.append(8)
        result = p6.union(setA, setB)
        self.assertEqual(2, result.size())
        self.assertEqual('8 -> 5 -> ', str(result))

        setA.append(52)
        result = p6.union(setA, setB)
        self.assertEqual(3, result.size())
        self.assertEqual('8 -> 52 -> 5 -> ', str(result))

        setB.append(14)
        result = p6.union(setA, setB)
        self.assertEqual(4, result.size())
        self.assertEqual('8 -> 52 -> 5 -> 14 -> ', str(result))

    def test_intersection_should_return_empty_ll_when_both_sets_are_empty(self):
        """
        Test intersection() should return an empty linked list when both sets are empty.
        """
        setA = p6.LinkedList()
        setB = p6.LinkedList()

        result = p6.intersection(setA, setB)
        self.assertEqual(0, result.size())

    def test_intersection_should_return_empty_ll_when_not_in_both_a_and_b(self):
        """
        Test intersection() should return an empty linked list when no values are in both sets.
        """
        setA = p6.LinkedList()
        setB = p6.LinkedList()

        for n in range(5):
            setA.append(n)

        for n in range(5, 11):
            setB.append(n)

        result = p6.intersection(setA, setB)
        self.assertEqual(0, result.size())

    def test_intersection_should_return_ll_with_values_in_both_a_and_b(self):
        """
        Test intersection() should return a linked list with the values in both set A and B.
        """
        setA = p6.LinkedList()
        setB = p6.LinkedList()

        setA.append(5)
        setB.append(5)
        result = p6.intersection(setA, setB)
        self.assertEqual(1, result.size())
        self.assertEqual('5 -> ', str(result))

        setB.append(8)
        result = p6.intersection(setA, setB)
        self.assertEqual(1, result.size())
        self.assertEqual('5 -> ', str(result))

        setA.append(52)
        result = p6.intersection(setA, setB)
        self.assertEqual(1, result.size())
        self.assertEqual('5 -> ', str(result))

        setB.append(52)
        result = p6.intersection(setA, setB)
        self.assertEqual(2, result.size())
        self.assertEqual('5 -> 52 -> ', str(result))

        setA.append(8)
        result = p6.intersection(setA, setB)
        self.assertEqual(3, result.size())
        self.assertEqual('5 -> 8 -> 52 -> ', str(result))

    def test_intersection_should_return_ll_with_distinct_values(self):
        """
        Test intersection() should return a linked list with distinct values.
        """
        setA = p6.LinkedList()
        setB = p6.LinkedList()

        for n in range(5):
            setA.append(n)
            setB.append(n)

        setA.append(3)
        setA.append(4)
        setB.append(2)
        setB.append(1)

        result = p6.intersection(setA, setB)
        self.assertEqual(5, result.size())
        self.assertEqual('0 -> 1 -> 2 -> 3 -> 4 -> ', str(result))


if __name__ == '__main__':
    unittest.main()
