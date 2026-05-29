input = input("Input: ")

for char in input:
    print(char.strip("aeiouAEIOU"), end='')

print()
