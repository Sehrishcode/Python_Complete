for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
numbers = [5, 2, 5, 2, 2]
for i in numbers:
    output = ""
    for j in range(i):
        output += "x"
    print(output)