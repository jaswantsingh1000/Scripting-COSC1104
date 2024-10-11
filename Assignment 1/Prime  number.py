def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def previous_prime(n):
    """Find the largest prime number less than n."""
    for num in range(n - 1, 1, -1):
        if is_prime(num):
            return num
    return None

def next_prime(n):
    """Find the smallest prime number greater than n."""
    num = n + 1
    while True:
        if is_prime(num):
            return num
        num += 1

def divisors(n):
    """Return a list of divisors of n."""
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

def main():
    while True:
        user_input = input("Please enter a positive whole number: ")
        if user_input.isdigit():
            number = int(user_input)
            if number > 0:
                break
            else:
                print("The number must be positive. Try again.")
        else:
            print("Invalid input. Please enter a positive whole number.")
    
    # Determine if the number is prime and provide the required information
    print(f"You entered: {number}")
    
    prev_prime = previous_prime(number)
    if prev_prime is not None:
        print(f"The prime number before {number} is: {prev_prime}")
    
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
        print(f"The divisors of {number} are: {divisors(number)}")
    
    next_prime_num = next_prime(number)
    print(f"The next prime number after {number} is: {next_prime_num}")

if __name__ == "__main__":
    main()
