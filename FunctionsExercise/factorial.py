def sum_factorial(some_number):

    for factorial in range(1, some_number):
        some_number *= factorial
    return some_number


first_number = int(input())
second_number = int(input())
first_factorial = sum_factorial(first_number)
second_factorial = sum_factorial(second_number)
result = first_factorial / second_factorial
print(f"{result:.2f}")
