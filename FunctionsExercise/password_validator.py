def valid_password(some_password):
    is_valid = True
    if len(some_password) < 6 or len(some_password) > 10:
        print(f"Password must be between 6 and 10 characters")
        is_valid = False

    if not some_password.isalnum():
        print(f"Password must consist only of letters and digits")
        is_valid = False

    counter_digit = 0
    for digit in some_password:
        if digit.isdigit():
            counter_digit += 1
    if counter_digit < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid




password = input()
pass_is_valid = valid_password(password)
if pass_is_valid:
    print(f"Password is valid")