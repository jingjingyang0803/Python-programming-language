"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 2.6.2 - Fixing the spaces:
 Create a program that asks the user's name and then greets them with the
 text in the example run below.

Example:
    Tell us your name: Teemu
    Hey Teemu, the printout formatting is going well!

Learning Goals:
 Practicing the definition of the value of a print command separator character.
"""

def main():
    name = input("Tell us your name: ")
    print("Hey " + name + ", the printout formatting is going well!")

if __name__ == "__main__":
    main()