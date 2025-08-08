age = int(input("How old are you? "))
if age < 0:
    print("Invalid Age !!!")
if age >= 0 and age <= 12:
    print("You are a child !!!")
if age >= 13 and age <= 19:
    print("You are a Teen now !!!")
if age >= 20 and age <= 64:
    print("You are an Adult !!!")
if age >= 65 and age <= 100:
    print("You are a Senior !!!")