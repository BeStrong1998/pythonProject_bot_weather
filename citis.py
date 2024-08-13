def cities() -> list[str]:
    """
    Открываем файл и читаем содержимое.

    Получаем список всех городов хранящиеся в файле.

    Returns:
        list[str]: Возвращаем результат функции в виде списка городов
    """
    with open('txt-cities-russia.txt', 'r', encoding='utf-8') as file:
        return file.read().split()
# fgfgff
