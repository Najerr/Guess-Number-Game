from random import randint


def get_random_number():
    number = randint(0,101)
    return number 
a = get_random_number()
# print(a)
def guess_number():
    player_number = int(input())
    
    if player_number < a:
        print("Ваше число меньше того, что загадано")
        guess_number()
    if player_number > a:
        print("Ваше число больше того, что загадано")
        guess_number()
    if player_number == a:
        print("Отличная интуиция! Вы угадали число:)")


guess_number()

