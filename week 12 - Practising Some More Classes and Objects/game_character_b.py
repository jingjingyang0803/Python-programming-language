"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 12.4 -- Game Character B:
 This program models a character adventuring in a video game.

Learning Goals:
 I will practise passing objects as a parameter to a method.
"""

class Character:
    """
    This class defines what a character is in the game and what
    he or she can do.
    """

    def __init__(self, name, hit_points):
        """Initializes the character with a name and hit_points.
        The inventory of the character is initialized as an empty dictionary.

        :param name: str, the name of the character.
        :param hit_points: int, the amount of hit points.
        """
        self.name = name
        self.hit_points = hit_points
        self.items = {}

    def get_name(self):
        """Returns the name of the character.
        """
        return self.name

    def has_item(self, test_item):
        """Returns True if the character has at least one of the
          test_item, False otherwise.
        """
        return test_item in self.items

    def how_many(self, test_item):
        """Returns the number of test_item the character has.
            If the character does not have any of the test_item, returns 0.
        """
        if self.has_item(test_item):
            return self.items[test_item]
        else:
            return 0

    def give_item(self, item):
        """Adds one of the item to the character's inventory.
        """
        if item not in self.items:
            self.items[item] = 1
        else:
            self.items[item] += 1

    def remove_item(self, item):
        """Removes one of the item from the character's inventory.
        If the character does not have any of the item, does nothing.
        """
        if self.has_item(item):
            self.items[item] -= 1
            # if the count of the item becomes 0, remove the item from the
            # inventory
            if self.items[item] == 0:
                self.items.pop(item)

    def printout(self):
        print(f"Name: {self.name}")
        print(f"Hitpoints: {self.hit_points}")
        # if there is no item, print message "  --nothing--"
        if self.items == {}:
            print("  --nothing--")
            return
        # print items in alphabetical order
        for item, count in sorted(self.items.items()):
            print(f"  {count} {item}")

    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """
        # Check if the item is in self's inventory. If not, return False.
        if item not in self.items:
            return False

        # Update the item inventory for both self and target.
        self.remove_item(item)
        target.give_item(item)
        return True


    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).

        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """
        if weapon not in WEAPONS:
            print(f"Attack fails: unknown weapon \"{weapon}\".")
            return False
        if target is self:
            print(f"Attack fails: {self.get_name()} can't attack "
                  f"him/herself.")
            return False
        if weapon not in self.items:
            print(f"Attack fails: {self.get_name()} doesn't have \""
                  f"{weapon}\".")
            return False

        print(f"{self.name} attacks {target.name} delivering {WEAPONS[weapon]}"
              f" damage.")
        target.hit_points -= WEAPONS[weapon]

        # Check if the target is defeated and print the message if so.
        if target.hit_points <= 0:
            print(f"{self.name} successfully defeats {target.name}.")
        return True


WEAPONS = {
    # Weapon          Damage
    #--------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)


    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()


    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword") # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword") # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
