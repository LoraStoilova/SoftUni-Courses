numbers = input().split()
all_numbers = []
for number in numbers:
    all_numbers.append(int(number))

is_even = lambda x: x % 2 == 0

result = list(filter(is_even, all_numbers))
print(result)
