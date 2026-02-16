import re


def evaluate_password(password: str) -> dict:
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Character variety checks
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Strength rating
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }


if __name__ == "__main__":
    user_input = input("Enter a password to evaluate: ")
    result = evaluate_password(user_input)

    print(f"\nStrength: {result['strength']}")
    print(f"Score: {result['score']}/6")

    if result["feedback"]:
        print("\nSuggestions:")
        for item in result["feedback"]:
            print(f"- {item}")
