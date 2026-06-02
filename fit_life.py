# Проект FitLife - MVP версия 2.0
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
user_weight = float(input("Какой у тебя вес?(например, 52)").replace(",", "."))
user_height = float(input("Какого ты рост?(например, 1.75)").replace(",", "."))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
bmi = round((user_weight / (user_height**2)), 1)  # расчёт индекса массы тела

# Подсчет воды: вес * 30 мл
WATER_PER_KG = 30
WATER_CONVERT_TO_LITERS = 1000
water_ml = user_weight * WATER_PER_KG
water_l = round((water_ml / WATER_CONVERT_TO_LITERS), 1)  # норма воды в литрах

# 4. Вывод красивого результата
print(f"Расчёт для {user_name}, {user_age} лет")
print(f"Индекс массы тела составляет: {bmi}")
print(f"Норма потребления воды: {water_l} л. в день")
print("Расчет окончен. Будьте здоровы!")
