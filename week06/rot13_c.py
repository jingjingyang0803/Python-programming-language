"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 6.11 -- ROT-13 Encryption for a Whole Message:
Implement the final version of the ROT-13 program so that it first reads
  the encrypted message from the user as a whole (the message is ended by
  entering an empty row). After this, the message is printed as encrypted.

    Enter text rows to the message. Quit by entering an empty row.
    Puff, the magic dragon lived by the sea,
    And frolicked in the autumn mist, in a land called Honah Lee.

    ROT13:
    Chss, gur zntvp qentba yvirq ol gur frn,
    Naq sebyvpxrq va gur nhghza zvfg, va n ynaq pnyyrq Ubanu Yrr.

Learning Goals:
Learn to implement a new program by combining previously implemented
 functions.
"""
def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  a single character to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    # if the letter is in lower case, we can directly find the index of
    # the letter in regular_chars and get the corresponding encrypted
    # character.
    if text in regular_chars:
        index = regular_chars.index(text)
        return encrypted_chars[index]
    # if the letter is in upper case, we can first change it to lower
    # case and then find the index of the letter in regular_chars.
    # Finally, we can get the corresponding encrypted character and
    # change it to upper case.
    elif text.lower() in regular_chars:
        index = regular_chars.index(text.lower())
        return encrypted_chars[index].upper()
    # if the character is not a letter, we can directly add it to the
    # encrypted text.
    else:
        return text


def row_encryption(line):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param line: A string.

    :return: str, <line> parameter encrypted using ROT13
    """
    encrypted_line = ""
    for char in line:
        encrypted_line += encrypt(char)
    return encrypted_line


def read_message():
    """
    Reads the input entered by the user, saves the rows in a list,
     and returns the list.
    The entry of the input is terminated by entering an empty row.
    This empty row is not saved in list.

    :return: the list of the rows of the message.
    """
    msg = []
    while True:
        row = input()
        if row == "":
            break
        msg.append(row)
    return msg

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    # Print the message in ROT13 encryption.
    for row in msg:
        print(row_encryption(row))

if __name__ == "__main__":
    main()