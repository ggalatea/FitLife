# Проект FitLife - MVP версия 2.0
WATER_PER_KG = 30
WATER_CONVERT_TO_LITERS = 1000
ROUNDING_UP = 1

import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")

# 1. Знакомство
user_name = input("Привет! Как тебя зовут?").title()
while True:
    try:
        user_age = int(input("Сколько тебе лет?"))
        break  # Выход из цикла при успешном преобразовании
    except ValueError:
        print("Пожалуйста, введи возвраст, используя цифры")

# 2. Сбор данных
while True:
    try:
        user_weight = float(input("Какой у тебя вес?(например, 52)"))
        break  # Выход из цикла при успешном преобразовании
    except ValueError:
        print("Пожалуйста, введи вес, используя цифры")

while True:
    try:
        user_height = float(input("Какого ты рост?(например, 1.75)"))
        break  # Выход из цикла при успешном преобразовании
    except ValueError:
        print("Пожалуйста, введи рост, используя цифры")


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
bmi = round((user_weight / (user_height**2)), ROUNDING_UP)
water_ml = user_weight * WATER_PER_KG
water_l = round((water_ml / WATER_CONVERT_TO_LITERS), ROUNDING_UP)

# 4. Вывод красивого результата
print(f"Расчёт для {user_name}, {user_age} лет")
print(f"Индекс массы тела составляет: {bmi}")
print(f"Норма потребления воды: {water_l} л. в день")
print("Расчет окончен. Будьте здоровы!")
