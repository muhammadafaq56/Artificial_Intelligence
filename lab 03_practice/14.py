import re  # Import regular expression module for pattern matching


def check_password(password):
    if (
        6 <= len(password) <= 16  # Check length requirement
        and re.search(r"[a-z]", password)  # Check for lowercase letters
        and re.search(r"[A-Z]", password)  # Check for uppercase letters
        and re.search(r"\d", password)  # Check for digits
        and re.search(r"[$#@]", password)
    ):  # Check for special characters
        return "Password is valid"
    else:
        return "Password is invalid"


# Main program execution
password = input("Enter password: ")  # Prompt user for password
print(check_password(password))  # Validate and display result
