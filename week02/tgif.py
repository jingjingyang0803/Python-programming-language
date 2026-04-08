"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 2.8.3 - TGIF:
 Create a program that prints the dates for all the Fridays in 2014. In
 2014, the first Friday was 3.1.

Programming tips:
 One possible solution is based on every seventh day being Friday. In the
 previous task, you implemented a program that goes through all the dates
 of a year. You can add this program a counter whose value is always
 increased by one when the program goes through the dates. The calculator
 can then be used to create a decision structure, which only prints on every
 seventh date.
"""

def main():
    counter = 0
    for month in range(1, 13):
        # determine the number of days in the month
        if month in (1, 3, 5, 7, 8, 10, 12):
            days = 31
        elif month in (4, 6, 9, 11):
            days = 30
        else:
            days = 28

        # print the date if it is a Friday
        for day in range(1, days + 1):
            counter += 1
            if (counter - 3) % 7 == 0:
                print(f"{day}.{month}.")

if __name__ == "__main__":
    main()