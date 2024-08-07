my_tuple = (1, 2, 3)
a, b, c = my_tuple

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

numbers = (1, 2, 3, 4, 5)
a, b, *rest = numbers

print(a)    # Output: 1
print(b)    # Output: 2
print(rest) # Output: [3, 4, 5]
