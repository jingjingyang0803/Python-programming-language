"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 8.7 - Numbering the file rows doesn't succeed:


Learning Goals:
 I learn about the error handling related to processing files.
"""

def main():
    file_name = input("Enter the name of the file: ")
    try:
        file = open(file_name, mode="r")
        i = 1
        for line in file:
            print(i, line.rstrip())  # get rid of the newline character at
            # the end of the line with rstrip()
            i += 1

    except IOError:
        print("There was an error in reading the file.")


if __name__ == "__main__":
    main()