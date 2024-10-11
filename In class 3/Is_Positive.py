def is_positive(num):
    """
    This function checks if the given number is positive.
    
    A number is positive if it is greater than zero.
    """
    return num > 0

if __name__ == "__main__":
    # Get a number from the user
    user_input = float(input("Enter a number to check if it's positive: "))

    # Check if the number is positive and print the result
    if is_positive(user_input):
        print(f" True.")
    else:
        print(f" False.")
