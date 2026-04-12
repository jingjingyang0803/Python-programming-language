"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 5.5.3 - Rubik's Cube Solving Contests:
 Implement a program that asks for the times of the contestant's
 performances and prints the result to the hundredth of a second.
 The best and the worst time(only one if several best or worst times) are
  removed.

    Enter the time for performance 1: 5.80
    Enter the time for performance 2: 5.40
    Enter the time for performance 3: 5.17
    Enter the time for performance 4: 5.19
    Enter the time for performance 5: 5.22
    The official competition score is 5.27 seconds.

Learning Goals:
 Getting more practice in the use of the list.
"""


def main():
    score_list = []

    # Ask for the times of the contestant's performances and store them in
    # a list
    i=1
    while i<=5:
        time = float(input(f"Enter the time for performance {i}: "))
        score_list.append(time)
        i+=1
    # Remove the best and the worst time
    score_list.remove(max(score_list))
    score_list.remove(min(score_list))
    # Calculate the average of the remaining three times and print the
    # result to the hundredth of a second
    average = sum(score_list)/len(score_list)
    print(f"The official competition score is {average:.2f} seconds.")


if __name__ == "__main__":
    main()