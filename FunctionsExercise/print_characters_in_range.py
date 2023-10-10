def characters_in_range(first, second):
    all_characters = []
    for character in range(ord(first) + 1, ord(second)):
        current_character = chr(character)
        all_characters.append(current_character)

    return all_characters


first_character = input()
second_character = input()
result = characters_in_range(first_character, second_character)

print(" ".join(result))
