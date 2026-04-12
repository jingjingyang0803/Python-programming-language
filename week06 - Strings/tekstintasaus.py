"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 6.14 -- Fully Justified Text:
Implement a program that formats text in a fully justified typesetting.
The user enters the number of characters that will be printed in one line.
The text justification algoritm will divide the text into segments that
  are shorter than this and then fill in the line to the desired character
  length by adding space characters inbetween the words. The space
  characters are placed so that in the beginning of the line each word
  spacings contain one space character more than in the end of the line.

The last line of the text won't be filled with extra spaces. It can be
  shorter than the other lines.

Learning Goals:
 I learn to use a datastructure that contains multiple strings.
"""


def read_input():
    """Reads the text from the user and returns the text as a string.
    The user can enter multiple lines of text and the input is terminated
     by an empty line.

    :return str: Text as a string
    """
    print("Enter text rows. Quit by entering an empty row.")
    text=""
    while True:
        line = input()
        if line == "":
            break
        text += " " + line  # Add a space before the line to separate it
                            # from the previous line
    return text


def justify_line(words, width):
    """Returns one justified line of the given width.

    :param words:
        A list of words to be placed on the line.
    :param width:
        The desired line width.

    :return:
        A justified line as a string.
    """
    # If there is only one word, we can't add spaces between words,
    # so we just return the word.
    if len(words) == 1:
        return words[0]

    total_word_length = 0
    for word in words:
        total_word_length += len(word)

    spaces_needed = width - total_word_length
    gaps = len(words) - 1

    # The basic number of spaces is the integer division of spaces_needed
    # by gaps, and the extra spaces are the remainder.
    basic_spaces = spaces_needed // gaps
    extra_spaces = spaces_needed % gaps

    line = ""

    for i in range(len(words) - 1):
        line += words[i]

        spaces = basic_spaces

        # The extra spaces are distributed starting from the leftmost gap until
        # they are all used up.
        if i < extra_spaces:
            spaces += 1

        line += " " * spaces

    line += words[-1]  # Add the last word without extra spaces after it

    return line


def print_text(text, width):
    """Prints the text justified to the given line width.

    :param text:
        The text to be printed.
    :param width:
        Number of characters per line.
    """
    words = text.split()  # Split the text into words based on whitespace
    i = 0

    while i < len(words):
        line_words = []
        line_length = 0

        while i < len(words):
            word = words[i]  # Get the current word

            # Calculate the new length of the line if we add the current word.
            # If the line is empty, the new length is just the length of
            # the word.
            # Otherwise, we need to add 1 for the space between the words.
            if len(line_words) == 0:
                new_length = len(word)
            else:
                new_length = line_length + 1 + len(word)

            # If the new length is within the desired width, we add the
            # word to the line.
            if new_length <= width:
                line_words.append(word)
                line_length = new_length
                i += 1
            # Otherwise, stop adding new words to the line
            else:
                break

        # If we have reached the end of the words, we print the last line
        # without justification.
        if i == len(words):
            print(" ".join(line_words))
        # Otherwise, we justify the line and print it.
        else:
            print(justify_line(line_words, width))


def main():
    text=read_input()

    width=int(input("Enter the number of characters per line: "))

    print_text(text, width)


if __name__ == "__main__":
    main()