def strip_vowels(s):
    vowels = "aAeEiIoOuU"
    result = ""
    for char in s:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    # Get user input
    user_input = input("Enter a string: ")
    result = strip_vowels(user_input)
    print(f"The string without vowels: {result}")
