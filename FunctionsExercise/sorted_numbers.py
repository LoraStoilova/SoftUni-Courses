numbers = input().split()
all_numbers = []
for number in numbers:
    all_numbers.append(int(number))

result = list(sorted(all_numbers))
print(result)