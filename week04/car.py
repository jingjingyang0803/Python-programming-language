"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 4.14 - Car:
 In this task, you shall create a simple driving simulation where the user
  drives a car through a two-dimensional desert surface, using a textual
  interface. The program calculates where the car moves and how much gas it
  uses.


Learning Goals:
 Learning to implement functions that contain calculations.
"""

from math import sqrt


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    print_result(x, y, gas)

    while True:
        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, current_gas=gas)
            print_result(x, y, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas,
                                       gas_consumption)
            print_result(x, y, gas)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank_size,fill_gas, current_gas):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """

    if tank_size - current_gas >= fill_gas:
        return current_gas + fill_gas
    else:
        return tank_size


def drive(current_x, current_y, dest_x, dest_y, current_gas, consumption_per_km):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """

    # It might be usefull to make one or two assisting functions
    # to help the implementation of this function.

    km_to_drive=sqrt((dest_x-current_x)**2+(dest_y-current_y)**2)
    gas_needed=km_to_drive*consumption_per_km/100
    if gas_needed > current_gas:
        km_drivable=current_gas*100/consumption_per_km
        ratio=km_drivable/km_to_drive
        new_x, new_y=calculate_distance(current_x,current_y,dest_x,dest_y,
                                         ratio)
        return 0.0, new_x, new_y
    else:
        return current_gas-gas_needed, dest_x, dest_y


      # Implement your own functions here. You are required to
      # implement at least two functions that take at least
      # one parameter and return at least one value.  The
      # functions have to be used somewhere in the program.

def calculate_distance(x1, y1, x2, y2, ratio):
    """
    Calculate a point between two coordinates based on a given ratio.

    The function returns a point that divides the line segment between
    (x1, y1) and (x2, y2) according to the specified ratio.

    :param x1: x-coordinate of the first point
    :param y1: y-coordinate of the first point
    :param x2: x-coordinate of the second point
    :param y2: y-coordinate of the second point
    :param ratio: A float representing how far the point is from the first point
                  toward the second point.
                  (0 returns the first point, 1 returns the second point)
    :return: A tuple (x, y) representing the calculated point
    """
    new_x = x1 + (x2 - x1) * ratio
    new_y = y1 + (y2 - y1) * ratio
    return new_x, new_y

def print_result(x,y,gas):
    """This function prints out the current coordinates of the car and the amount of gas in the tank.

    :param x: x-coordinate of the car
    :param y: y-coordinate of the car
    :param gas: amount of gas in the tank
    """
    print("Coordinates x={:.1f}, y={:.1f}, the tank contains {:.1f} "
          "liters of gas.".format(x, y, gas))


def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
