import re

def check_password_strength(password):
    # Initialize strength score
    strength_score = 0

    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    digit_criteria = re.search(r'\d', password)
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Checking each criteria
    if length_criteria:
        strength_score += 1
    if uppercase_criteria:
        strength_score += 1
    if lowercase_criteria:
        strength_score += 1
    if digit_criteria:
        strength_score += 1
    if special_char_criteria:
        strength_score += 1

    # Determine strength level
    if strength_score == 5:
        return "Strong"
    elif 3 <= strength_score < 5:
        return "Moderate"
    else:
        return "Weak"

# Get user input
password = input("Enter a password: ")
strength = check_password_strength(password)

# Provide feedback
print(f"Password Strength: {strength}")
if strength != "Strong":
    print("Suggestions to improve password strength:")
    if len(password) < 8:
        print("- Make it at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        print("- Include at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        print("- Include at least one lowercase letter.")
    if not re.search(r'\d', password):
        print("- Include at least one digit.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("- Include at least one special character.")
