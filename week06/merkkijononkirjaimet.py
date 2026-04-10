"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 6.4 - Vowels and Consonants:
A program that asks from a user an English word and tells how many vowels
  (a, e, i, o, u and y) and consonants the word contains.
Assume that the word is always written with the lower-case a–z letter of
  the English alphabet. Also, the user always enters at least one character
  as an input.

    Enter a word: sassafrass
    The word "sassafrass" contains 3 vowels and 7 consonants.

Learning Goals:
 Learning to go through the characters of a string using a repetition
  structure.
"""

def main():
    word = input("Enter a word: ")
    vowels = "aeiouy"
    vowels_count = 0
    for char in word:
        if char in vowels:
            vowels_count += 1

    consonants_count = len(word) - vowels_count
    print(f'The word "{word}" contains {vowels_count} vowels and'
           f' {consonants_count} consonants.')

if __name__ == "__main__":
    main()