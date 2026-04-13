"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 10.4 - Product:
 Make methods set_sale_percentage and get_price work correctly.

Learning Goals:
 I will practise more about defining methods and attributes.
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        # sale percentage is always 0.0% in new objects
        self.sale_percentage = 0.0

    def printout(self):
        print(self.name)
        print(f"  price: {self.price:.2f}")
        print(f"  sale%: {self.sale_percentage:.2f}")

    def set_sale_percentage(self, percentage: float):
        if percentage >= 0 or percentage <= 100:
            self.sale_percentage = percentage

    def get_price(self) -> float:
        return self.price * (1 - self.sale_percentage / 100)


def main():

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
