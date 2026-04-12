"""
COMP.CS.100 Programming 1: Introduction to Programming implementation for
2026 spring

Learning Goals:
To learn the basic meaning of the error messages Python prints when there is an
 error in a program code.

Creator: Jingjing Yang
Student id number: 154016843
"""

"""
The price of a single ride bus ticket in Tampere
and surrounding areas on Aug 23rd, 2020.

The rules used by the program are:

  -----  -------
   Age    Price
  -----  -------
   >24     2.04
  17-24    1.47
   7-16    1.02
   0-6     0.00

Limited usefulness, the actual rules are more complex.
"""

def main():
    age = int(input("Please, enter your age: "))
    ticket_price = 0.0

    if age < 7:
        ticket_price = 0.00
    elif age < 17:
        ticket_price = 1.02
    elif age < 25:
        ticket_price = 1.47
    else:
        ticket_price = 2.04

    print("Your ride will cost: " + str(ticket_price))

if __name__ == "__main__":
    main()