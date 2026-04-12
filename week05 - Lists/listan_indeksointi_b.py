"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 5.3.2 - Going Through the List Indices:
 Create a program that first reads 5 numbers a user has entered and then
  prints all the entered numbers in reverse order.

    Give 5 numbers:
    Next number: 2
    Next number: 7
    Next number: 3
    Next number: -8
    Next number: 6
    The numbers you entered, in reverse order:
    6
    -8
    3
    7
    2

Learning Goals:
 To practice the use of indexes when going through the values stored in a list.
"""

def main():
    print("Give 5 numbers: ")
    numbers = []

    i = 5
    while i:
        num=int(input("Next number: "))
        # append the number to the list
        numbers.append(num)
        i -= 1

    # print the numbers in reverse order
    print("The numbers you entered, in reverse order:")
    j = 1
    while j <= len(numbers):
        print(numbers[-j])
        j += 1

if __name__ == "__main__":
    main()