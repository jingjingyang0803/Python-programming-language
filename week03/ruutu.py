"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 3.6.3 - Printing a box:
 Implement the function print_box to be used by the attached main program,
 so that the program prints great-looking boxes like this:

    Enter the width of a frame: 6
    Enter the height of a frame: 3
    Enter a print mark: *

    ******
    ******
    ******

Learning Goals:
 Understanding what happens when a parameter is passed from the main
 function to another function.
"""

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
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
