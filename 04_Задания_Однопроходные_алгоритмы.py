"""
Написать программу, которая читая символы из файла, распознает, преобразует
и выводит на экран объекты по определенному правилу. Объекты разделены
пробелами. Распознавание и преобразование делать по возможности через
регулярные выражения. Для упрощения под выводом числа прописью подразумевается
последовательный вывод всех цифр числа.
Вариант 17.
Последовательности натуральных чисел, расположенных в порядке не возрастания.
Для каждой такой последовательности минимальное число вывести прописью.
"""

import re

# Словарь, отображающий цифры (0-9) на их словесные представления
digits_map = {
    0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре",
    5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять"
}

def process_sequence(filename):
    # Обработка файла
    try:
        with open(filename, 'r') as file:
            sequence_str = file.read().strip()
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return
    
    # Регулярное выражение для нахождения натуральных чисел
    natural_number_pattern = r'^[1-9][0-9]*$'
    numbers = []

    # Разделение строки на символы и проверка на соответствие
    for char in sequence_str.split():
        if re.match(natural_number_pattern, char):
            numbers.append(int(char))
        else:
            print(f"Предупреждение: Не удалось преобразовать '{char}' в число. Пропускаем.")

    if not numbers:
        print("Последовательность пуста.")
        return

    # Инициализация текущей невозрастающей подпоследовательности
    current_sequence = [numbers[0]]
    # Инициализация минимального числа текущей подпоследовательности
    min_num = numbers[0]

    # Цикл по последовательности
    for i in range(1, len(numbers)):
        if numbers[i] <= current_sequence[-1]:
            current_sequence.append(numbers[i])
            min_num = min(min_num, numbers[i])
        else:
            output_min(min_num)
            current_sequence = [numbers[i]]
            min_num = numbers[i]

    output_min(min_num)


# Вывод числа прописью по цифрам
def output_min(number):
    try:
        if number < 0:  # Обработка отрицательных чисел
            print("Отрицательные числа не обрабатываются")
            return
        num_str = str(number)
        result = ""
        for digit in num_str:
            result += digits_map[int(digit)] + " "
        print(result.strip())
    except (KeyError, ValueError):
        print("Ошибка: Невозможно преобразовать число в текст.")

filename = "input.txt"
process_sequence(filename)
