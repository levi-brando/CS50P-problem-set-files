camel_case = input("camelCase: ")

print("snake_case: ", end='', sep='')

for char in camel_case:
    if char in camel_case.upper():
        lowercase = char.lower()
        print("_", end='')
        print(lowercase, end='')
    else:
        print(char, end='')

print()

