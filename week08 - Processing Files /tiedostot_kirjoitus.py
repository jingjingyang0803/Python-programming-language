"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 8.9 - Writing numbered lines to a file:
 Implement a program that reads an user message in the usual style, ending
  with an empty line, and then saves it to a file so that the file also
  contains line numbers.

Learning Goals:
 I learn the details related to writing files.
"""

def main():
    file_name=input("Enter the name of the file: ")

    try:
        write_file=open(file_name,mode="w")
        print("Enter rows of text. Quit by entering an empty row.")

        line_number = 1
        while True:
            line=input()

            if line=="":
                break

            # Write the line number and the line to the file.
            text_to_write=str(line_number)+" "+line
            print(text_to_write,file=write_file)
            line_number+=1

        print(f"File {file_name} has been written.")
        write_file.close()

    except IOError:
        print(f"Writing the file {file_name} was not successful.")

if __name__ == "__main__":
    main()