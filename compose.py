"""Повышенная сложность, задание 1: композиция функций."""

from typing import Callable


UnaryFunction = Callable[[int], int]


def compose(*functions: UnaryFunction) -> UnaryFunction:
    """Объединяет функции справа налево; без функций возвращает аргумент."""
    if not all(callable(function) for function in functions):
        raise TypeError("Все аргументы compose должны быть функциями.")

    def composed(value: int) -> int:
        """Применяет сохранённые функции в обратном порядке."""
        result = value
        for function in reversed(functions):
            result = function(result)
        return result

    return composed


def add_one(number: int) -> int:
    """Увеличивает число на единицу."""
    return number + 1


def square(number: int) -> int:
    """Возводит число в квадрат."""
    return number ** 2


def main() -> None:
    """Показывает зависимость результата от порядка композиции."""
    number = 3
    square_after_add = compose(square, add_one)
    add_after_square = compose(add_one, square)
    identity = compose()
    print(f"Исходное число: {number}")
    print(f"Сначала +1, затем квадрат: {square_after_add(number)}")
    print(f"Сначала квадрат, затем +1: {add_after_square(number)}")
    print(f"Композиция без функций: {identity(number)}")


if __name__ == "__main__":
    main()
