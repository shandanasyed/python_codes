def add(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print("Start")
print(add(1, 2, 3, 4, 5))