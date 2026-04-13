"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 9.7 -- Contacts:
 The function creates a dictionary for each of the CSV-file lines. The
  information can be accessed from this dict by the title of the CSV-file
  column. The function fill store these dicts in another dict where you
  can access them by the key presented in the first column of the line.
  You can assume that there is no duplicate keys in the file.

Learning Goals:
 I learn to use a dict to combine pieces of information that are related to
 each other.
"""
def read_file(filename):
    """
    Reads the contact file and creates a dictionary for each line.

    :param filename: The filename to read.
    :return: A dictionary for each line, where the key is the person's
             name and the value is another dictionary with the person's
             information including name, phone, email, skype name.
             Or None if the file cannot be read.
    """
    try :
        info=open(filename)
        contacts = {}
        for line in info:
            line = line.rstrip()
            parts = line.split(";")
            key = parts[0]

            if len(parts) == 5:
                contact_info = {"name": parts[1], "phone": parts[2], "email":
                    parts[3], "skype": parts[4]}
            # the example input file does not contain a skype name for all
            # the contacts
            else:
                contact_info = {"name": parts[1], "phone": parts[2], "email":
                    parts[3], "skype": ""}

            contacts[key] = contact_info
        return contacts
    except OSError:
        pass

def main():
    info=read_file("contacts.csv")
    print("")
    print(info["Mike"]["phone"])
    # '050 123546'
    print(info["Tom"]["email"])
    # 'tom@tuni.fi'
    print(info["Archie"]["name"])
    # 'Archie Architect'

if __name__ == "__main__":
    main()