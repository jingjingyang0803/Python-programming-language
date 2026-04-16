def calculate_price(hours, age):
    """
    The first parameter value is an integer from 0 to 23 and the second
     parameter value is a positive integer (≥ 0).

    :param hours: time
    :param age: passenger age

    :return: float,ticket price
    """
    time_price={"morning":2.7,"evening":3.5,"night":4.0}
    time=""
    if 6 <= hours <= 17:
        time="morning"
    elif 16 <= hours <= 22:
        time = "evening"
    elif 23 <= hours <= 5:
        time = "night"

    if age < 3:
        return 0.0
    elif age <=15 or age >=65:
        return time_price[time]-1
    else:
        return time_price[time]


def count_unique_characters(string):
    """
    Determines how many of the characters of a string occur in the string
    only once.
    Lower-case and upper-case letters are considered as different characters.

    :param: string
    :return: int, the count of unique characters.
    """
    char_count={}

    for char in string:
        if char not in char_count:
            char_count[char]=0
        char_count[char] += 1
    unique=0
    for char in char_count:
        if char_count[char]==1:
            unique+=1
    return unique


def count_smaller(lst, integer):
    if len(lst)==0:
        return None

    i=0
    count=0
    while i < len(lst):
        if lst[i] < integer:
            count+=1
        i+=1
    return count


def main():
    print(calculate_price(21, 46))  # 3.5
    print(calculate_price(10, 6))   # 1.7
    print(calculate_price(19, 1))   # 0.0
    print("="*10)

    print(count_unique_characters("cat"))       # 3
    print(count_unique_characters("abba"))      # 0
    print(count_unique_characters("tuni"))      # 4
    print(count_unique_characters("Aarghhh!"))  # 5
    print(count_unique_characters("x"))         # 1
    print(count_unique_characters(""))          # 0
    print("="*10)

    print(count_smaller([1, 2, 3], 1))                      # 0
    print(count_smaller([1, 2, 3], 2))                      # 1
    print(count_smaller([1, 2, 3], 3))                      # 2
    print(count_smaller([1, 2, 3], 4))                      # 3
    print(count_smaller([11, 4, -90, -72, -44, 47], 20))    # 5
    print(count_smaller([42, 13], 100))                     # 2
    print(count_smaller([13], 42))                          # 1
    print(count_smaller([], 0))                             # None


if __name__ == "__main__":
    main()