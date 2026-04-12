"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 2.8.2 - The dates of the year:
 Create a program that prints all the dates of a year which is not leap year:

    1.1.
    2.1.
    3.1.
    4.1.
    5.1.
    ...
    31.1.
    1.2.
    2.2.
    3.2.
    ...
    28.2.
    1.3.
    ...

Learning Goals:
 Practicing nested repetition structures.
"""

def main():
    for month in range(1, 13):
        # determine the number of days in the month
        if month in (1, 3, 5, 7, 8, 10, 12):
            days = 31
        elif month in (4, 6, 9, 11):
            days = 30
        else:
            days = 28

        # print the dates of the month
        for day in range(1, days + 1):
            print(f"{day}.{month}.")


if __name__ == "__main__":
    main()