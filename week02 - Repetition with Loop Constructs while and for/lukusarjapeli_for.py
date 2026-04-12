"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 2.5.1 - Number series game Zip Boing Using for-loop:
 Implement the Zip Boing game using for as the loop structure.

Example:
    How many numbers would you like to have? 10
    1
    2
    zip
    4
    5
    zip
    boing
    8
    zip
    10

Learning Goals:
 Getting familiar with the for-loop repetition structure. Understanding the
 difference to a while-loop.
"""

def main():
    number_range = int(input("How many numbers would you like to have? "))

    # Use a for loop to iterate through the numbers from 1 to the total
    # specified by the user.
    for i in range(1, number_range + 1):
        if i % 3 == 0 and i % 7 == 0:
            print("zip boing")
        elif i % 3 == 0:
            print("zip")
        elif i % 7 == 0:
            print("boing")
        else:
            print(i)


if __name__ == "__main__":
    main()