"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 12.3 - Game Character A:


Learning Goals:
 I will practise using a data structure type as an attribute of an object.
"""

class Character:
    # TODO: the class implementation goes here.


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
