"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 8.12 -- Calculating scores:
 Create a program that helps you add up the scores that various contestants
 have obtained in a game. The scores are stored in a text file that the program uses as input.

Learning Goals:
 I learn to process information that is stored in a file.
"""

def main():
    file_name=input("Enter the name of the score file: ")
    contestant_scores={}

    try:
        file=open(file_name,mode="r")
        for line in file:
            contestant, score=line.split(" ")
            if contestant not in contestant_scores:
                contestant_scores[contestant]=int(score)
            else:
                contestant_scores[contestant]+=int(score)
        file.close()
    except OSError:
        pass

    # Print the scores of the contestants in alphabetical order.
    print("Contestant score:")
    for contestant in sorted(contestant_scores):
        print(contestant, contestant_scores[contestant])


if __name__ == "__main__":
    main()