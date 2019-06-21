#!/usr/bin/env python3

import unittest
import problem_4 as p4


class Test_ActiveDirectory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        p4.users = dict()

    def tearDown(self):
        p4.users = dict()

    def test_should_return_false_when_no_users(self):
        """
        Test is_user_in_group() should return false when there are no users.
        """
        groups = self._create_groups(3)
        self.assertFalse(p4.is_user_in_group('user1', groups[0]))
        self.assertFalse(p4.is_user_in_group('user1', groups[1]))
        self.assertFalse(p4.is_user_in_group('user1', groups[2]))

    def test_should_return_false_when_user_doesnt_exist(self):
        """
        Test is_user_in_group() should return false when the user doesn't exist.
        """
        groups = self._create_groups(3)
        groups[2].add_user('user2')
        groups[1].add_group(groups[2])
        groups[0].add_user('user1')
        groups[0].add_group(groups[1])
        self.assertFalse(p4.is_user_in_group('user3', groups[0]))
        self.assertFalse(p4.is_user_in_group('user3', groups[1]))
        self.assertFalse(p4.is_user_in_group('user3', groups[2]))

    def test_should_find_user_in_root(self):
        """
        Test is_user_in_group() should find the user in the root.

                Group 0
                   |
              ----------
             |          |
            user1    Group 1
                        |
                     Group 2
        """
        groups = self._create_groups(3)
        groups[0].add_user('user1')
        groups[1].add_group(groups[2])
        groups[0].add_group(groups[1])
        groups[0].add_group(groups[1])

        self.assertTrue(p4.is_user_in_group('user1', groups[0]))
        self.assertFalse(p4.is_user_in_group('user1', groups[1]))
        self.assertFalse(p4.is_user_in_group('user1', groups[2]))

    def test_should_find_user_in_last_subgroup(self):
        """
        Test is_user_in_group() should find the user in last subgroup.

                Group 0
                   |
                Group 1
                   |
                Group 2
                   |
                 user1
        """
        groups = self._create_groups(3)
        groups[0].add_user('user1')
        groups[2].add_user('user1')
        groups[1].add_group(groups[2])
        groups[0].add_group(groups[1])

        self.assertTrue(p4.is_user_in_group('user1', groups[0]))
        self.assertTrue(p4.is_user_in_group('user1', groups[1]))
        self.assertTrue(p4.is_user_in_group('user1', groups[2]))

    def test_should_find_user_in_hierarchy(self):
        """
        Test is_user_in_group() should find the user in hierarchy.

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
        """
        groups = self._create_groups(5)
        groups[4].add_user('user5')
        groups[4].add_user('user6')
        groups[3].add_user('user4')
        groups[3].add_group(groups[4])
        groups[2].add_user('user3')
        groups[2].add_group(groups[3])
        groups[1].add_user('user2')
        groups[0].add_user('user1')
        groups[0].add_group(groups[1])
        groups[0].add_group(groups[2])

        self.assertTrue(p4.is_user_in_group('user1', groups[0]))
        self.assertFalse(p4.is_user_in_group('user1', groups[1]))
        self.assertFalse(p4.is_user_in_group('user1', groups[2]))
        self.assertFalse(p4.is_user_in_group('user1', groups[3]))
        self.assertFalse(p4.is_user_in_group('user1', groups[4]))

        self.assertTrue(p4.is_user_in_group('user2', groups[0]))
        self.assertTrue(p4.is_user_in_group('user2', groups[1]))
        self.assertFalse(p4.is_user_in_group('user2', groups[2]))
        self.assertFalse(p4.is_user_in_group('user2', groups[3]))
        self.assertFalse(p4.is_user_in_group('user2', groups[4]))

        self.assertTrue(p4.is_user_in_group('user3', groups[0]))
        self.assertFalse(p4.is_user_in_group('user3', groups[1]))
        self.assertTrue(p4.is_user_in_group('user3', groups[2]))
        self.assertFalse(p4.is_user_in_group('user3', groups[3]))
        self.assertFalse(p4.is_user_in_group('user3', groups[4]))

        self.assertTrue(p4.is_user_in_group('user4', groups[0]))
        self.assertFalse(p4.is_user_in_group('user4', groups[1]))
        self.assertTrue(p4.is_user_in_group('user4', groups[2]))
        self.assertTrue(p4.is_user_in_group('user4', groups[3]))
        self.assertFalse(p4.is_user_in_group('user4', groups[4]))

        self.assertTrue(p4.is_user_in_group('user5', groups[0]))
        self.assertFalse(p4.is_user_in_group('user5', groups[1]))
        self.assertTrue(p4.is_user_in_group('user5', groups[2]))
        self.assertTrue(p4.is_user_in_group('user5', groups[3]))
        self.assertTrue(p4.is_user_in_group('user5', groups[4]))

        self.assertTrue(p4.is_user_in_group('user6', groups[0]))
        self.assertFalse(p4.is_user_in_group('user6', groups[1]))
        self.assertTrue(p4.is_user_in_group('user6', groups[2]))
        self.assertTrue(p4.is_user_in_group('user6', groups[3]))
        self.assertTrue(p4.is_user_in_group('user6', groups[4]))

    def _create_groups(self, num_groups):
        """Returns a list of groups."""
        groups = []
        for n in range(num_groups):
            groups.append(p4.Group('Group {}'.format(n)))
        return groups


if __name__ == '__main__':
    unittest.main()
