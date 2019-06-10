#!/usr/bin/env python3

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # Bail out if no path is given.
    if not bool(path):
        return []

    # If a falsey is given for the suffix, set it to None to simplify the file suffix conditional check.
    if not bool(suffix):
        suffix = None

    def _find_files(path, files):
        """Recursively walk through the filesystem to find all files that end with the given suffix."""
        for entry in os.listdir(path):
            fullpath = os.path.join(path, entry)
            if os.path.isdir(fullpath):
                files = _find_files(fullpath, files)

            elif os.path.isfile(fullpath) and (suffix is None or entry.endswith(suffix)):
                files.append(fullpath)

        return files

    return _find_files(path, [])


if __name__ == '__main__':
    # print (os.listdir('.'))

    def run_test(suffix, path):
        files = find_files(suffix, path)
        if len(files) == 0:
            print('No files found.\n')
            return

        for fullpath in files:
            print(fullpath)
        print()

    run_test('', '')
    # should print:
    # No files found.

    run_test('.c', None)
    # should print:
    # No files found.

    run_test('.c', './fixtures/problem_2/testdir')
    # should print:
    # ./fixtures/problem_2/testdir/subdir3/subsubdir1/b.c
    # ./fixtures/problem_2/testdir/t1.c
    # ./fixtures/problem_2/testdir/subdir5/a.c
    # ./fixtures/problem_2/testdir/subdir1/a.c

    run_test('_2.py', '.')
    # should print:
    # ./problem_2.py
    # ./tests_2.py

    run_test('', './fixtures/problem_2/')
    # should print all files:
    # ./fixtures/problem_2/testdir/subdir4/.gitkeep
    # ./fixtures/problem_2/testdir/subdir3/subsubdir1/b.h
    # ./fixtures/problem_2/testdir/subdir3/subsubdir1/b.c
    # ./fixtures/problem_2/testdir/t1.c
    # ./fixtures/problem_2/testdir/subdir2/.gitkeep
    # ./fixtures/problem_2/testdir/subdir5/a.h
    # ./fixtures/problem_2/testdir/subdir5/a.c
    # ./fixtures/problem_2/testdir/t1.h
    # ./fixtures/problem_2/testdir/subdir1/a.h
    # ./fixtures/problem_2/testdir/subdir1/a.c
