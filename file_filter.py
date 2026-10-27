"""Повышенная сложность, задание 4: фильтрация файла через генератор."""

import argparse
from pathlib import Path
from typing import Iterator, Union


def filter_lines(
    file_path: Union[str, Path],
    keyword: str,
    case_sensitive: bool = False,
) -> Iterator[str]:
    """Построчно выдаёт строки UTF-8-файла с ключевым словом как подстрокой.

    По умолчанию регистр не учитывается. Переводы строк удаляются,
    остальные пробелы сохраняются. Проверки и открытие файла происходят
    при начале перебора генератора. Файл закрывается при завершении
    перебора или при явном закрытии генератора методом close().
    """
    if not isinstance(keyword, str):
        raise TypeError("Ключевое слово должно быть строкой.")
    if not keyword.strip():
        raise ValueError("Ключевое слово не должно быть пустым.")
    search_keyword = keyword if case_sensitive else keyword.casefold()
    with Path(file_path).open(encoding="utf-8") as source:
        for line in source:
            text = line.rstrip("\r\n")
            search_text = text if case_sensitive else text.casefold()
            if search_keyword in search_text:
                yield text


def main() -> None:
    """Читает параметры запуска и выводит подходящие строки файла."""
    parser = argparse.ArgumentParser(
        description="Отбор строк текстового файла по ключевому слову."
    )
    parser.add_argument(
        "file_path", nargs="?", type=Path,
        default=Path(__file__).with_name("sample_data.txt"),
        help=("путь к UTF-8-файлу; по умолчанию "
              "sample_data.txt рядом со скриптом"),
    )
    parser.add_argument(
        "keyword", nargs="?", default="Python",
        help="подстрока для поиска; по умолчанию Python",
    )
    parser.add_argument(
        "--case-sensitive", action="store_true", help="учитывать регистр"
    )
    arguments = parser.parse_args()
    found = False
    try:
        for line in filter_lines(
            arguments.file_path, arguments.keyword, arguments.case_sensitive
        ):
            print(line)
            found = True
    except (OSError, UnicodeError, ValueError, TypeError) as error:
        parser.error(str(error))
    if not found:
        print("Подходящие строки не найдены.")


if __name__ == "__main__":
    main()
