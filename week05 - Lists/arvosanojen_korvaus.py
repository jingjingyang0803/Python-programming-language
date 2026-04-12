"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 5.6.1 - Replacing Course Grades:
 Your job is to implement a function named convert_grades which helps the
  teachers to manage this difficult process of modifying the grades. This
  function should receive a list on integers between 0–5 as its parameter.
 Each of these numbers represent an unmodified grade for an individual
  student. Your function is to loop over the numbers in the parameter list
  and replace every grade greater than zero with the value 6, which is/was
  the number used to express grade "pass" in the student database.

Learning Goals:
 To understand, that if a function modifies the elements of a list it
  received as a parameter, the modifications also affect the actual
  parameter at the point where the function was called.
"""
def convert_grades(grade_list):
    """Modifies the list by replacing every grade greater than zero with
     the value 6.

    :param grade_list: a list of integers between 0 and 5(including) as a
    parameter.
    """
    for i in range(len(grade_list)):
        if grade_list[i] >= 1 or grade_list[i] >= 5:
            grade_list[i] = 6
        elif grade_list[i] == 0:
            grade_list[i] = 0


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()