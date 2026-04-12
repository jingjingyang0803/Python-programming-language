"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 7.9 - Word Density Calculator:
 Implement a word density calculator that reads a piece of text from the
 user and then prints how many times each of the words appears in the text.
 The words in the list are printed in alphabetic order and all the letters
 are in lower-case.

    Enter rows of text for word counting. Empty row to quit.
    I'm on a high way to hell
    I'm on a high way to hell
    It's going really well
    Well it's only hell

    a : 2 times
    going : 1 times
    hell : 3 times
    high : 2 times
    i'm : 2 times
    it's : 2 times
    on : 2 times
    only : 1 times
    really : 1 times
    to : 2 times
    way : 2 times
    well : 2 times

Learning Goals:
 Also using dict for saving the amounts and to execute operations where
 information contained by dict is used for calculation.
"""

def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    word_count = {}

    while True:
        # Read a line of input from the user and convert it to lower-case.
        line = input().lower()

        # If the user enters an empty line, stop reading input.
        if line == "":
            break

        # Split the line into words and count the occurrences of each word.
        words = line.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Print the word counts in alphabetic order.
    for word in sorted(word_count):
        print(f"{word} : {word_count[word]} times")

if __name__ == "__main__":
    main()