"""
COMP.CS.100 Programming 1: Introduction to Programming implementation for
2026 spring

Learning Goals:
Learning to use variables and calculate statement values.

Write a program that asks how much study benefits the user receives and
calculates how a 1,17 percent index raise affects the benefits.
The program prints the following:
Enter the amount of the study benefits: 335.32
If the index raise is 1.17 percent, the study benefit,
after a raise, would be 339.243244 euros
and if there was another index raise, the study
benefits would be as much as 343.2123899548 euros

Creator: Jingjing Yang
Student id number: 154016843
"""
benefits = float(input("Enter the amount of the study benefits: "))

index_raise = 1.17 / 100
benefits_after_raise = benefits * (1 + index_raise)
benefits_after_second_raise = benefits_after_raise * (1 + index_raise)

print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be " + str(benefits_after_raise) + " euros")
print("and if there was another index raise, the study")
print("benefits would be as much as " + str(benefits_after_second_raise) + " euros")