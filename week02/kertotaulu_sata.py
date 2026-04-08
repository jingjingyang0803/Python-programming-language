"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 2.3.2 - Multiplication table, values over a hundred:
 Create a program that prints a multiplication table for a given number
 until it reaches a result that is more than hundred.

Example:
    Choose a number: 6
    1 * 6 = 6
    2 * 6 = 12
    3 * 6 = 18
    ...
    17 * 6 = 102

Learning Goals:
 Creating a repetition structure where the number of repetitions is not
 known (calculated) in advance. Comparing the repetition structure to the
 repetition structure implemented in the previous part.
"""

def main():
    number = int(input("Choose a number: "))
    multiplier = 1
    result = multiplier * number

    while result <= 100:
        result = multiplier * number
        print(str(multiplier) + " * " + str(result) + " = " + str(result))
        multiplier += 1


if __name__ == "__main__":
    main()