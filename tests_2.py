#!/usr/bin/env python3

import unittest
from problem_2 import find_files


class Test_FindFiles(unittest.TestCase):

    def test_should_return_empty_list_when_path_given(self):
        """
        Test find_files() should return an empty list when no path is given.
        """
        self.assertListEqual([], find_files('', ''))
        self.assertListEqual([], find_files('', None))
        self.assertListEqual([], find_files('', False))
        self.assertListEqual([], find_files('', []))
        self.assertListEqual([], find_files('.c', ''))
        self.assertListEqual([], find_files('.h', ''))
        self.assertListEqual([], find_files('.py', ''))
        self.assertListEqual([], find_files('.md', ''))

    def test_should_return_all_files_when_no_suffix_given(self):
        """
        Test find_files() should return a list of all files when no suffix is given.
        """
        expected = [
            './fixtures/problem_2/testdir/t1.c',
            './fixtures/problem_2/testdir/t1.h',
            './fixtures/problem_2/testdir/subdir2/.gitkeep',
            './fixtures/problem_2/testdir/subdir1/a.c',
            './fixtures/problem_2/testdir/subdir1/a.h',
            './fixtures/problem_2/testdir/subdir3/subsubdir1/b.c',
            './fixtures/problem_2/testdir/subdir3/subsubdir1/b.h',
            './fixtures/problem_2/testdir/subdir4/.gitkeep',
            './fixtures/problem_2/testdir/subdir5/a.c',
            './fixtures/problem_2/testdir/subdir5/a.h',
        ]
        expected.sort()

        actual = find_files('', './fixtures/problem_2')
        actual.sort()
        self.assertListEqual(expected, actual)

        actual = find_files('', './fixtures/problem_2/testdir')
        actual.sort()
        self.assertListEqual(expected, actual)

    def test_set_should_return_all_files_ending_in_c(self):
        """
        Test find_files() should return a list of all files that end with the .c extension.
        """
        expected = [
            './fixtures/problem_2/testdir/t1.c',
            './fixtures/problem_2/testdir/subdir1/a.c',
            './fixtures/problem_2/testdir/subdir3/subsubdir1/b.c',
            './fixtures/problem_2/testdir/subdir5/a.c',
        ]
        expected.sort()

        actual = find_files('c', './fixtures/problem_2')
        actual.sort()
        self.assertListEqual(expected, actual)

        actual = find_files('.c', './fixtures/problem_2')
        actual.sort()
        self.assertListEqual(expected, actual)

        actual = find_files('.c', './fixtures/problem_2/testdir')
        actual.sort()
        self.assertListEqual(expected, actual)

    def test_set_should_return_all_files_ending_in_h(self):
        """
        Test find_files() should return a list of all files that end with the .h extension.
        """
        expected = [
            './fixtures/problem_2/testdir/t1.h',
            './fixtures/problem_2/testdir/subdir1/a.h',
            './fixtures/problem_2/testdir/subdir3/subsubdir1/b.h',
            './fixtures/problem_2/testdir/subdir5/a.h',
        ]
        expected.sort()

        actual = find_files('h', './fixtures/problem_2')
        actual.sort()
        self.assertListEqual(expected, actual)

        actual = find_files('.h', './fixtures/problem_2')
        actual.sort()
        self.assertListEqual(expected, actual)

        actual = find_files('.h', './fixtures/problem_2/testdir')
        actual.sort()
        self.assertListEqual(expected, actual)

    def test_should_return_all_files_ending_in_gitkeep(self):
        """
        Test find_files() should return a list of all files that end with the .h extension.
        """
        expected = [
            './fixtures/problem_2/testdir/subdir2/.gitkeep',
            './fixtures/problem_2/testdir/subdir4/.gitkeep',
        ]

        actual = find_files('keep', './fixtures/problem_2')
        actual.sort()
        self.assertListEqual(expected, actual)

        actual = find_files('.gitkeep', './fixtures/problem_2/testdir')
        actual.sort()
        self.assertListEqual(expected, actual)


    def test_should_return_all_files_with_given_suffix(self):
        """
        Test find_files() should return a list of all files that end with the given suffix.
        """
        expected = [
            './problem_2.py',
            './tests_2.py',
        ]
        actual = find_files('_2.py', '.')
        self.assertListEqual(expected, actual)

        expected = [
            './explanation_2.md',
            './given_2.md',
        ]
        actual = find_files('_2.md', '.')
        self.assertListEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
