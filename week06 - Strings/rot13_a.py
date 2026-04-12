"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 6.9 -- ROT-13 Encryption of One Line:
Implement a so-called ROT-13 encryption. In ROT-13 system, the characters
  are replaced with other characters in accordance with the following formula:

    unencrypted character:
    a b c d e f g h i j k l m n o p q r s t u v w x y z

    encrypted character:
    n o p q r s t u v w x y z a b c d e f g h i j k l m

Upper-case letters are changed to other upper-case letters using the same
 logic.

Learning Goals:
Getting acquainted with string structure, ie. how to handle the characters
  in a string using a for command and the [] operator.
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


def main():
    print(row_encryption("Happy, happy, joy, joy!"))
    # 'Unccl, unccl, wbl, wbl!'

if __name__ == "__main__":
    main()