import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Угадай число от 1 до 100: "))
    attempts += 1

    if guess < number:
        print("Загаданное число больше.")
    elif guess > number:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляю! Ты угадал число за {attempts} попыток.")
        break