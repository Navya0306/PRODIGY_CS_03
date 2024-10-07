import re

def assess_password_strength(password):
    # Initialize criteria
    criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r'[A-Z]', password) is not None,
        "lowercase": re.search(r'[a-z]', password) is not None,
        "numbers": re.search(r'\d', password) is not None,
        "special_characters": re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None,
    }
    
    # Count how many criteria are met
    strength_score = sum(criteria.values())

    # Provide feedback based on the criteria met
    if strength_score < 3:
        strength = "Weak"
    elif strength_score == 3:
        strength = "Moderate"
    else:
        strength = "Strong"

    feedback = [
        "Password Strength Assessment:",
        f"- Length >= 8 characters: {'✔' if criteria['length'] else '✖'}",
        f"- Contains uppercase letters: {'✔' if criteria['uppercase'] else '✖'}",
        f"- Contains lowercase letters: {'✔' if criteria['lowercase'] else '✖'}",
        f"- Contains numbers: {'✔' if criteria['numbers'] else '✖'}",
        f"- Contains special characters: {'✔' if criteria['special_characters'] else '✖'}",
        f"Overall Strength: {strength}"
    ]

    return "\n".join(feedback)

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to assess its strength: ")
    print(assess_password_strength(password))