# import

import random


# functions

def average(grades: list[float]) -> float:
    """Average of numbers in grades"""
    final_grade: float = sum(grades) / len(grades)
    print(final_grade)

def main() -> None:
    average([8, 9.5, 12, 10.5])


# if __name__ == '__main__'

if __name__ == '__main__':
    main()
