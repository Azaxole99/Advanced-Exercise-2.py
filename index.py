# Question 1: Multi-Step Arithmetic Operations

import math
a = 5
b = 10
c = 7


a += 3
b *= 2
c %= 4


result = math.sqrt(a**2 + b**2 + c**2)
print("the value of a:", a)
print("the value of b:", b)
print("the value of c:", c)

print(f"the square of the sum of their squares: {result:.2f}")

# Question 2: Complex Conditional Evaluation

x = int(input("Enter an integer for x: "))
y = int(input("Enter an integer for y: "))
z = int(input("Enter an integer for z: "))
is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 <= z <= 50
final_condition = is_even and is_positive and is_in_range
print(final_condition)

# Question 3: Grading with Adjustments

score = float(input("Enter your base score (0-100): "))
score +=5
score -=10
score = max(0, min(score, 100))
if score >= 80:
    grade = 'A'
elif score >= 70:
    grade = 'B'
elif score >= 60:
    grade = 'C'
elif score >= 50:
    grade = 'D'
else:
    grade = 'F'

    print(f"final score: {score:.2f}")
    print(f"grade: {grade}")

# Question 4: Advanced Calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
try:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    elif operation == "**":
        result = num1 ** num2
    else:
        print("Invalid operation.")
        result = None
    if result is not None:
      print("Result:", result)
except ZeroDivisionError:
  print("Error: Cannot divide or calculate a remainder by zero.")
except overflowError:
  print("Error: The result is too large to handle.")