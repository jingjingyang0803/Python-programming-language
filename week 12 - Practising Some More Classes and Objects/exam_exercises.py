def calculate_price(hours, age):
    """
    Returns the ticket price based on time and passenger age.

    :param hours: int, hour of the day (0...23)
    :param age: int, passenger age (>= 0)

    :return: float, ticket price
    """
    if 6 <= hours <= 17:
        price = 2.7
    elif 18 <= hours <= 22:
        price = 3.5
    else:
        price = 4.0

    if age < 3:
        return 0.0
    elif age <= 15 or age >= 65:
        return price - 1
    else:
        return price


def count_unique_characters(string):
    """
    Counts how many characters occur exactly once in the string.

    Lower-case and upper-case letters are considered different.

    :param string: str, the string to examine
    :return: int, the number of unique characters
    """
    char_count = {}

    for char in string:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

    unique_count = 0
    for count in char_count.values():
        if count == 1:
            unique_count += 1

    return unique_count


def count_smaller(lst, integer):
    """
    Counts how many integers in the list are smaller than the given integer.

    :param lst: list, a list of integers
    :param integer: int, the comparison value

    :return: int, the number of smaller integers,
             or None if the list is empty
    """
    if not lst:
        return None

    count = 0
    for number in lst:
        if number < integer:
            count += 1

    return count


def main():
    print(calculate_price(21, 46))  # 3.5
    print(calculate_price(10, 6))   # 1.7
    print(calculate_price(19, 1))   # 0.0
    print("=" * 10)

    print(count_unique_characters("cat"))       # 3
    print(count_unique_characters("abba"))      # 0
    print(count_unique_characters("tuni"))      # 4
    print(count_unique_characters("Aarghhh!"))  # 5
    print(count_unique_characters("x"))         # 1
    print(count_unique_characters(""))          # 0
    print("=" * 10)

    print(count_smaller([1, 2, 3], 1))                       # 0
    print(count_smaller([1, 2, 3], 2))                       # 1
    print(count_smaller([1, 2, 3], 3))                       # 2
    print(count_smaller([1, 2, 3], 4))                       # 3
    print(count_smaller([11, 4, -90, -72, -44, 47], 20))     # 5
    print(count_smaller([42, 13], 100))                      # 2
    print(count_smaller([13], 42))                           # 1
    print(count_smaller([], 0))                              # None


if __name__ == "__main__":
    main()