"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 6.12 -- How Many abbas?:
Implement the function count_abbas, which returns the number of abbas (
 meaning the string "abba") that the parameter string contains.

Learning Goals:
 Learning to design an algorithm related to processing the strings.
"""
def count_abbas(string):
    """
    Returns the number of abbas (meaning the string "abba") that the
     parameter string contains.

    :param string: input string

    :return: number of abbas (meaning the string "abba") that the
             parameter string contains
    """
    count = 0
    for i in range(len(string) - 3):
        if string[i:i+4] == "abba":
            count += 1
    return count


def main():
    print(count_abbas("abbabbabba"))  # 3
    print(count_abbas("barbapapa"))  # 0
    print(count_abbas("a"))  # 0

if __name__ == "__main__":
    main()