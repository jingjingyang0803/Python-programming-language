"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 4.8 - Geometric patterns:
 Complete the code of the program that prompts the user to select a
  geometric pattern (a square or a rectangle or c circle) and to enter the
  required dimensions. The program prints the circumference and area of the
  pattern to two decimal places. The program first prints a menu where the
  user can select their desired pattern or stop the program (s = square,
  r = rectangle and q = quit). This is the menu where the user returns after
  performing the previously selected action.
 If something other than n, s ,c or q is entered, the program prints error
  message "Incorrect entry, try again!" and returns to the pattern
  selection. If a negative number or a zero is entered as a dimension,
  the user is asked to re-enter the value, using the same prompt as originally.


Example output:
    Enter the pattern's first letter or (q)uit: s
    Enter the length of the square's side: 2.2
    The circumference is 8.80
    The surface area is 4.84

    Enter the pattern's first letter or (q)uit: r
    Enter the length of the rectangle's side 1: -4
    Enter the length of the rectangle's side 1: 1.5
    Enter the length of the rectangle's side 2: -3.5
    Enter the length of the rectangle's side 2: 2.5
    The circumference is 8.00
    The surface area is 3.75

    Enter the pattern's first letter or (q)uit: y
    Incorrect entry, try again!

    Enter the pattern's first letter or (q)uit: s
    Enter the length of the square's side: 0
    Enter the length of the square's side: -3
    Enter the length of the square's side: 4
    The circumference is 16.00
    The surface area is 16.00

    Enter the pattern's first letter or (q)uit: c
    Enter the circle's radius: 1.5
    The circumference is 9.42
    The surface area is 7.07

    Enter the pattern's first letter or (q)uit: q
    Goodbye!

Learning Goals:
 Learning to find program parts that can be turned to functions. Rehearsing
 the creation of functions.
 Design your program using at least seven functions you defined by you. The
 main function does not count as one of them.
"""
from math import pi as PI

def menu():
    """Print a menu for user to select which geometric pattern to use in
     calculations.
    """
    choice = ""
    while choice != "q":
        choice = input("Enter the pattern's first letter or (q)uit: ")
        if choice == "s":
            a = read_number("Enter the length of the square's side: ")
            print_result(rectangle_circumference(a,a),rectangle_area(a,a))
        elif choice == "r":
            side1 = read_number("Enter the length of the rectangle's side 1: ")
            side2 = read_number("Enter the length of the rectangle's side 2: ")
            print_result(rectangle_circumference(side1,side2),
                         rectangle_area(side1,side2))
        elif choice == "c":
            radius = read_number("Enter the circle's radius: ")
            print_result(circle_circumference(radius),circle_area(radius))
        elif choice == "q":
            print("Goodbye!")
        else:
            print("Incorrect entry, try again!")
        # Print a new line after each calculation or error message for
        # better readability.
        print()

def read_number(prompt):
    """Read a positive number from user input. If the user enters a
     negative number or zero, the function prompts the user to enter a
     number again until a positive number is entered.

    :param prompt: the prompt message to display to the user
    :return: a positive number entered by the user
    """
    number = 0.0
    while number <= 0:
        number = float(input(prompt))
    return number

def rectangle_circumference(a, b):
    """Calculate the circumference of a rectangle with sides a and b.

    :param a: first side
    :param b: second side
    :return: circumference
    """
    return 2 * (a + b)

def rectangle_area(a, b):
    """Calculate the area of a rectangle with sides a and b.

    :param a: first side
    :param b: second side
    :return: area of the rectangle
    """
    return a * b

def circle_circumference(r):
    """Calculate the circumference of a circle with radius r.

    :param r: radius of circle
    :return: circumference of circle
    """
    return 2 * PI * r

def circle_area(r):
    """Calculate the area of a circle with radius r.

    :param r: radius of circle
    :return: area of circle
    """
    return PI * r * r

def print_result(circumference_value, area_value):
    """Print the circumference and area values formatted to two decimal places.
    :param circumference_value: circumference
    :param area_value: area
    :return: None
    """
    print(f"The circumference is {circumference_value:.2f}")
    print(f"The surface area is {area_value:.2f}")


def main():
    menu()

if __name__ == "__main__":
    main()
