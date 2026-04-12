"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 2.2.2 Bored? (checking for errors):
 The program you implemented in the previous section will not work properly
 when the user enters something other than "y", "Y", "n", or "N".
 Now, implement a whole new program, which only contains a repeating structure
 that asks the user's answer again if the answer is not "y", "Y", "n" or "N".

Examples of how the program operates:
    Answer Y or N: q
    Incorrect entry.
    Answer Y or N: w
    Incorrect entry.
    Answer Y or N: n
    You answered n

Learning Goals:
 Learning to implement a repeating structure where the user does not know the
 number of repetitions in advance (while).
"""

def main():
    while True:
        answer = input("Answer Y or N: ")
        if answer=="y" or answer=="Y" or answer=="n" or answer=="N":
            print(f"You answered " + answer)
            break
        else:
            print("Incorrect entry.")

if __name__ == "__main__":
    main()