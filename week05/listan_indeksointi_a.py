"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 5.3.1 - Going Through the Elements of a List:
 Create a program that first reads 5 numbers a user enters and then prints,
  in the order the user entered them, all the numbers that are greater than
  zero.

    Give 5 numbers:
    Next number: 0
    Next number: 1
    Next number: -2
    Next number: 3
    Next number: -4
    The numbers you entered that were greater than zero were:
    1
    3

Learning Goals:
 To learn about usign for loop to go through (iterate over) every element
  of a list.
"""

def main():
    print("Give 5 numbers: ")
    numbers = []

    i = 5
    while i:
        num=int(input("Next number: "))
        # append the number to the list if it is greater than zero
        if num>0:
            numbers.append(num)
        i -= 1

    # print the numbers greater than zero
    print("The numbers you entered that were greater than zero were:")
    for num in numbers:
        print(num)

if __name__ == "__main__":
    main()