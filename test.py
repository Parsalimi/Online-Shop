numbers = [4, 2, 9, 1, 11, 12, 15, 0]

for round in range(0, len(numbers)-1):
    for index in range(0, len(numbers)-1):
        if numbers[index] > numbers[index+1]:
            numbers[index], numbers[index+1] = numbers[index+1], numbers[index]

print(numbers)
