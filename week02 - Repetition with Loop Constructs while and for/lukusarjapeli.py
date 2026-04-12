"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 2.4.1 - Number series game Zip Boing:
 In the game Zip Boing players sit in a ring and call numbers in turns. The
 first player says 1, the next one 2 and so forth. The game is called Zip
 Boing because every time the next number is divisible by 3 the player has
 to say "zip" and every time the number is divisible by 7 the player has to
 say "boing". Also, if the umber is divisible by both the numbers,
 the player should say "zip boing".

Example:
    How many numbers would you like to have? 10
    1
    2
    zip
    4
    5
    zip
    boing
    8
    zip
    10

Learning Goals:
 Learning to combine control and repetition structures.
"""

def main():
    total = int(input("How many numbers would you like to have? "))

    # Use a while loop to iterate through the numbers from 1 to the total
    # specified by the user.
    number = 1
    while number <= total:
        # Check if the number is divisible by 3 and 7, or just one of them,
        # and print the appropriate output.
        if number % 3 == 0 and number % 7 == 0:
            print("zip boing")
        elif number % 3 == 0:
            print("zip")
        elif number % 7 == 0:
            print("boing")
        else:
            print(number)
        # Increase the number by 1 for the next iteration.
        number += 1


if __name__ == "__main__":
    main()