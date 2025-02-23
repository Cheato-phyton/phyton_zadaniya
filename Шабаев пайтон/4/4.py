# Эта программа выводит строку "Привет, мир!"
from curses import echo


print("Привет, мир!")


# Переменная для хранения имени
name = "Иван"

# Переменная для хранения возраста
age = 25

# Переменная для хранения города
city = "Москва"

print(f"Имя: {name}, Возраст: {age}, Город: {city}")


# Цикл for, который проходит по числам от 1 до 10
for i in range(1, 11):
    # Вывод текущего числа
    print(i)



# Попытка сложить число и строку, что вызовет ошибку TypeError
result = 10 + "20"



# Часть 1: Вывод приветствия
print("Привет! Это программа с несколькими задачами.")

# Часть 2: Вывод чисел от 1 до 5
for i in range(1, 6):
    print(i)

# Часть 3: Вывод квадратов чисел от 1 до 3
for i in range(1, 4):
    print(i ** 2)



# Программа берет первые 4 символа из строки "интерпретатор"
word = "интерпретатор"
first_four = word[:4]
print("Первые 4 символа:", first_four)



# Умножение строки "Привет" три раза
text = "Привет"
result = text * 3
print(result)



"""
Эта программа принимает строку от пользователя,
преобразует ее в нижний регистр
и выводит результат.
"""
user_input = input("Введите строку: ")
print(user_input.lower())



# Факториал числа 7 вычисляется как произведение всех чисел от 1 до 7
factorial = 1
for i in range(1, 8):
    factorial *= i
print("Факториал 7:", factorial)



# Шаг 1: Запрашиваем у пользователя число
number = int(input("Введите число: "))

# Шаг 2: Проверяем, является ли число четным
if number % 2 == 0:
    print("Число четное.")
else:
    print("Число нечетное.")

# Шаг 3: Выводим квадрат числа
print("Квадрат числа:", number ** 2)

# Шаг 4: Выводим числа от 1 до введенного числа
for i in range(1, number + 1):
    print(i, end=" ")


echo "# Pyhton_practick-zadaniya" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Cheato-phyton/Pyhton_practick-zadaniya.git
git push -u origin main