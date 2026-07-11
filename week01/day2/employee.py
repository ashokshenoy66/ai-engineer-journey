def calculate_bonus(salary: float, percentage: float = 10) -> int:
    """
    Calculates employee bonus.
    """
    return salary * percentage / 100

print(calculate_bonus(50000))
print(calculate_bonus(50000, 15))