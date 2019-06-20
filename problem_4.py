#!/usr/bin/env python3

import sys


class User:
    def __init__(self, id):
        self.id = id
        self.member_of = dict()

    def get_id(self):
        return self.id

    def join(self, group):
        self.member_of[group.get_name()] = group

    def get_groups(self):
        return self.member_of

    def is_member_of(self, group):
        if type(group) is Group:
            group = group.get_name()

        return group in self.member_of


class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    user = get_user(user)

    return user.is_member_of(group)


def get_user(user):
    """
    Returns the user by the given user name or ID.

    If does not exist, creates a new user and adds to the users map.

    Args:
      user(str|class:User): user name/id or instance of User
    """
    if type(user) is User:
        return user

    global users
    if user not in users:
        users[user] = User(user)

    return users[user]


def join_group(user, group):
    """
    Handles the user joining the group.

    Args:
      user(str|class:User): user name/id or the instance of the user.
      group(class:Group): group for the user to join.
    """
    if type(user) is not User:
        user = get_user(user)

    user.join(group)
    group.add_user(user)


if __name__ == '__main__':
    global users
    users = dict()

    def print_user(user_id):
        print('User {} in: R&D {}, DX {}, DevRel {}'.format(
            user_id,
            is_user_in_group(user_id, rd_group),
            is_user_in_group(user_id, dx_eng),
            is_user_in_group(user_id, devrel)
        ))

    print("Data size: {}".format(sys.getsizeof(users)))

    rd_group = Group('R&D Group')
    dx_eng = Group("DX Engineering")
    devrel = Group("DevRel Team")
    rd_group.add_group(dx_eng)
    dx_eng.add_group(devrel)

    for i in range(500):
        user_id = 'user' + str(i)
        join_group(user_id, devrel)
        print_user(user_id)

    for i in range(500, 900):
        user_id = 'user' + str(i)
        join_group(user_id, dx_eng)
        print_user(user_id)

    for i in range(900, 940):
        user_id = 'user' + str(i)
        join_group(user_id, dx_eng)
        print_user(user_id)

    print ("\nData size: {}; len {}\n".format(sys.getsizeof(users), len(users)))

    # Edge case of user not in the group
    print_user('does_not_exist')
    user = get_user('user_not_in_a_group')
    print_user(user.get_id())
