#!/usr/bin/env python3


class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = dict()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users[user] = None

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

    def _is_user_in_group(user, group, result=None):
        """Checks if the user is in the group. If found, returns; else, recursively calls subgroups."""
        if result is not None:
            return result

        if user in group.get_users():
            return True

        for subgroup in group.get_groups():
            result = _is_user_in_group(user, subgroup)
            if result:
                return result

        return False

    return _is_user_in_group(user, group)


if __name__ == '__main__':
    def _create_groups(num_groups):
        groups = []
        for n in range(num_groups):
            groups.append(Group('Group {}'.format(n)))
        return groups

    def run_edge_case_1():
        """Edge Case: No users."""
        print('Running no users edge case....')
        groups = _create_groups(3)

        print(is_user_in_group('user1', groups[0]))     # False
        print(is_user_in_group('user1', groups[1]))     # False
        print(is_user_in_group('user1', groups[2]))     # False

    def run_edge_case_2():
        """Edge Case: user is the root group."""
        print('\nRunning user in root edge case....')
        groups = _create_groups(3)

        groups[0].add_user('user1')
        groups[1].add_group(groups[2])
        groups[0].add_group(groups[1])

        """
                Group 0
                   |
              ----------
             |          |
            user1    Group 1
                        |
                     Group 2
        """

        print(is_user_in_group('user1', groups[0]))     # True
        print(is_user_in_group('user1', groups[1]))     # False
        print(is_user_in_group('user1', groups[2]))     # False

    def run_edge_case_3():
        """Edge Case: user is in the last subgroup."""
        print('\nRunning user in last subgroup case....')
        groups = _create_groups(3)

        groups[2].add_user('user1')
        groups[1].add_group(groups[2])
        groups[0].add_group(groups[1])

        """
                Group 0
                   |
                Group 1
                   |
                Group 2
                   |
                 user1 
        """

        print(is_user_in_group('user1', groups[0]))     # True
        print(is_user_in_group('user1', groups[1]))     # True
        print(is_user_in_group('user1', groups[2]))     # True

    run_edge_case_1()
    run_edge_case_2()
    run_edge_case_3()
