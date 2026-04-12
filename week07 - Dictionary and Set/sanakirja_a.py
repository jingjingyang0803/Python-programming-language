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
            if english_word in english_spanish:
                spanish_word=english_spanish[english_word]
                print(english_word, "in Spanish is", spanish_word)
            else:
                print("The word", english_word, "could not be found from "
                                                 "the dictionary.")

        elif command == "A":
            english_word=input("Give the word to be added in English: ")
            spanish_word=input("Give the word to be added in Spanish: ")
            if english_word not in english_spanish:
                english_spanish[english_word]=spanish_word
            else:
                print("The word", english_word, "already exists in the "
                                                 "dictionary.")

        elif command == "R":
            english_word=input("Give the word to be removed: ")
            if english_word in english_spanish:
                del english_spanish[english_word]
            else:
                print("The word", english_word, "could not be found from "
                                                 "the dictionary.")

        elif command == "P":
            for word in sorted(english_spanish):
                print(word, english_spanish[word])

        elif command == "T":
            text=input("Enter the text to be translated into Spanish: ")
            text.split(" ")
            translated_text=""
            for word in text.split(" "):
                if word in english_spanish:
                    translated_text+=english_spanish[word]+" "
                else:
                    translated_text+=word+" "
            print("The text, translated by the dictionary:")
            print(translated_text.strip())

        elif command == "Q":
            print("Adios!\n")

            print("If the word in the translated sentence is not in the "
                  "dictionary, the\nword in question should be printed to "
                  "the sentence in English.")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()