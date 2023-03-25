# Гра "Вгадай число" - вгадайте число яке загадала програма

from random import randint

secret_num = randint(1, 10)  # Програма вибирає рандомне число від 1 до 10 включно
print(secret_num)

players_num = input("Please enter a number from 1 to 10 >>> ").strip()

if players_num.isalpha():  # Перевірка на літери
    print("You have entered a letter(s). Please enter a number from 1 to 10.")
elif players_num.isdigit():
    print(f"Your number is {players_num}.")  # Число користувача
    players_num_int = int(players_num)
    if players_num_int > 10 or players_num_int < 1:  # Перевірка на out of range
        print("You have entered a number that out of range. Please enter a number from 1 to 10.")
    elif 10 >= players_num_int >= 1 and players_num_int != secret_num:  # Перевірка що число від 1 до 10
        print(f"You were close, the secret number was {secret_num}. Please try again.")
    elif players_num_int == secret_num:  # Користувач вгадав число
        print(f"WIN-WIN! Congratulations! The secret number was {secret_num} as well.")
else:  # Якщо float або інше
    print("You have entered a FLOAT or negative number or special symbol(s). Please enter an INTEGER number from 1 to 10.")
