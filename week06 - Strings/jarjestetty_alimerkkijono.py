"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 6.13 -- The Longest Substring in Order:
This program finds the longest substring in a given string
 in which the letters are in alphabetical order.

Learning Goals:
 Learning to design a somewhat more challenging algorithm for processing
 strings.
"""
def longest_substring_in_order(string):
    """
    Returns the longest substring of the given string in which the letters are
    in alphabetical order.

    Args:
        string: the string to find the longest substring in order from.

    Returns:
        string: the longest substring of the given string in which the
                letters are in alphabetical order.
    """
    longest = ""
    current = ""

    for i in range(len(string)):
        # If the current character is in alphabetical order with previous
        # add it to the current substring.
        if i == 0 or string[i] >= string[i - 1]:
            current += string[i]
        else:
            # If the current substring is longer than the longest substring
            # found so far, update the longest substring
            if len(current) > len(longest):
                longest = current
            # Start a new current substring with the current character
            current = string[i]

    # Return the longest substring in order found so far
    if len(current) > len(longest):
        longest = current
    return longest


def main():
    print(longest_substring_in_order("abcabcdefgabab"))  # 'abcdefg'
    print(longest_substring_in_order("acdkbarstyefgioprtyrtyx"))  # 'efgioprty'


if __name__ == "__main__":
    main()