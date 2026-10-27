"""Средняя сложность, задание 5: генератор чисел Фибоначчи."""

from itertools import islice
from typing import Iterator


def fibonacci() -> Iterator[int]:
    """Бесконечно генерирует числа Фибоначчи, начиная с 0 и 1."""
    previous, current = 0, 1
    while True:
        yield previous
        previous, current = current, previous + current


def main() -> None:
    """Выводит первые десять значений бесконечного генератора."""
    count = 10
    numbers = list(islice(fibonacci(), count))
    print(f"Первые {count} чисел Фибоначчи: {numbers}")


if __name__ == "__main__":
    main()
