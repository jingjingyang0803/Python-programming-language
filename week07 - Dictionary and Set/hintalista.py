"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 7.3 - Price List:

    Enter product name:␣␣␣␣milk␣␣⏎
    The price of milk is 1.09 e
    Enter product name:␣␣␣meat␣␣␣⏎
    Error: meat is unknown.
    Enter product name:␣␣␣␣␣⏎
    Bye!

Learning Goals:
 I will understand how to index dict data structure to find the payload
 connected to the key.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}

def main():
    while True:
        # Remove leading and trailing whitespace characters from the input
        # string.
        product = input("Enter product name: ").strip()

        # End the program if the input string is empty.
        if not product:
            print("Bye!")
            break
        # Print price with two decimals if the product is in the price list.
        if product in PRICES:
            print(f"The price of {product} is {PRICES[product]:.2f} e")
        # Print an error message if the product is not in the price list.
        else:
            print(f"Error: {product} is unknown.")

if __name__ == "__main__":
    main()