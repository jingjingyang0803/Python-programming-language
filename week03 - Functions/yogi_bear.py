"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 3.6.2 - The song "Yogi Bear":
 Implement a function called repeat_name, which repeats printing the bear's
 name as many times as the caller of the function wants to.

lyrics of the song:
    I know someone you don't know
    Yogi, Yogi
    I know someone you don't know
    Yogi, Yogi Bear
    Yogi, Yogi Bear
    Yogi, Yogi Bear
    I know someone you don't know
    Yogi, Yogi Bear

    Yogi has a best friend too
    Boo Boo, Boo Boo
    Yogi has a best friend too
    Boo Boo, Boo Boo Bear
    Boo Boo, Boo Boo Bear
    Boo Boo, Boo Boo Bear
    Yogi has a best friend too
    Boo Boo, Boo Boo Bear

    Yogi has a sweet girlfriend
    Cindy, Cindy
    Yogi has a sweet girlfriend
    Cindy, Cindy Bear
    Cindy, Cindy Bear
    Cindy, Cindy Bear
    Yogi has a sweet girlfriend
    Cindy, Cindy Bear

Learning Goals:
 Learning that the function can use other functions as an aid.
"""

def repeat_name(bear_name, repetition_number):
    """
    Prints the bear's name as many times as the caller of the function wants to.
    Parameters:
        bear_name (str): The name of the bear.
        repetition_number (int): The number of times that the bear is repeated.
    Returns:
        None
    """
    for i in range(repetition_number):
            print(f"{bear_name}, {bear_name} Bear")

def verse(verse_text, bear_name):
    """
    Prints one verse of the song "Yogi Bear".
    Parameters:
        verse_text (str): The text of the verse.
        bear_name (str): The name of the bear.
    Returns:
        None
    """
    print(verse_text)
    print(f"{bear_name}, {bear_name}")
    print(verse_text)
    repeat_name(bear_name, 3)
    print(verse_text)
    repeat_name(bear_name, 1)
    print()

def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
