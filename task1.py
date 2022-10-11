player = input('Введите ваше имя ')
bot = input('Введите имя бота ')
sum = 100
takes=[]
from random import *
random = randint(1, 2)
if random == 2:
    print(f'Игрок {player} ходит первым ')
    winner = player
else:
    print(f'Бот {bot} ходит первым ')
    winner = bot
print(winner)
count = randint(0,2)
while sum > 28:
        if count:
            a = int(input('Введите число от 1 до 28!!! '))
            if 1 <= a <= 28 and a not in takes:
                  print("Отлично, следующий ход")
                  takes.append(a)
                  count = False 
                  sum = sum - a
                  print(sum)
            else:
                print("Такое число уже было, либо оно не в пределах 1-28!!!Введите снова!!! ")
        else:
            winner == bot
            a = int(input('Введите число от 1 до 28!!!!!!!!! '))
            if 1 <= a <= 28 and a not in takes:
                print("Отлично, теперь Вы!")
                takes.append(a)
                count = True
                sum = sum - a
                print(sum)
            else:
                print("Такое число уже было, либо оно не в пределах 1-28!!!Введите снова!!! ")
                 
            

if count:
    print(f"{player} win!")
else:
    print(f"{bot} win!")