"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 6.10 -- Saving a Message:
Implement the function read_message to the attached code template . The
  function reads the input entered by the user, saves the rows in a list,
  and returns the list. The entry of the input is terminated by entering
  an empty row. This empty row is not saved in list.
Also implement a main program that calls the function to read a message and
  then prints the strings in the list using ALL CAPITALS.

    Enter the text rows of the message. End by entering an empty row.
    Puff, the magic dragon lived by the sea,
    And frolicked in the autumn mist, in a land called Honah Lee.

    The same, shouting:
    PUFF, THE MAGIC DRAGON LIVED BY THE SEA,
    AND FROLICKED IN THE AUTUMN MIST, IN A LAND CALLED HONAH LEE.

Learning Goals:
 Learning to save strings in a list.
"""
def read_message():
    """
    Reads the input entered by the user, saves the rows in a list,
     and returns the list.
    The entry of the input is terminated by entering an empty row.
    This empty row is not saved in list.

    :return: the list of the rows of the message.
    """
    msg = []
    while True:
        row = input()
        if row == "":
            break
        msg.append(row)
    return msg

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    # Print the message in ALL CAPITALS.
    for row in msg:
        print(row.upper())


if __name__ == "__main__":
    main()