#задача 1

days_in_year = 365
weeks_in_year = 52
daily_income = 1500
weekly_expense = 850

total = daily_income * days_in_year
total_2 = weekly_expense * weeks_in_year

save_years = total - total_2

print(f"Накопления за год: {save_years} рублей")

#задача 2

number = 2
result = number ** 9
print(f"{number} в степени 9 = {result}")

#задача 3

apple = 20
print(apple)

#задача 4

house = 10  # Пример значения
house += 5
print(house)

#задача 5

integer_var = 42
string_var = "Привет!"
float_var = 1.5

print(f"Целое число: {integer_var}")
print(f"Строка: {string_var}")
print(f"Дробное число: {float_var}")

#задача 6

text = "12345678"
for char in text:
    print(char)

#задача 7

book_title = input("Введите название книги: ")
author_name = input("Введите имя автора: ")
publication_year = input("Введите год публикации: ")

print(f"Книга: {book_title}")
print(f"Автор: {author_name}")
print(f"Год публикации: {publication_year}")

#задача 8

length = 10
width = 5
summa = length * width
print(f"Площадь прямоугольника: {summa}")

#задача 9

kwadrat = 7  # Сторона квадрата
summa_kawadrata = kwadrat** 2
print(f"Площадь квадрата: {summa_kawadrata}")

#задача 10

price = 1000
skidka = 20

skidka_price = price * (1 - skidka / 100)
print(f"Цена со скидкой: {skidka_price} рублей")