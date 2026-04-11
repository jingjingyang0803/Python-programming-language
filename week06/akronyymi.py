"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 6.7 - Forming an Acronym:
Implement the function create_an_acronym, which requests a name as a
  parameter and returns its acronym. An acronym is formed by taking the
  first letter of every word in a name and capitalizing it.
It is assumed that the caller of the function always passes at least one
  character as a parameter value (an empty string "" cannot be a parameter
  value).

Learning Goals:
 Familiarizing yourself with the string methods of Python.
"""
def create_an_acronym(name):
    """Returns an acronym formed by taking the first letter of every word
     in a name and capitalizing it.

    :param name: str,
        The name, not empty.

    :return: str,
        The acronym formed by taking the first letter of every word in a name.
    """
    words = name.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym


def main():
    print(create_an_acronym("central intelligence agency"))  # 'CIA'

if __name__ == "__main__":
    main()