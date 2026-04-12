"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 6.6 - Reverse the Names to Correct Order:
In various lists of names, names are sometimes presented in reverse order,
  the last name before the first name, so that there is a comma after the
  last name. Create a function reverse_name, which changes a string
  containing such a name to the order, where the first name is followed with
  the last name. The names are separated with a space and the comma as well
  as all unnecessary spaces are removed. The function returns the modified
  name.
It is assumed that the name string contains no more than one comma and
  that the caller of the function always passes at least one character as a
  parameter value (an empty string "" cannot be a parameter value).

Learning Goals:
 To get acquainted with the string methods in Python.
"""

def reverse_name(name):
    """Reverses the order of a name given in the format "Last, First" to
     "First Last".
     The function also removes any unnecessary spaces and the comma.
     It is assumed that the input string contains no more than one comma
      and is not empty.

    :param name:
        A string containing a name in the format "Last, First".

    :return:
        A string containing the name in the format "First Last".
    """
    parts = name.split(",")  # Split the name into parts using comma as a separator
    if len(parts) == 2:
        # Get the first name and remove extra whitespace
        first_name = parts[1].strip()
        # Get the last name and remove extra whitespace
        last_name = parts[0].strip()

        # Combine first and last name with a space and remove any extra
        # whitespace
        return (first_name + " " + last_name).strip()
    else:
        return name.strip()  # If there is no comma, print the name as
                             # is (after stripping whitespace)


def main():
    print(reverse_name("Techie, Teddy"))  # should output 'Teddy Techie'
    print(reverse_name("Scumble,    Arnold"))  # 'Arnold Scumble'
    print(reverse_name("Fortunato,Frank"))  # 'Frank Fortunato'
    print(reverse_name("von Grünbaumberger, Herbert"))  #'Herbert von Grünbaumberger'
    print(reverse_name("   Duck,     Donald  "))  # 'Donald Duck'

    print(reverse_name(" , Y "))  # 'Y'
    print(reverse_name(","))  # ''
    print(reverse_name("Stuart Student"))  # 'Stuart Student'


if __name__ == "__main__":
    main()