import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generate a secure random password.

    Args:
        length (int): Length of the password (default is 12).
        use_uppercase (bool): Include uppercase letters (default is True).
        use_digits (bool): Include digits (default is True).
        use_special (bool): Include special characters (default is True).

    Returns:
        str: The generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 for a secure password.")

    
    lowercase_pool = string.ascii_lowercase
    uppercase_pool = string.ascii_uppercase if use_uppercase else ""
    digit_pool = string.digits if use_digits else ""
    special_pool = string.punctuation if use_special else ""

    
    character_pool = lowercase_pool + uppercase_pool + digit_pool + special_pool
    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase_pool))
    if use_digits:
        password.append(random.choice(digit_pool))
    if use_special:
        password.append(random.choice(special_pool))
    password.append(random.choice(lowercase_pool))

    
    remaining_length = length - len(password)
    password.extend(random.choices(character_pool, k=remaining_length))

    
    random.shuffle(password)
    return ''.join(password)


if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    length = int(input("Enter the password length (minimum 4): "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_uppercase, use_digits, use_special)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
