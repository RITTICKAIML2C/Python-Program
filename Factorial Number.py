number = int(input("Enter a number: "))
factorial = 1
if number < 0:
    print("Factorial cannot be negative.")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print("The factorial of {} is {}".format(number, factorial))