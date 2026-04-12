"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 5.2 - Number Sequences:
 Create a program that first prints the even numbers from 0 to 100 in an
  ascending order, and then the same numbers in descending order. Each
  number is printed on its own row.

    0
    2
    4
    6
    ⋮
    98
    100
    100
    98
    ⋮
    4
    2
    0

Learning Goals:
 Lists are often processed using a for loop and a range function, so the
 purpose of the first task is reviewing how the for and range operate.
"""

def main():
    for i in range(0, 101, 2):
        print(i)
    for i in range(100, -1, -2):
        print(i)

if __name__ == "__main__":
    main()