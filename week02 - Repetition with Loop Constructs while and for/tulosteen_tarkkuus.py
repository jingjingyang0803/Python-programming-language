"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 2.6.1 - Fixing precision:
 Format the program's printout so that in the first section, the approximate
 value of the pi is printed to the specificity of zero decimals (ie. as an
 integer) and, in the second section, to the specificity of four decimals.

Example output:
    The approximate value of pi is 3 or, if we want to get specific, 3.1416

Learning Goals:
 Practicing the definition of the number of shown decimals using a printout
 formatting function. Noting that the value and the printing specificity of
 a number are two different things.
"""

def main():
    PI = 3.14159265358979323846
    print(f"The approximate value of pi is {PI:.0f} or, ", end="")
    print(f"if we want to get specific, {PI:.4f}")

if __name__ == "__main__":
    main()
