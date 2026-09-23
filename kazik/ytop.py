import random
import os
BALANCE_FILE = 'balance.txt'

if os.path.exists(BALANCE_FILE):
    with open(BALANCE_FILE, "r") as f:
            balance = int(f.read())
else:
    balance = 500
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))
print("добро пожаловать в рулетку FRINGET")
print("у вас", balance, "$")
bid = int(input("сколько ставите? "))
winning_number = random.randint(0,36)
print(f"выпало число: {winning_number}")
if winning_number % 2 == 0:
    print("поздравляю число четное вы выиграли")
    balance += bid #прибавляем к балансу сумму ставки
else:
    print("увы число не четное вы проиграли")
    balance -= bid #отнимаем от баланса сумму ставки

print(f"ваш новый баланс: {balance} $")
with open(BALANCE_FILE, "w") as f:
    f.write(str(balance))