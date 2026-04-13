"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 9.5 -- Selecting a TV series:
 A program to search for series on the basis of a genre.

Learning Goals:
 The selection and combination of data structures.
"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    TODO: comment the parameter and the return value.
    """

    # TODO initialize a new data structure

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            # TODO add the name and genres data to the data structure

        file.close()
        return  # TODO return the data structure

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    # TODO print the genres

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        # TODO print the series belonging to a genre.


if __name__ == "__main__":
    main()
