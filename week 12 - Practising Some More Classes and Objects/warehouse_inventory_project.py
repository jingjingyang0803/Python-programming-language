"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
StudentId: 154016843
Name:      Jingjing Yang
Email:     jingjing.yang@tuni.fi

This program manages a product warehouse. The user can print, delete,
modify, combine, and discount products stored in a database file.
"""

LOW_STOCK_LIMIT = 30


class Product:
    """
    This class represent a product i.e. an item available for sale.
    """

    def __init__(self, code, name, category, price, stock):
        self.__code = code
        self.__name = name
        self.__category = category
        self.__price = price
        self.__stock = stock
        self.__original_price = price

    def __str__(self):
        """
        YOU SHOULD NOT MODIFY THIS METHOD or it will mess up
        the automated tests.
        """

        lines = [
            f"Code:     {self.__code}",
            f"Name:     {self.__name}",
            f"Category: {self.__category}",
            f"Price:    {self.__price:.2f}€",
            f"Stock:    {self.__stock} units",
        ]

        longest_line = len(max(lines, key=len))

        for i in range(len(lines)):
            lines[i] = f"| {lines[i]:{longest_line}} |"

        solid_line = "+" + "-" * (longest_line + 2) + "+"
        lines.insert(0, solid_line)
        lines.append(solid_line)

        return "\n".join(lines)

    def __eq__(self, other):
        """
        YOU SHOULD NOT MODIFY THIS METHOD or it will mess up
        the automated tests since the read_database function will
        stop working correctly.
        """

        return self.__code == other.__code and \
               self.__name == other.__name and \
               self.__category == other.__category and \
               self.__price == other.__price

    def get_category(self):
        """
        Returns the category of the product.

        :return str: category
        """
        return self.__category

    def get_stock(self):
        """
        Returns the stock of the product.

        :return int: stock
        """
        return self.__stock

    def get_price(self):
        """
        Returns the price of the product.

        :return float: price
        """
        return self.__price

    def get_original_price(self):
        """
        Returns the original price of the product.

        :return float: original price
        """
        return self.__original_price

    def modify_stock_size(self, amount):
        """
        YOU SHOULD NOT MODIFY THIS METHOD since read_database
        relies on its behavior and might stop working as a result.

        Allows the <amount> of items in stock to be modified.
        This is a very simple method: it does not check the
        value of <amount> which could possibly lead to
        a negative amount of items in stock. Caveat emptor.

        :param amount: int, how much to change the amount in stock.
                       Both positive and negative values are accepted:
                       positive value increases the stock and vice versa.
        """

        self.__stock += amount

    def modify_price(self, amount):
        """
        Modifies the price of the product by the given amount.
        This method does not check the value of <amount> which
        could lead to a negative price. Caveat emptor.

        :param amount: float, how much to change the price.
                       Both positive and negative values are accepted:
                       positive value increases the price and vice versa.
        """
        self.__price = self.__original_price + amount

def _read_lines_until(fd, last_line):
    """
    YOU SHOULD NOT MODIFY THIS FUNCTION since read_database
    relies on its behavior and might stop working as a result.

    Reads lines from <fd> until the <last_line> is found.
    Returns a list of all the lines before the <last_line>
    which is not included in the list. Return None if
    file ends bofore <last_line> is found.
    Skips empty lines and comments (i.e. characeter '#'
    and everything after it on a line).

    You don't need to understand this function works as it is
    only used as a helper function for the read_database function.

    :param fd: file, file descriptor the input is read from.
    :param last_line: str, reads lines until <last_line> is found.
    :return: list[str] | None
    """

    lines = []

    while True:
        line = fd.readline()

        if line == "":
            return None

        hashtag_position = line.find("#")
        if hashtag_position != -1:
            line = line[:hashtag_position]

        line = line.strip()

        if line == "":
            continue

        elif line == last_line:
            return lines

        else:
            lines.append(line)


def read_database(filename):
    """
    YOU SHOULD NOT MODIFY THIS FUNCTION as it is ready.

    This function reads an input file which must be in the format
    explained in the assignment. Returns a dict containing
    the product code as the key and the corresponding Product
    object as the payload. If an error happens, the return value will be None.

    You don't necessarily need to understand how this function
    works as long as you understand what the return value is.
    You can probably learn something new though, if you examine the
    implementation.

    :param filename: str, name of the file to be read.
    :return: dict[int, Product] | None
    """

    data = {}

    try:
        with open(filename, mode="r", encoding="utf-8") as fd:

            while True:
                lines = _read_lines_until(fd, "BEGIN PRODUCT")
                if lines is None:
                    return data

                lines = _read_lines_until(fd, "END PRODUCT")
                if lines is None:
                    print(f"Error: premature end of file while reading '{filename}'.")
                    return None

                # print(f"TEST: {lines=}")

                collected_product_info = {}

                for line in lines:
                    keyword, value = line.split(maxsplit=1)  # ValueError possible

                    # print(f"TEST: {keyword=} {value=}")

                    if keyword in ("CODE", "STOCK"):
                        value = int(value)  # ValueError possible

                    elif keyword in ("NAME", "CATEGORY"):
                        pass  # No conversion is required for string values.

                    elif keyword == "PRICE":
                        value = float(value)  # ValueError possible

                    else:
                        print(f"Error: an unknown data identifier '{keyword}'.")
                        return None

                    collected_product_info[keyword] = value

                if len(collected_product_info) < 5:
                    print(f"Error: a product block is missing one or more data lines.")
                    return None

                product_code = collected_product_info["CODE"]
                product_name = collected_product_info["NAME"]
                product_category = collected_product_info["CATEGORY"]
                product_price = collected_product_info["PRICE"]
                product_stock = collected_product_info["STOCK"]

                product = Product(code=product_code,
                                  name=product_name,
                                  category=product_category,
                                  price=product_price,
                                  stock=product_stock)

                # print(product)

                if product_code in data:
                    if product == data[product_code]:
                        data[product_code].modify_stock_size(product_stock)

                    else:
                        print(f"Error: product code '{product_code}' conflicting data.")
                        return None

                else:
                    data[product_code] = product

    except OSError:
        print(f"Error: opening the file '{filename}' failed.")
        return None

    except ValueError:
        print(f"Error: something wrong on line '{line}'.")
        return None


def example_function_for_example_purposes(warehouse, parameters):
    """
    This function is an example of how to deal with the extra
    text user entered on the command line after the actual
    command word.

    :param warehouse: dict[int, Product], dict of all known products.
    :param parameters: str, all the text that the user entered after the command word.
    """

    try:
        # Let's try splitting the <parameters> string into two parts.
        # Raises ValueError if there are more or less than exactly two
        # values (in this case there should be one int and one float) in
        # the <parameters> string.
        code, number = parameters.split()

        # First parameter was supposed to be a products code i.e. an integer
        # and the second should be a float. If either of these assumptions fail
        # ValueError will be raised.
        code = int(code)
        number = float(number)

    except ValueError:
        print(f"Error: bad parameters '{parameters}' for example command.")
        return

    # <code> should be an existing product code in the <warehouse>.
    if code not in warehouse:
        print(f"Error: unknown product code '{code}'.")
        return

    # All the errors were checked above, so everything should be
    # smooth sailing from this point onward. Of course, the other
    # commands might require more or less error/sanity checks, this
    # is just a simple example.

    print("Seems like everything is good.")
    print(f"Parameters are: {code=} and {number=}.")


def handle_print(warehouse, parameters):
    """
    Handles the print command. If <parameters> is empty, prints all
     products in the warehouse in ascending order of their codes.
    Otherwise, <parameters> should be a product code and the corresponding
     product is printed. If the product code does not exist, an error
      message is printed.

    :param warehouse: dict[int, Product], all products
    :param parameters: str, all the text that the user entered after the
                       command word.
    """
    if parameters == "":
        for product_code in sorted(warehouse):
            print(warehouse[product_code])
        return

    error_message = (
        f"Error: product '{parameters}' can not be printed as it does not "
         f"exist."
    )

    try:
        code = int(parameters)
    except ValueError:
        print(error_message)
        return

    if code not in warehouse:
        print(error_message)
    else:
        print(warehouse[code])


def handle_delete(warehouse, parameters):
    """
    Handles the delete command. <parameters> should be a product code.
    If the product code does not exist, an error message is printed.
    If the product exists but has stock remaining, an error message is printed.
    Otherwise, the product is deleted from the warehouse.

    :param warehouse: dict[int, Product], all products
    :param parameters: str, all the text that the user entered after the
                       command word.
    """
    error_not_found = (
        f"Error: product '{parameters}' can not be deleted as it does not exist."
    )
    error_stock = (
        f"Error: product '{parameters}' can not be deleted as stock remains."
    )

    try:
        code = int(parameters)
    except ValueError:
        print(error_not_found)
        return

    if code not in warehouse:
        print(error_not_found)
    elif warehouse[code].get_stock() > 0:
        print(error_stock)
    else:
        del warehouse[code]


def handle_change(warehouse, parameters):
    """
    Handles the change command.
    <parameters> should contain a product code and a stock change amount.
    If the parameters are invalid, an error message is printed.
    If the product code does not exist, an error message is printed.
    Otherwise, the stock is modified by the given amount(negative or positive).

    :param warehouse: dict[int, Product], all products
    :param parameters: str, all the text that the user entered after the
                       command word.
    """
    error_message = f"Error: bad parameters '{parameters}' for change command."

    try:
        code, amount = parameters.split()
        code = int(code)
        amount = int(amount)
    except ValueError:
        print(error_message)
        return

    error_not_found = (
        f"Error: stock for '{code}' can not be changed as it does not exist."
    )

    if code not in warehouse:
        print(error_not_found)
    else:
        warehouse[code].modify_stock_size(amount)


def handle_low(warehouse):
    """
    Handles the low command. Prints all products whose stock is below the
     LOW_STOCK_LIMIT in ascending order of their codes.

    :param warehouse: dict[int, Product], all products
    """
    for product_code in sorted(warehouse):
        if warehouse[product_code].get_stock() < LOW_STOCK_LIMIT:
            print(warehouse[product_code])


def handle_combine(warehouse, parameters):
    """
    Handles the combine command. <parameters> should be two product codes.
    If either of the product codes does not exist, an error message is printed.
    If two codes are same, an error message is printed.
    If the two products have different categories or prices, an error
     message is printed.
    If the two products have the same category and price, the stock of the
     first product is increased by the stock of the second product and the
     second product is deleted from the warehouse.

    :param warehouse: dict[int, Product], all products
    :param parameters: str, all the text that the user entered after the
                          command word.
    """
    error_message = f"Error: bad parameters '{parameters}' for combine command."

    try:
        code1, code2 = parameters.split()
        code1 = int(code1)
        code2 = int(code2)
    except ValueError:
        print(error_message)
        return

    if code1 not in warehouse or code2 not in warehouse or code1 == code2:
        print(error_message)
        return

    product1 = warehouse[code1]
    product2 = warehouse[code2]

    if product1.get_category() != product2.get_category():
        print(f"Error: combining items of different categories "
              f"'{product1.get_category()}' and '{product2.get_category()}'.")
        return

    if product1.get_price() != product2.get_price():
        print(f"Error: combining items with different prices "
              f"{product1.get_price()}€ and {product2.get_price()}€.")
        return

    product1.modify_stock_size(product2.get_stock())
    del warehouse[code2]


def handle_sale(warehouse, parameters):
    """
    <parameters> should contain a category name and a sale percentage.
    If the percentage is invalid or outside the range 0-100,
    an error message is printed.

    If the input is valid, all products in the given category are assigned
    a new sale price based on their original price. Finally, the number of
    affected products is printed.

    :param warehouse: dict[int, Product], all products
    :param parameters: str, all the text that the user entered after the
                            command word.
    """
    error_message = f"Error: bad parameters '{parameters}' for sale command."

    try:
        category, sale_percentage = parameters.rsplit(maxsplit=1)
        sale_percentage = float(sale_percentage)
    except ValueError:
        print(error_message)
        return

    if sale_percentage < 0 or sale_percentage > 100:
        print(error_message)
        return

    count = 0
    for product in warehouse.values():
        if product.get_category() == category:
            discount = product.get_original_price() * sale_percentage / 100
            product.modify_price(-discount)
            count += 1

    print(f"Sale price set for {count} items.")


def main():
    """
    Reads the product database and starts the command loop.
    """
    filename = input("Enter database name: ")
    warehouse = read_database(filename)

    if warehouse is None:
        return

    while True:
        command_line = input("Enter command: ").strip()

        if command_line == "":
            return

        command, *parameters = command_line.split(maxsplit=1)
        command = command.lower()
        parameters = "" if len(parameters) == 0 else parameters[0]

        if "example".startswith(command) and parameters != "":
            example_function_for_example_purposes(warehouse, parameters)

        elif "print".startswith(command):
            handle_print(warehouse, parameters)

        elif "delete".startswith(command) and parameters != "":
            handle_delete(warehouse, parameters)

        elif "change".startswith(command) and parameters != "":
            handle_change(warehouse, parameters)

        elif "low".startswith(command) and parameters == "":
            handle_low(warehouse)

        elif "combine".startswith(command) and parameters != "":
            handle_combine(warehouse, parameters)

        elif "sale".startswith(command) and parameters != "":
            handle_sale(warehouse, parameters)

        else:
            print(f"Error: bad command line '{command_line}'.")

if __name__ == "__main__":
    main()
