"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 3.8.1 - Triangle's area:
  Implement the function area, which uses the lengths of the triangle's
  sides as its parameters, and calculates the triangle's area, and a main
  program that asks for the lengths of the sides from the user and prints
  the result of the calculation.

Learning Goals:
  Understanding what happens when a return value is passed from a function
  to the main function.
"""

from math import sqrt

def area(a, b, c):
    """
    Calculate the area of a triangle using Heron's formula.
    Parameters:
        a, b, c: float, float, float; sides of triangle
    Returns:
        area: float; area of the triangle
    """
    s = (a + b + c) / 2.0
    triangle_area = sqrt(s * (s - a) * (s - b) * (s - c))
    return triangle_area


def main():
    line1 = input("Enter the length of the first side: ")
    line2 = input("Enter the length of the second side: ")
    line3 = input("Enter the length of the third side: ")

    triangle_area = area(float(line1), float(line2), float(line3))
    print(f"The triangle's area is {triangle_area:.1f}")


if __name__ == "__main__":
    main()
