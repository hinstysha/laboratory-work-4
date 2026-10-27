"""Средняя сложность, задание 3: сумма чисел с помощью reduce."""

from functools import reduce
from typing import Iterable


def sum_numbers(numbers: Iterable[int]) -> int:
    """Суммирует целые числа через reduce; для пустого набора возвращает 0."""
    return reduce(lambda total, number: total + number, numbers, 0)


def main() -> None:
    """Демонстрирует суммирование обычного и пустого списков."""
    numbers = [1, 2, 3, 4, 5]
    print(f"Числа: {numbers}")
    print(f"Сумма: {sum_numbers(numbers)}")
    print(f"Сумма пустого списка: {sum_numbers([])}")


if __name__ == "__main__":
    main()
