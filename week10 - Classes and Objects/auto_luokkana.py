"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 10.8 -- Classified Car:


Learning Goals:
 Learning to implement a simple class as Python code. Learning the concepts
 of class, object and method.
"""

class Car:
    """
    Class Car: Implements a car that moves a certain distance and
    whose gas tank can be filled. The class defines what a car is:
    what information it contains and what operations can be
    carried out for it.
    """

    def __init__(self, tank_size, gas_consumption):
        """
        Constructor, initializes the newly created object.

        :param tank_size: float, the size of this car's tank.
        :param gas_consumption: float, how much gas this car consumes
                   when it drives a 100 kilometers
        """

        self.__tank_volume = tank_size
        self.__consumption = gas_consumption

        # Initialize the amount of gas in the car's tank and
        # the number of kilometers in the car's odometer.
        # Tank is empty and the odometer shows a zero when the car is created.
        self.__gas=0.0
        self.__odometer = 0.0

    def fill_gas(self,amount):
        if amount < 0:
            print("You cannot remove gas from the tank")
        elif amount < self.__tank_volume - self.__gas:
            self.__gas += amount
        else:
            self.__gas = self.__tank_volume

    def drive(self,distance):
        if distance < 0:
            print("You cannot travel a negative distance")
        else:
            gas_needed = distance * self.__consumption / 100
            # If the car does not have enough gas to drive the whole
            # distance, it drives as far as it can with the remaining gas
            # and then stops.
            if gas_needed > self.__gas:
                distance_driven = self.__gas * 100 / self.__consumption
                self.__odometer += distance_driven
                self.__gas = 0.0
            else:
                self.__odometer += distance
                self.__gas -= gas_needed


    def print_information(self):
        # Print how much gas the car's tank contains and what does the car's
        # odometer show in one decimal place.
        print(f"The tank contains {self.__gas:.1f} liters of gas and the "
              f"odometer "
              f"shows {self.__odometer:.1f} kilometers.")


def main():
    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")

    # Here we define the variable car which is an object initiated
    # from the class Car (its type is Car). This is the point where the
    # constructor of the class Car (i.e. the method that is named __init__)
    # is called automatically behind the scenes to give an initial
    # value for the Car object we are creating!

    car = Car(tank_size, gas_consumption)

    # In this program we only need one car object but it is possible
    # to create multiple objects from one class. For example we could
    # create more objects if we needed them:
    #
    #     lightning_mcqueen = Car(20, 30)
    #     canyonero = Car(200, 400)

    while True:
        car.print_information()

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up?")

            # call the fill-method for the car-object here (task b)
            car.fill_gas(to_fill)

        elif choice == "2":
            distance = read_number("How many kilometers to drive?")

            # call the drive-method for the car-object here (task c)
            car.drive(distance)

        elif choice == "3":
            print("Thank you and bye!")
            break


def read_number(prompt, error_message="Incorrect input!"):
    """
    **** DO NOT MODIFY THIS FUNCTION ****

    This function is used to read input (float) from the user.

    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print
        if the entered value is not a float.
    """

    while True:
        try:
            return float(input(prompt + " "))

        except ValueError:
            print(error_message)


if __name__ == "__main__":
    main()
