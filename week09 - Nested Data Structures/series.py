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
    Reads and saves the data of a file in format name;genre1,genre2,...,genreN
     into a  dictionary where the genres are the keys and the series names
     are the values.

    :param filename: the name of the file to read

     :return: a dictionary with the genres as keys and the series names of
     as values
    """

    # initialize a new data structure
    genre_name = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            try:
                name, genres = row.rstrip().split(";")

                genres = genres.split(",")

                # add the show name to the list of shows for each genre
                for genre in genres:
                    if genre in genre_name:
                        genre_name[genre].append(name)
                    else:
                        genre_name[genre] = [name]

            except ValueError:
                print("Error: rows were not in the format name;genres.")
                return None

        file.close()
        return  genre_name  # return the data structure

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    # if the data could not be read, exit the program
    if genre_data is None:
        return

    # print the available genres in alphabetical order
    genre_list=[]
    for genre in sorted(genre_data.keys()):
        genre_list.append(genre)
    print("Available genres are:", ", ".join(genre_list))

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        # print the series belonging to a genre line by line in alphabetical
        # order only if the input genre has been found in the data
        if genre in genre_list:
            for name in sorted(genre_data[genre]):
                    print(name)


if __name__ == "__main__":
    main()
