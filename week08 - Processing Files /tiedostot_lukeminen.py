"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 8.6 - Numbering the file lines:
 Create a program that reads a file and prints its contents with each row
 starts with the row's number and a space.

Learning Goals:
 I learn the details related to processing files.
"""

def main():
    file_name=input("Enter the name of the file: ")
    try:
        file=open(file_name, mode="r")
        i=1
        for line in file:
            print(i,line.rstrip())  # get rid of the newline character at
                                    # the end of the line with rstrip()
            i+=1

    except IOError:
        print("The file does not exist")

if __name__ == "__main__":
    main()