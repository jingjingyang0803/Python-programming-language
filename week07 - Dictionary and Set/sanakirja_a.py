"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 7.5 - A Tourist Dictionary:


Learning Goals:
 I review the basic operations of a dictionary (dict).
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            english_word=input("Enter the word to be translated: ")

            # Translate the word using the dictionary.
            # If the word is not found, print a message about it.
            if english_word in english_spanish:
                spanish_word=english_spanish[english_word]
                print(english_word, "in Spanish is", spanish_word)
            else:
                print("The word", english_word, "could not be found from "
                                                 "the dictionary.")

        elif command == "A":
            english_word=input("Give the word to be added in English: ")
            spanish_word=input("Give the word to be added in Spanish: ")

            # Add the word pair to the dictionary.
            # If the English word already exists,
            # its translation is updated to the new Spanish word.
            english_spanish[english_word]=spanish_word

        elif command == "R":
            english_word=input("Give the word to be removed: ")

            # Remove the word from the dictionary if it exists.
            # If the word is not found, print a message about it.
            if english_word in english_spanish:
                del english_spanish[english_word]
            else:
                print("The word", english_word, "could not be found from "
                                                 "the dictionary.")

        elif command == "P":
            # Print the words in the dictionary in alphabetical order.
            for word in sorted(english_spanish):
                print(word, english_spanish[word])

        elif command == "T":
            text=input("Enter the text to be translated into Spanish: ")
            translated_text=""

            # Translate the text word by word.
            # If a word is not found in the dictionary,
            # it is added to the translated text without translation.
            for word in text.split(" "):
                if word in english_spanish:
                    translated_text+=english_spanish[word]+" "
                else:
                    translated_text+=word+" "

            print("The text, translated by the dictionary:")
            print(translated_text.strip())

        elif command == "Q":
            print("Adios!")

            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()