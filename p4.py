def get_positive_number():
    while True:
        try:
            number = int(input("Please enter a positive number: "))
            if number <= 0:
                raise ValueError("The number must be positive.")
            return number
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

# Example usage
positive_number = get_positive_number()
print(f"You entered a valid number: {positive_number}")
