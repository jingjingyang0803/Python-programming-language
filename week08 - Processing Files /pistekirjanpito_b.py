"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 8.13 -- Errors of calculating scores:
 Add handling of the error situations to the program pistekirjanpito_a.py.

Learning Goals:
 I learn to handle the error situations when processing information that is
 stored in a file.
"""

def main():
    file_name=input("Enter the name of the score file: ")
    contestant_scores={}

    try:
        file=open(file_name,mode="r")
        # If the file can not be opened in the read mode
    except OSError:
        print("There was an error in reading the file.")
        return

    try:
        for line in file:
            parts = line.split()

            if len(parts) != 2:
                print("There was an erroneous line in the file:")
                print(line)
                return

            contestant, score = parts

            try:
                score = int(score)
            except ValueError:
                print("There was an erroneous score in the file:")
                print(score)
                return
    finally:
        file.close()


    # Print the scores of the contestants in alphabetical order.
    print("Contestant score:")
    for contestant in sorted(contestant_scores):
        print(contestant, contestant_scores[contestant])


if __name__ == "__main__":
    main()