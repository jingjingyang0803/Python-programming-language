"""
COMP.CS.100 Programming 1: Introduction to Programming implementation for
2026 spring

Learning Goals:
Learning to create a somewhat more complicated if structure.

Let’s create a game of rock-paper-scissors for two players.
In this game, both players use one letter to tell whether they choose
rock (R), paper (P) or scissors (S). After this, the program shows the result.
The program does not need to consider incorrect entries, so there is no need to
 verify if the user entered something other than the letters "R"`, "P" or "S".
Player 1, enter your choice (R/P/S): P
Player 2, enter your choice (R/P/S): S
Player 2 won!

Creator: Jingjing Yang
Student id number: 154016843
"""
def main():
    player1 = input("Player 1, enter your choice (R/P/S): ")
    player2 = input("Player 2, enter your choice (R/P/S): ")

    if player1 == player2:
        print("It's a tie!")
    elif ((player1 == "R" and player2 == "S") or
          (player1 == "P" and player2 == "R") or
          (player1 == "S" and player2 == "P")):
        print("Player 1 won!")
    else:
        print("Player 2 won!")

if __name__ == "__main__":
    main()