"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 3.8.2 - Printing a box and checking the inputs:
 Check that the numbers entered by the user are greater than zero.

Example:
    Enter the width of a frame: -1
    Enter the width of a frame: 0
    Enter the width of a frame: -4
    Enter the width of a frame: 4
    Enter the height of a frame: -1
    Enter the height of a frame: 0
    Enter the height of a frame: 2
    Enter a print mark: #

    ####
    ####

Learning Goals:
 Practising functions in further detail.
"""
def read_input(prompt_text):
    """
    Reads input from the user.
    Parameters:
        prompt_text: the prompt text to be shown to the user
    Returns:
        The input read from the user, as an integer greater than zero.
    """
    user_input = 0
    while user_input <= 0:
        user_input = int(input(prompt_text))
    return user_input


def print_box(width, height, mark):
    """
    Prints a box of given width and height, using the given mark.
    Parameters:
        width: the width of the box (number of marks in one line)
        height: the height of the box (number of lines)
        mark: the mark used to print the box
    Returns:
        None
    """
    for i in range(int(height)):
        print(mark * int(width))


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
