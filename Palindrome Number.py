number = int(input("Enter a number: "))
original = number
reversed_number = 0
while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
if original == reversed_number:
    print(original,"is a palindrome number")
else:
    print(original,"is not a palindrome number")