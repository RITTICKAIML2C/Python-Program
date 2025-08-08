principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the time of interest: "))
time = float(input("Enter the time of interest: "))
amount = principal * (pow(1 + rate /100, time))
compound_interest = amount - principal
print("The required compound interest is: ", compound_interest)