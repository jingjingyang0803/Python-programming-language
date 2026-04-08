"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 2.8.1 - Bored? (improved version):
 Combine the previously implemented programs to create a program that asks
 the user if they're bored until they are, and additionally requires them to
 answer with the letter "y", "Y", "n" or "N", ie. asks the user for the answer
 repeatedly until receiving a valid input.

Examples:
    Bored? (y/n) o
    Incorrect entry.
    Bored? (y/n) z
    Incorrect entry.
    Bored? (y/n) m
    Incorrect entry.
    Bored? (y/n) n
    Bored? (y/n) n
    Bored? (y/n) n
    Bored? (y/n) f
    Incorrect entry.
    Bored? (y/n) j
    Incorrect entry.
    Bored? (y/n) y
    Well, let's stop this, then.

Learning Goals:
 Learning to implement a repeating structure where the user does not know
 the number of repetitions in advance (while). Nested loops.
"""

def main():
    answer = input("Bored? (y/n) ")
    while answer != "y" and answer != "Y":
        if answer != "n" or answer != "N":
            print("Incorrect entry.")
        # ask repeatedly until receiving y/Y
        answer = input("Bored? (y/n) ")
    print("Well, let's stop this, then.")

if __name__ == "__main__":
    main()