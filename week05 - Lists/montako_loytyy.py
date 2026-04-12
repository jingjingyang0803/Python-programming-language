"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 5.4.1 - A List as a Return Value:
 Create a function named input_to_list which has 1 parameter: number of
  integers user needs to enter. The function then asks user to enter that
  many numbers, reads the numbers from the user, saves them in a list and
  returns that list.

 Also create a main function which:
    asks the user for the number of integers to be processed
    calls input_to_list to read the numbers from the user
    asks the user what number the user are searching for and
    prints data on whether the searched numbers are found from the entered
     numbers and, if so, how many times

Learning Goals:
 To familiarize yourself with the prebuilt operations of a list and their
  call notation, i.e. the functions and the methods that you can use to
  perform operations for a list. At the same time, to practice the use of
  a list as a function parameter and a return value.
"""

def input_to_list(amount):
    """A function that reads a given amount of integers from the user and
     returns a list containing those integers.

    :param amount: The amount of integers user needs to enter
    :return: A list containing those integers
    """
    print(f"Enter {amount} numbers:")
    list_numbers = []
    i=1
    while i<=amount:
        value=int(input(""))
        list_numbers.append(value)
        i+=1

    return list_numbers

def main():
    amount=int(input("How many numbers do you want to process: "))

    list_numbers=input_to_list(amount)

    number_to_search=int(input("Enter the number to be searched: "))

    count=list_numbers.count(number_to_search)
    if count>0:
        print(f"{number_to_search} shows up {count} times among the numbers "
              f"you have entered.")
    else:
        print(f"{number_to_search} is not among the numbers you have "
               f"entered.")


if __name__ == "__main__":
    main()