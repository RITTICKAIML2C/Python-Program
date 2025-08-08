number = int(input("Enter number: "))

sum_squares = 0
for i in range(1, number + 1):
    sum_squares += i ** 2

print("Sum of squares of first", number, "natural numbers is:", sum_squares)
