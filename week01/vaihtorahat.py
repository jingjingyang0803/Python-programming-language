"""
COMP.CS.100 Programming 1: Introduction to Programming implementation for
2026 spring

Learning Goals:
Learning about using arithmetic operators in Python and making calculations
 with integers.

Create a program that asks how much purchases cost and the amount of paid money
 and then prints the amount of change. To simplify the program, only 1, 2, 5
 and 10 euros are offered as change.
It is assumed that the paid amount is always euros, i.e. no cents are paid
 besides euros. It is further assumed that the paid amount is always at least 1
 euro.

Examples of how the program works:
Purchase price: 12
Paid amount of money: 50
Offer change:
3 ten-euro notes
1 five-euro notes
1 two-euro coins
1 one-euro coins

Creator: Jingjing Yang
Student id number: 154016843
"""
def main():
    purchase_price = int(input("Purchase price: "))
    paid_amount = int(input("Paid amount of money: "))

    change = paid_amount - purchase_price

    if change <= 0:
        print("No change")
    else:
        print("Offer change:")

        tens = change // 10
        if tens:
            print(tens, "ten-euro notes")

        change = change % 10
        fives = change // 5
        if fives:
            print(fives, "five-euro notes")

        change = change % 5
        twos = change // 2
        if twos:
            print(twos, "two-euro coins")

        change = change % 2
        ones = change // 1
        if ones:
            print(ones, "one-euro coins")

if __name__ == "__main__":
    main()