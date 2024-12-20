char = input("Enter a single character: ")
if len(char) == 1:
    if char.isupper():
        print(f"'{char}' is an uppercase letter.")
    elif char.islower():
        print(f"'{char}' is a lowercase letter.")
    elif char.isdigit():
        print(f"'{char}' is a digit.")
    else:
        print(f"'{char}' is neither a letter nor a digit.")