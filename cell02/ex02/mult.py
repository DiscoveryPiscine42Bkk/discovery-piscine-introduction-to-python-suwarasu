number = int(input("Enter first number:\n"))
number2 = int(input("Enter second number:\n"))

result = number * number2

print(f"{number} x {number2} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")