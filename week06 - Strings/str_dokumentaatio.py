"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 6.8 - Capitalization:
Create the function capitalize_initial_letters, which uses a string as a
  parameter and returns it as written, with each word starting in upper
  case but the rest of the world in lower case.
The parameter value can be an empty string "". The function returns an
  empty string, if the parameter value is an empty string

Learning Goals:
 Getting acquainted with string methods in Python. Learning to use Python's
 documentation.
"""
def capitalize_initial_letters(name):
    """
    Returns the string with each word starting in upper case but the rest of
    the world in lower case.

    :param name: A string.

    :return: The string with each word starting in upper case but the rest of
             the world in lower case.
    """
    return name.title()


def main():
    print(capitalize_initial_letters("drIVING cAR"))  # 'Driving Car'


if __name__ == "__main__":
    main()