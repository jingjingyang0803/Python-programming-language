"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 4.6.1 - Comparing floating-point (decimal) numbers:
 Implement the function compare_floats that uses two floating point numbers
  and an epsilon as a parameter and returns information on whether the
  numbers are same to a sufficient degree (the parameter epsilon) as a
  truth value.

Learning Goals:
 Learning to compare floating-point numbers sensibly and to implement a
 function for this purpose for future use.
"""
EPSILON = 0.000000001

def compare_floats(a, b, epsilon):
    """Compares two floating-point numbers a and b with a given epsilon.

    :param a: First floating-point number
    :param b: Second floating-point number
    :param epsilon: Epsilon, the threshold for considering a and b as equal
    :return: True if a and b difference is less than epsilon, False otherwise
    """
    return abs(a - b) < epsilon

def main():
    print(compare_floats(0.00000000000000000001, 0.0000000000000000002,
                          EPSILON))
    print(compare_floats(0.0002, 0.0000002,
                          EPSILON))

if __name__ == "__main__":
    main()