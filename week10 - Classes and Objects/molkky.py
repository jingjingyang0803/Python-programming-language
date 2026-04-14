"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 10.10 -- Scoring for Mölkky:
 A program which scores a game of Mölkky when there are two players playing.


Example output:
    Enter the score of player Teppo of throw 1: 0

    Scoreboard after throw 1:
    Matti: 0 p, hit percentage 0.0
    Teppo: 0 p, hit percentage 0.0

    Enter the score of player Matti of throw 2: 24

    Scoreboard after throw 2:
    Matti: 24 p, hit percentage 100.0
    Teppo: 0 p, hit percentage 0.0

    Enter the score of player Teppo of throw 3: 35
    Cheers Teppo!

    Scoreboard after throw 3:
    Matti: 24 p, hit percentage 100.0
    Teppo: 35 p, hit percentage 50.0

    Enter the score of player Matti of throw 4: 24
    Matti needs only 2 points. It's better to avoid knocking down the pins with higher points.

    Scoreboard after throw 4:
    Matti: 48 p, hit percentage 100.0
    Teppo: 35 p, hit percentage 50.0

    Enter the score of player Teppo of throw 5: 0

    Scoreboard after throw 5:
    Matti: 48 p, hit percentage 100.0
    Teppo: 35 p, hit percentage 33.3

    Enter the score of player Matti of throw 6: 0
    Matti needs only 2 points. It's better to avoid knocking down the pins with higher points.

    Scoreboard after throw 6:
    Matti: 48 p, hit percentage 66.7
    Teppo: 35 p, hit percentage 33.3

    Enter the score of player Teppo of throw 7: 10
    Teppo needs only 5 points. It's better to avoid knocking down the pins with higher points.

    Scoreboard after throw 7:
    Matti: 48 p, hit percentage 66.7
    Teppo: 45 p, hit percentage 50.0

    Enter the score of player Matti of throw 8: 4
    Matti gets penalty points!

    Scoreboard after throw 8:
    Matti: 25 p, hit percentage 75.0
    Teppo: 45 p, hit percentage 50.0

    Enter the score of player Teppo of throw 9: 5
    Game over! The winner is Teppo!

Learning Goals:
 I will learn how to implement a class using Python.
"""
class Player:
    def __init__(self, name):
        self.__name = name
        # Initialize  the other attributes to their default values
        self.__throw_times = 0
        self.__hit_times = 0
        self.__points = 0
        self.__won = False

    def get_name(self):
        return self.__name

    def get_hit_percentage(self):
        if self.__throw_times == 0:
            return 0.0
        else:
            return self.__hit_times / self.__throw_times * 100.0

    def get_points(self):
        return self.__points

    def get_average_points(self):
        if self.__throw_times > 0:
            return self.__points / self.__throw_times
        else:
            return 0.0

    def has_won(self):
        return self.__won

    def add_points(self, points):
        penalty = False
        # Set the player's score to 25 if the total score would exceed 50.
        # Otherwise, add the scored points normally.
        if self.__points + points > 50:
            self.__points = 25
            penalty = True
        else:
            self.__points += points
        # Update relevant attributes with current points and throw information
        self.__throw_times += 1

        if points > 0:
            self.__hit_times += 1

        if self.__points == 50:
            self.__won = True

        return penalty


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        # Store the average points of the player in turn before
        # the throw, so that we can use them later for the printouts.
        average_before_throw = in_turn.get_average_points()

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        penalty = in_turn.add_points(pts)

        # Print a warning if the player has more than 50 points after the throw
        if penalty:
            print(in_turn.get_name() + " gets penalty points!")
        else:
            # Print a warning if the player has between 40 and 49 points after
            # the throw
            if 40 <= in_turn.get_points() <= 49:
                print(in_turn.get_name(),"needs only",50-in_turn.get_points(),
                      "points. It's better to avoid knocking down the pins with "
                      "higher points.")

            # Print a supporting message "Cheers NAME!" if this is not his
            # first throw and the points scored in this throw
            # exceed the player's average points per throw before this round.
            if throw > 2 and pts > average_before_throw:
                print("Cheers " + in_turn.get_name() + "!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, "
              f"hit percentage {player1.get_hit_percentage():.1f}")
        print(f"{player2.get_name()}: {player2.get_points()} p, "
              f"hit percentage {player2.get_hit_percentage():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
