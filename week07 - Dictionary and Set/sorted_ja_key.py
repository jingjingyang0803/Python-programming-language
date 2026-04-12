"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 7.13 -- Sorting by Price:


Learning Goals:
 I will learn to use the key parameter for the sorted function.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}

def main():
    def product_price(name):
        return PRICES[name]

    for product_name in sorted(PRICES, key = product_price):
        print(f"{product_name} {PRICES[product_name]:.2f}")

if __name__ == "__main__":
    main()