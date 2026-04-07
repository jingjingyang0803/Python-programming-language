"""
COMP.CS.100 Programming 1: Introduction to Programming implementation for
2026 spring

Learning Goals:
Review if, elif, and else.

Create a program that asks the user how they feel on scale 1-10 and then
proposes a suitable emoticon to describe the mood.
Make program verify the numeric values - if something other than a numeric
value between 1 and 10 is entered, the program should print Bad input!
:'( value 1
:-( value less than 4
:-| value 4-7
:-) value over 7
:-D value 10

Creator: Jingjing Yang
Student id number: 154016843
"""
def main():
    feeling = input("How do you feel? (1-10) ")

    if not feeling.isdigit():
        print("Bad input!")
        return

    feeling = int(feeling)

    if feeling < 1 or feeling > 10:
        print("Bad input!")
    elif feeling == 1:
        print("A suitable smiley would be :'(")
    elif feeling < 4:
        print("A suitable smiley would be :-(")
    elif feeling <= 7:
        print("A suitable smiley would be :-|")
    elif feeling < 10:
        print("A suitable smiley would be :-)")
    else:
        print("A suitable smiley would be :-D")

if __name__ == "__main__":
    main()