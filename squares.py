"""Средняя сложность, задание 1: квадраты чисел от 1 до 10 через map."""


def calculate_squares() -> list[int]:
    """Возвращает квадраты чисел от 1 до 10 с помощью map."""
    return list(map(lambda number: number ** 2, range(1, 11)))


def main() -> None:
    """Демонстрирует вычисление квадратов чисел от 1 до 10."""
    print("Числа:", list(range(1, 11)))
    print("Квадраты:", calculate_squares())


if __name__ == "__main__":
    main()
