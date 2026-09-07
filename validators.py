def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format")
    return True

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    return True