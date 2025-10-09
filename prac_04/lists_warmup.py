# numbers = [3, 1, 4, 1, 5, 9, 2]
# Numbers [0] = 3
# Numbers [-1] = 2
# Numbers [3] = 1
# Numbers [1] = [3, 1, 4, 1, 5, 9]
# Numbers [3:4] = 1
# True
# False
# ValueError. Answer: False
# Numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers = ["ten", 1, 4, 1, 5, 9, 1]

print(numbers[1:])

if 9 in numbers:
    print("yes 9 is in an elements from numbers")
else:
    print("no 9 is not an element from numbers")
