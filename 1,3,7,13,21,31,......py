number = int(input("Enter a number: "))
term = 1
difference = 2
print("Series: ", end = " ")
for i in range(number):
    print(term, end = " ")
    term += difference
    difference += 2