def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score out of range")
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"