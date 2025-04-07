# Завдання 1

deposit = float(input("Введіть початкову суму вкладу: "))
rate = float(input("Введіть річну процентну ставку (%): "))
target = float(input("Введіть бажану кінцеву суму: "))

years = 0
while deposit < target:
    deposit += deposit * (rate / 100)
    years += 1
    print(f"Рік {years}: {deposit:.2f} грн")

print(f"Потрібно {years} років, щоб досягнути бажаної суми.")

# Завдання 2 

import random

number = random.randint(1, 100)
for attempt in range(1, 8):
    guess = int(input(f"Спроба {attempt}/7. Введіть число: "))
    if guess == number:
        print(f"Вітаю! Ви вгадали число за {attempt} спроб.")
        break
    elif guess < number:
        print("Загадане число більше.")
    else:
        print("Загадане число менше.")
else:
    print(f"На жаль, ви не вгадали. Число було {number}.")

# Завдання 3 

start = int(input("Введіть нижню межу: "))
end = int(input("Введіть верхню межу: "))

found = False
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=' ')
            found = True

if not found:
    print("Простих чисел не знайдено.")

# Завдання 4 

while True:
    try:
        n = int(input("Введіть невід'ємне ціле число: "))
        if n < 0:
            print("Число не може бути від'ємним.")
        else:
            break
    except ValueError:
        print("Це не ціле число.")

factorial = 1
process = ""
i = 1
while i <= n:
    factorial *= i
    process += str(i) + ("*" if i < n else "")
    i += 1

print(f"{n}! = {process} = {factorial}")

# Завдання 5 

start_population = 10
growth_rate = float(input("Введіть відсоток зростання за годину: "))
max_population = int(input("Введіть максимальну кількість бактерій: "))

population = start_population
hours = 0

while population < max_population:
    print(f"Година {hours}: {int(population)} бактерій")
    population += population * (growth_rate / 100)
    hours += 1

print(f"Година {hours}: {int(population)} бактерій (досягнута межа)")
print(f"Потрібно {hours} годин для досягнення межі.")
