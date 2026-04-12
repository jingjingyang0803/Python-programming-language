"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 2.2.1 Bored? (first version):
 Create a program that asks the user if they're bored, until they are.

Examples output:
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) y
Well, let's stop this, then.

Learning Goals:
Learning to implement a repeating structure where the number of times a
 repetition happens is not known in advance (while).
"""

def main():
    bored = input("Bored? (y/n) ")
    while bored != "y":
        bored = input("Bored? (y/n) ")
    print("Well, let's stop this, then.")

if __name__ == "__main__":
    main()