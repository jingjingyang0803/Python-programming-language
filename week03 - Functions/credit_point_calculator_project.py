"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 3.3 - Project: Credit Point Calculator:
 Implement a program which allows a student to follow their credit point gain.

Running Examples
1.Student has gained enough credit points during a four month period:
    Enter the number of months: 4
    Enter the number of credits in month 1: 3
    Enter the number of credits in month 2: 0
    Enter the number of credits in month 3: 9
    Enter the number of credits in month 4: 10

    You are a full time student and your monthly credit point average is 5.5.

2.Too few credits gained in nine months:
    Enter the number of months: 9
    Enter the number of credits in month 1: 0
    Enter the number of credits in month 2: 5
    Enter the number of credits in month 3: 0
    Enter the number of credits in month 4: 5
    Enter the number of credits in month 5: 0
    Enter the number of credits in month 6: 5
    Enter the number of credits in month 7: 0
    Enter the number of credits in month 8: 5
    Enter the number of credits in month 9: 0

    Your monthly credit point average 2.2 does not classify you as a full time student.

3.Two consecutive months without any acquired credit points:
    Enter the number of months: 8
    Enter the number of credits in month 1: 10
    Enter the number of credits in month 2: 0
    Enter the number of credits in month 3: 0

    You did have too many study breaks!
"""

def main():
        # Get the number of months from the user
        number_of_months = int(input("Enter the number of months: "))

        # Initialize variables to keep track of total credits and
        # consecutive zero months
        total_credits = 0
        consecutive_zero_months = 0

        # Loop through each month and get the number of credits for that month
        for month in range(1, number_of_months + 1):
            credits = int(input(f"Enter the number of credits in month "
                                 f"{month}: "))
            # Check for consecutive zero months
            if credits == 0:
                consecutive_zero_months += 1
            else:
                consecutive_zero_months = 0 # Reset if credits are not zero

            if consecutive_zero_months >= 2:
                print("\nYou did have too many study breaks!")
                return

            # Add the credits for the month to the total
            total_credits += credits

        # Calculate the average credits per month and print the result
        average_credits = total_credits / number_of_months
        if average_credits >= 5:
            print(f"\nYou are a full time student and your monthly credit "
                   f"point average is {average_credits:.1f}.")
        else:
            print(f"\nYour monthly credit point average"
                   f" {average_credits:.1f} does not classify you as a full time student.")


if __name__ == "__main__":
    main()