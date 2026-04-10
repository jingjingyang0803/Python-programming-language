"""
COMP.CS.100 Programming 1.
Name:       Jingjing Yang
Email:      jingjing.yang@tuni.fi
Student Id: 154016843

6.2 - Project: Energy statistic:
 A program printing energy cunsumption histograms based on the data the
  user entered. The energy consumption values will be divided into classes
  based on a logarithmic scale.

Note: All the inputs for this program are integers (int) for simplicity.
     The program should be able to handle any non-negative integer values.

    Class number    Values belonging to the class
    1.              0–9
    2.              10–99
    3.              100–999
    4.              1000–9999
    5.              10000–99999
    ...             ...–...

Example output:
    Enter energy consumption data.
    End by entering an empty line.

    Enter energy consumption (kWh): 91
    Enter energy consumption (kWh): 10
    Enter energy consumption (kWh): 101
    Enter energy consumption (kWh): 912
    Enter energy consumption (kWh): 22
    Enter energy consumption (kWh): 6
    Enter energy consumption (kWh):
        0-9: *
      10-99: ***
    100-999: **

Learning Goals:
 Practise materials covered in the class in weeks 1–5.
"""

def main():
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()

    data = read_input()

    # Do not print the histogram if there is no data to print.
    if not data:
        print("Nothing to print. Done.")
        return

    # Print the histogram of the energy consumption values entered by the user.
    print_histogram(data)


def read_input():
    """
    Reads energy consumption values from the user until an empty line is
    entered.  The values are returned as a list of integers.

    :return: list of int
        The energy consumption values entered by the user.
    """
    input_data = []

    while True:
        user_input = input("Enter energy consumption (kWh): ")

        # If the user input is an empty line, break the loop.
        if user_input == "":
            break

        value = int(user_input) # Assume all input are integers for simplicity.

        # If the user input is negative, print an error message and
        # ask for input again.
        if value < 0:
            print(f"You entered: {value}. Enter non-negative numbers only!")
            continue

        # If the user input is valid, add it to the input data list.
        input_data.append(value)

    return input_data


def class_minimum_value(class_number):
    """
    Returns the smallest value of the given class number.

    :param class_number: int
        The class to find the smallest value.

    :return: int
        The smallest value of the class with the given <class_number>.
    """
    smallest_value = 10 ** class_number // 100 * 10
    return smallest_value


def class_maximum_value(class_number):
    """
    Returns the largest value of the given class number.

    :param class_number: int
        The class to find the largest value.

    :return: int
        The largest value of the class with the given <class_number>.
    """
    largest_value  = 10 ** class_number - 1
    return largest_value


def get_class_number(value):
    """
    Returns the class number the given value belongs to.

    :param value: int
        The value to check

    :return: int
        The class number the given value belongs to.
    """
    class_number = 1
    while True:
        if (class_minimum_value(class_number) <= value <=
                 class_maximum_value(class_number)):
           return class_number
        class_number += 1


def get_class_counts(data):
    """
    Counts how many values in the given data belong to each class.

    :param data: list of int
        The energy consumption values entered by the user.

    :return: list of int
        Counts of how many values in the given data belong to each class.
        The value at index n of the returned list is the count of values
        belonging to class n.
    """
    # Calculate the number of classes needed to cover all the values in the
    # input data.
    number_of_categories = get_class_number(max(data))

    # Initialize the class counts list with zeros.
    # The class numbers start from 1(0-9), so we need to add 1 to the
    # number of categories to have enough
    class_counts = [0] * (number_of_categories + 1)

    # For each value in the input data, determine which class it belongs to
    # and increment the count for that class.
    for value in data:
        class_number = get_class_number(value)
        class_counts[class_number] += 1

    return class_counts


def print_single_histogram_line(class_number, count, largest_class_number):
    """
    Prints one correctly indented histogram line.

    :param class_number: int,
        Expresses which consumption class (1, 2, 3, ...)
        should the histogram line be printed for. The <class_number> is used
        to decide which value range (0-9, 10-99, 100-999, ...) should be
        printed in front of the histogram markers ("*").

    :param count: int,
        How many of the values entered by the user belong to <class_number>.

    :param largest_class_number: int,
        What is the largest class out of all input values
        the user entered. This is needed when deciding the indentations
        for all other histogram lines.  For example, if the largest
        number the user entered was 91827364 (8 digits) the value
        of this paramter should be 8.
    """

    # <range_string> represents the range of the values the line's
    # histogram will represent in the printout.  For example "1000-9999".

    min_value = class_minimum_value(class_number)
    max_value = class_maximum_value(class_number)
    range_string = f"{min_value}-{max_value}"


    # How many characters will the largest class' range need when printed.
    # For example if the <largest_class_number> is 7, it would print
    # "1000000-9999999" in the beginning of the line and requires 15 characters.
    # This value defines the print width for all the other <range_string>'s.

    largest_width = 2 * largest_class_number + 1


    # Now all the preparations have been done and we can print the
    # histogram line with the correct number of whitespaces in the
    # beginning of the line followed by the correct number of '*'
    # characters. ">" character in the following f-string places
    # <range_string>'s value to the right edge of the output field
    # (filler white spaces will be printed in the beginning).

    print(f"{range_string:>{largest_width}}: {'*' * count}")


def print_histogram(data):
    """
    Prints the histogram of the energy consumption values in the given data.

    :param data: list of int
        The energy consumption values entered by the user.
    """
    class_counts = get_class_counts(data)

    # The largest class number is the last index in the counts list
    largest_class_number = len(class_counts) - 1

    # Print the histogram lines for all the classes from 1 to the largest
    # class number.
    for class_number in range(1, largest_class_number + 1):
        count = class_counts[class_number]
        print_single_histogram_line(class_number, count, largest_class_number)


if __name__ == "__main__":
    main()
