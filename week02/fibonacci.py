"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 2.7 - Fibonacci series:
 Implement a program that prints the Fibonacci sequence for a number of
 times set by the user:

    How many Fibonacci numbers do you want? 7
    1. 1
    2. 1
    3. 2
    4. 3
    5. 5
    6. 8
    7. 13

Learning Goals:
 Reviewing the while structure again and getting acquainted with new roles
 of the variables.
"""

def main():
    n = int(input("How many Fibonacci numbers do you want? "))
    a, b = 1, 1 # first two numbers of the Fibonacci sequence

    i = 1
    while i <= n:
        print(f"{i}. {a}")
        a, b = b, a + b
        i += 1

if __name__ == "__main__":
    main()