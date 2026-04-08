"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 4.7 - Lottery Probabilities:
 Implement a program that asks the user for two input values:
    the amount of lottery balls (or numbers) and
    the drawn balls (or numbers).
 and then prints the probability of getting a jackpot with only one coupon.
 Additionally have the program print the following error messages:
    "The number of balls must be a positive number."
    "At most the total number of balls can be drawn."
 Note:
    The use of math library is not allowed.
    Probability is printed as a fractional notation.

Example outputs:
    Enter the total number of lottery balls: 39
    Enter the number of the drawn balls: 7
    The probability of guessing all 7 balls correctly is 1/15380937

    Enter the total number of lottery balls: -3
    Enter the number of the drawn balls: 4
    The number of balls must be a positive number.

    Enter the total number of lottery balls: 30
    Enter the number of the drawn balls: 31
    At most the total number of balls can be drawn.

Learning Goals:
 Teaching yourself to find parts of the program that can be turned into
 functions. Rehearsing the creation of functions.
"""
def calculate_probability(total_balls, drawn_balls):
    """Calculates the probability of guessing all drawn balls correctly.

    :param total_balls: int, the total number of lottery balls.
    :param drawn_balls: int, the number of drawn balls.
    :return: A string with the probability or an error message.
    """
    if total_balls <= 0:
        return "The number of balls must be a positive number."
    elif drawn_balls > total_balls:
        return "At most the total number of balls can be drawn."
    else:
        probability = 1
        for i in range(drawn_balls):
            probability *= (total_balls - i)/(i + 1)
        return (f"The probability of guessing all {drawn_balls} balls "
                 f"correctly is 1/{probability:.0f}")

def user_input():
    """Prompts the user for the total number of lottery balls and the
     number of drawn balls.

    :return: int, int, a tuple containing the total number of balls and the
    number
      of drawn balls.
    """
    total_balls = int(input("Enter the total number of lottery balls: "))
    drawn_balls = int(input("Enter the number of the drawn balls: "))
    return total_balls, drawn_balls

def main():
    total_balls, drawn_balls = user_input()
    result = calculate_probability(total_balls, drawn_balls)
    print(result)

if __name__ == "__main__":
    main()