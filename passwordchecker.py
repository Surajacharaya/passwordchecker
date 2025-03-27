import re

def check_password_complexity(password):
    # Define the complexity criteria
    min_length = 8
    has_uppercase = re.search(r'[A-Z]', password) is not None
    has_lowercase = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    is_long_enough = len(password) >= min_length

    # Check if all criteria are met
    if all([has_uppercase, has_lowercase, has_digit, has_special_char, is_long_enough]):
        return True
    else:
        return False

# Example usage
passwords_to_check = [
    "Password123!",
    "weakpass",
    "StrongPass1@",
    "12345678",
    "NoSpecialChar1",
    "Short1!"
]

for pwd in passwords_to_check:
    if check_password_complexity(pwd):
        print(f"'{pwd}' is a strong password.")
    else:
        print(f"'{pwd}' is NOT a strong password.")