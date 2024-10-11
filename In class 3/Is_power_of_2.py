def is_power_of_two(num):
    """
    This function returns True if the given number is a power of 2.
    Otherwise, it returns False.
    """
    if num < 1:
        return False
    return (num & (num - 1)) == 0

if __name__ == "__main__":
    # Get a number from the user
    user_input = int(input("Enter a number to check if it's a power of 2: "))

    # Check if the number is a power of 2 and print the result
    if is_power_of_two(user_input):
        print(f"True")
    else:
        print(f"False")
