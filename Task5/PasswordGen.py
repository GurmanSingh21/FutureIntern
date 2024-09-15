import random
import string


# Function to generate random password
def generate_password(length, use_upper, use_lower, use_digits, use_special):
    available_chars = ''

    # Adding character sets based on user input
    if use_upper:
        available_chars += string.ascii_uppercase
    if use_lower:
        available_chars += string.ascii_lowercase
    if use_digits:
        available_chars += string.digits
    if use_special:
        available_chars += string.punctuation

    # Ensure at least one type of character is selected
    if not available_chars:
        print("Error: You must select at least one character type.")
        return None

    # Generate the password
    password = ''.join(random.choice(available_chars) for _ in range(length))
    return password


# Function to get user input for password criteria
def get_password_criteria():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 1:
                print("Length should be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Ask user for character types to include
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    return length, use_upper, use_lower, use_digits, use_special


# Main function
def main():
    print("Welcome to the Random Password Generator!")
    length, use_upper, use_lower, use_digits, use_special = get_password_criteria()

    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    if password:
        print("\nGenerated Password:", password)


# Run the program
if __name__ == "__main__":
    main()
