"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 2.3.1 - Multiplication table, school version:
 Create a program that prints a multiplication table for an entered number
 just like in school, using steps of one to ten.

Example:
    Choose a number: 6
    1 * 6 = 6
    2 * 6 = 12
    3 * 6 = 18
    ...
    10 * 6 = 60

Learning Goals:
 Learning to implement a repetition using a while structure so that the
 number of times for repetition is known in advance.
"""

def main():
    number = int(input("Choose a number: "))
    i = 1
    while i <= 10:
        print(f"{i} * {number} = {i * number}")
        i += 1

if __name__ == "__main__":
    main()