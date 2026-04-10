"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 5.7 - Bus Time Table:
 Design and implement a program which asks the user what time it is and
  prints the times(from 6:30    10:15   14:15   16:20   17:20   20:00) for
  the next three buses, based of the entered time.

    Enter the time (as an integer): 1000
    The next buses leave:
    1015
    1415
    1620

Learning Goals:
 Practicing the implementation of a slightly more complicated list program
  and once again reviewing the operations of the remainder operator.
"""

def main():
    bustime_list = [630,1015,1415,1620,1720,2000]

    current_time=int(input("Enter the time (as an integer): "))

    # Find the index of the next bus,
    # default is 0, if the current time is later than the last bus, the next
    #  bus is the first one on the next day.
    next_bus_index=0
    for i in range(len(bustime_list)):
        # If the current time is earlier than or equal to the bus time,
        #  the next bus
        if current_time <= bustime_list[i]:
            next_bus_index=i
            break

    # Print the next three buses, if the index exceeds the list length,
    # use the remainder operator to get the correct index.
    print("The next buses leave:")
    for j in range(next_bus_index,next_bus_index+3):
        print(bustime_list[j%len(bustime_list)])


if __name__ == "__main__":
    main()