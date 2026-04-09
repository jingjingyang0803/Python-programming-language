"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 4.11.1 - Improved Box Printing:
 Printing of the box uses two different print marks:
    One for printing the box's edge,
    the other for printing the box's inner part.
 The default values of the print marks are "#" and " ".
 Parameters have also been named.


Learning Goals:
 Getting to know optional and named parameters.
"""
def print_box(width, height, border_mark="#", inner_mark=" "):
    """Prints a box of given width and height, using specified characters
     for the border and inner part.
    :param width: Width of the box.
    :param height: Height of the box.
    :param border_mark: Mark of the border mark, default is "#".
    :param inner_mark: Mark of the inner part, default is ".
    :return: None
    """
    for i in range(height):
        for j in range(width):
            # Print the border mark for the first and last line
            if i == 0 or i == height - 1:
                print(border_mark, end="")
            # Print the border mark for the first and last column
            elif j == 0 or j == width - 1:
                print(border_mark, end="")
            # Print inner mark for the rest
            else:
                print(inner_mark, end="")
        print()  # Move to the next line after printing each line of the box.
    print() # Print an empty line after printing the box for better readability.


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)

if __name__ == "__main__":
    main()