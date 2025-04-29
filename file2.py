# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Example usage
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(check_even_odd(num))
