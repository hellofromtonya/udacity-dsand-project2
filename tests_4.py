#!/usr/bin/env python3

import unittest
import problem_4 as p4


class Test_ActiveDirectory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        p4.users = dict()

    def tearDown(self):
        p4.users = dict()

    def test_group_get_name_should_return_the_name(self):
        """
        Test Group::get_name() should return the name.
        """
        group = p4.Group('Group 2')
        self.assertEqual('Group 2', group.get_name())

    def test_group_add_group_should_add_the_given_group(self):
        """
        Test Group::add_group() should add the given group to the `groups` attribute.
        """
        group1 = p4.Group('Group 1')
        group2 = p4.Group('Group 2')

        self.assertEqual(0, len(group1.groups))
        group1.add_group(group2)
        self.assertEqual(1, len(group1.groups))
        self.assertEqual(group2, group1.groups[0])

    def test_get_user_should_create_and_return_user(self):
        """
        Test get_user() should create and return the user.
        """
        user_id = 'user1'
        self.assertFalse(user_id in p4.users)
        user = p4.get_user(user_id)
        self.assertEqual(user_id, user.get_id())
        self.assertTrue(user_id in p4.users)

    def test_get_user_should_return_existing_user(self):
        """
        Test get_user() should return existing user.
        """
        user_id = 'user1'
        p4.users[user_id] = p4.User(user_id)
        self.assertEqual(p4.users[user_id], p4.get_user(user_id))

    def test_user_join_should_add_group_to_member_of(self):
        """
        Test User::join() should add the given group to the `member_of` attribute.
        """
        group = p4.Group('Group 2')
        user = p4.User('user2')

        self.assertFalse(user.member_of)
        user.join(group)
        self.assertEqual(1, len(user.member_of.keys()))
        self.assertTrue('Group 2' in user.member_of)
        self.assertEqual(group, user.member_of['Group 2'])

    def test_user_is_member_of_should_return_if_user_has_joined_given_group(self):
        """
        Test User::is_member_of() should check if the user is a member of the given group.
        """
        group1 = p4.Group('Group 1')
        group2 = p4.Group('Group 2')
        group3 = p4.Group('Group 3')

        user = p4.User('user1')
        user.join(group1)
        user.join(group2)

        # Test with the object.
        self.assertTrue(user.is_member_of(group1))
        self.assertTrue(user.is_member_of(group2))
        self.assertFalse(user.is_member_of(group3))

        # Test with the group name.
        self.assertTrue(user.is_member_of('Group 1'))
        self.assertTrue(user.is_member_of('Group 2'))
        self.assertFalse(user.is_member_of('Group 3'))

        # Check with different hierarchies of groups within groups.
        group2.add_group(group3)
        group1.add_group(group2)
        self.assertTrue(user.is_member_of(group1))
        self.assertTrue(user.is_member_of(group2))
        self.assertFalse(user.is_member_of(group3))

    def test_join_group_should_make_user_member_of_group(self):
        """
        Test join_group() should make the user a member of the group.
        """
        group1 = p4.Group('Group 1')
        user_id = 'user1'
        p4.join_group(user_id, group1)

        self.assertEqual(p4.users[user_id], p4.get_user(user_id))
        self.assertEqual(p4.users[user_id], p4.get_user(user_id))
        self.assertTrue(user_id in p4.users)
        self.assertListEqual([p4.users[user_id]], group1.users)
        self.assertListEqual([p4.users[user_id]], group1.get_users())

    def test_is_user_in_group_should_check_if_user_member_of_group(self):
        """
        Test is_user_in_group() should check if the user is a member of the group.
        """
        group1 = p4.Group('Group 1')
        user = 'user1'

        # Test when the user is not a member of the group.
        self.assertFalse(p4.is_user_in_group(user, group1))
        self.assertFalse(p4.is_user_in_group(p4.users[user], group1))

        # Test when the user is a member of the group.
        p4.join_group(user, group1)
        self.assertTrue(p4.is_user_in_group(user, group1))
        self.assertTrue(p4.is_user_in_group(p4.users[user], group1))


if __name__ == '__main__':
    unittest.main()
