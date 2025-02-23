input1 = input("Введите первую строку: ")
input2 = input("Введите вторую строку: ")
result = input1 + " " + input2
print("Результат:", result)

inputs = [input(f"Введите строку {i + 1}: ") for i in range(5)]
result = "".join(inputs)
print("Результат:", result)

user_input = input("Введите строку с пробелами: ")
trimmed_input = user_input.strip()
print("Результат:", trimmed_input)

user_input = input("Введите строку: ")
upper_case = user_input.upper()
print("Результат:", upper_case)

user_input = input("Введите строку: ")
lower_case = user_input.lower()
print("Результат:", lower_case)

text = "Этот текст будет выведен на новой строке.\n" * 4
print(text)

def dada(s):
    return s[0].upper() + s[1:]

user_input = input("Введите строку: ")
result = dada(user_input)
print("Результат:", result)

user_input = input("Введите строку: ")
reversed_input = user_input[::-1]
print("Результат:", reversed_input)

user_input = input("Введите строку: ")
multiplier = int(input("Сколько раз умножить строку? "))
result = user_input * multiplier
print("Результат:", result)

user_input = input("Введите строку: ")
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
count = sum(1 for char in user_input if char in vowels)
print("Количество гласных:", count)

user_input = input("Введите строку: ")
title_case = user_input.title()
print("Результат:", title_case)

double_quotes = "Это строка с двойными кавычками."
single_quotes = 'Это строка с одинарными кавычками.'
print(double_quotes)
print(single_quotes)

word = "колледж"
first_char = word[0]
print("Первый символ:", first_char)

word = "программирование"
first_four_chars = word[:4]
print("Первые 4 символа:", first_four_chars)