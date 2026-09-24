def attendance_percentage(present, total):
    return (present / total) * 100


def eligible(percentage):
    if percentage >= 75:
        return True
    return False