"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 4.10.1 - Triangle's angle:
 Implement the function calculate_angle, that will calculate (and return!)
  the magnitude of the third angle of the triangle, when the magnitudes of
  the other two angles are known (i.e. given as parameters to the
  function). The function must handle right-angled triangle as an exception.
 In case of a right-angled triangle you don't need to give the magnitude of
  the right-angle (90°) as a parameter at all: the function only needs the
  magnitude of one of the sharp angles as a parameter and will calculate
  the magnitude of the other sharp angle.

Learning Goals:
 Get to know default values of parameters and optional parameters.
"""
def calculate_angle(angle1, angle2=90):
    """ Calculate the magnitude of the third angle of the triangle.

    :param angle1: First angle of the triangle.
    :param angle2: Second angle of the triangle, default is 90.
    :return: Magnitude of the third angle of the triangle.
    """
    return 180 - angle1 - angle2

def main():
    print(calculate_angle(50,60))
    print(calculate_angle(30))

if __name__ == "__main__":
    main()