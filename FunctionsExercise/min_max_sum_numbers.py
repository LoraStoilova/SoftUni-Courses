def min_number(some_numbers):
    min_value = min(some_numbers)
    return min_value

def max_number(some_numbers):
    max_value = max(some_numbers)
    return max_value

def sum_numbers(some_numbers):
    sum_value = sum(some_numbers)
    return  sum_value

numbers = input().split()
all_numbers = []
for number in numbers:
    all_numbers.append(int(number))

min_num = min_number(all_numbers)
max_num = max_number(all_numbers)
sum_num = sum_numbers(all_numbers)

print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_num}")

