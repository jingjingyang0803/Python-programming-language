"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 3.6.1 - The song "Old MacDonald had a farm":
 Implement a function that makes the program print the words of the song as
 follows:

    Old MACDONALD had a farm
    E-I-E-I-O
    And on his farm he had a cow
    E-I-E-I-O
    With a moo moo here
    And a moo moo there
    Here a moo, there a moo
    Everywhere a moo moo
    Old MacDonald had a farm
    E-I-E-I-O

    ...

Learning Goals:
 Learning to create a function that uses parameters. Understanding the uses
 of the functions.
"""

def print_verse(animal_name, vocalization):
    """
    Prints one verse of the song "Old MacDonald Had a Farm".

    Parameters:
        animal_name (str): The name of the animal on the farm.
        vocalization (str): The sound that the animal makes.

    Returns:
        None
    """
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {animal_name}")
    print("E-I-E-I-O")
    print(f"With a {vocalization} {vocalization} here")
    print(f"And a {vocalization} {vocalization} there")
    print(f"Here a {vocalization}, there a {vocalization}")
    print(f"Everywhere a {vocalization} {vocalization}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
    print()

def main():
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
