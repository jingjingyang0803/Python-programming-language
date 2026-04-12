"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 5.5.2 - A Function for Reviewing a List's Order of
Magnitude:


Learning Goals:
 Familiarizing yourself with the prebuilt operations the list contains,
  ie. the functions and the methods that can be used to perform operations
  to the list. At the same time, practising the use of the list as a
  function parameter.
"""
def is_the_list_in_order(some_list):
    """ Checks if the elements of the list are in order of magnitude.

    :param some_list: list to check
    :return: boolean, True if list is in order of magnitude, False otherwise
    """
    for i in range(len(some_list) - 1):
        if some_list[i] > some_list[i + 1]:
            return False
    return True


def main():
    print(is_the_list_in_order([37, 42, 43]))
    print(is_the_list_in_order([42, 37, 43]))

if __name__ == "__main__":
    main()