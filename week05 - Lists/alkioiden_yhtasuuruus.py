"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 5.5.1 - A Function for Comparing Whether List Members Have
an Equal Value:
 Create the function are_all_members_same, which uses a list as a parameter
  and returns information on whether all the members contained by the list
  are the same.

Learning Goals:
 Familiarizing yourself with the prebuilt operations the list contains,
  meaning the functions and methods that you can use to perform operations
  for lists. Simultaneously, practising the use of the list as a function
  parameter.
"""
def are_all_members_same(some_list):
    """A function that checks if all the members contained by the list
    are the same.

    :param some_list: A list that contains all the members contained by the list.
    :return: True if all the members contained by the list are the same,
     False otherwise.
    """
    for i in range(len(some_list) - 1):
        if some_list[i] != some_list[i + 1]:
            return False
    return True


def main():
    print(are_all_members_same([42, 42, 42, 43, 42]))
    print(are_all_members_same([42, 42, 42, 42]))

if __name__ == "__main__":
    main()