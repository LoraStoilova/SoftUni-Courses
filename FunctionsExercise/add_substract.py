def sum_numbers(first, second):
    return first + second


def subtract(sum_first_second, third):
    return sum_first_second - third


def add_and_subtract(first_num, second_num, third_num):
    sum_result = sum_numbers(first_num, second_num)
    final_result = subtract(sum_result, third_num)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))


