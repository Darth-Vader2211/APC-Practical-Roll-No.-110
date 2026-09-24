def total_marks(marks):
    return sum(marks)


def percentage(marks):
    return sum(marks) / len(marks)


def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 40:
        return "D"
    else:
        return "F"