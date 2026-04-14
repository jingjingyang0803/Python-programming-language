"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 12.3 - Game Character A:


Learning Goals:
 I will practise using a data structure type as an attribute of an object.
"""

class Character:
    def __init__(self, name):
        self.name = name

        self.items = {}

    def get_name(self):
        return self.name

    def has_item(self, test_item):
        return test_item in self.items

    def how_many(self, test_item):
        return self.items[test_item]

    def give_item(self, item):
        if item not in self.items:
            self.items[item] = 1
        else:
            self.items[item] += 1

    def remove_item(self, item):
        if item not in self.items:
            print("Item not found.")
        elif self.items[item] == 0:
            print("Item can not be removed.")
        else:
            self.items[item] -= 1
            if self.items[item] == 0:
                self.items.pop(item)

    def printout(self):
        print(f"Name: {self.name}")
        for item, count in sorted(self.items.items()):
            print(count, item)

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
