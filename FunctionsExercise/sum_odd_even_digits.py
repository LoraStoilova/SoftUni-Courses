def sum_odd_even_number(some_number):
    sum_even = 0
    sum_odd = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    return sum_even, sum_odd


number = input()
sum_even_numbers, sum_odd_numbers = sum_odd_even_number(number)
print(f"Odd sum = {sum_odd_numbers}, Even sum = {sum_even_numbers}")