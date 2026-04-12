"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 2.6.3 - Fixing field width:
 The attached file includes a program that prints a simple cheat sheet for
 learning the multiplication table.
 Format the program's  printout so that each multiplication result is shown
 in a printout field, which is four characters wide.

Expected output:
     1   2   3   4   5   6   7   8   9  10
     2   4   6   8  10  12  14  16  18  20
     3   6   9  12  15  18  21  24  27  30
     4   8  12  16  20  24  28  32  36  40
     5  10  15  20  25  30  35  40  45  50
     6  12  18  24  30  36  42  48  54  60
     7  14  21  28  35  42  49  56  63  70
     8  16  24  32  40  48  56  64  72  80
    10  20  30  40  50  60  70  80  90 100

Learning Goals:
 To practice defining field width when formatting a printout.
"""

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            # Set the field width to 4 characters
            print(f"{i * j:4}", end="")
        print() # Move to the next line after printing each row

if __name__ == "__main__":
    main()
