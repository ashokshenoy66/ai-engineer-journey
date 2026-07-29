def calculate_bonus(salary: float, percentage: float = 10) -> float:
    """
    Calculates employee bonus.
    """
    return salary * percentage / 100

if __name__ == "__main__":
    print(calculate_bonus(50000))
    print(calculate_bonus(50000, 15))