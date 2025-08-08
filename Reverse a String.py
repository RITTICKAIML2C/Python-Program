def reverse_string(s):
    return s[::-1]  # slicing method to reverse

text = input("Enter a string: ")
reversed_text = reverse_string(text)
print("Reversed string:", reversed_text)
