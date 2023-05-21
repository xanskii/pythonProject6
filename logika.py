from random import  randint
n = randint(1,3)
from decouple import config
money = 1000
while True:

    print (f'деньги : {money} ')
    person_money = int (input ('ставка :  '))
    money =  money - person_money
    if money < 0 :
       print ('у вас нету такое денег ')
       break

    print(f' остолась деньги : {money} ')
    print ( 'начинается игра ')

    r = int(input('число от 1 до 30\n'
                  'число :  '))
    if r == n :
        print (f'вы угадали чило \n'
               f'вы выиграли : {person_money * 2}')
        money = money +(person_money * 2)
    elif r < n :
        print (f'вы не угадили \n '
               f'вы прогирали  {person_money } ')
    elif r > n:
        print(f'вы не угадили \n '
              f'вы прогирали  {person_money} ')
    else :
        print ('ошибка')
        break
    if   money  == 0 :
        print ('у вас не остолось денег')
        break
    print('хотите ли вы сыграть еще :')
    command = input('1) да\n'
                    '0) нет\n')
    if command == '1' and 'да':
        print('continue')
    elif command == '0' and 'нет':
        print('stop')
        print (f' у вас остоалось{money}')
        break
    else:
        print('!!ОШИБКА!!')
        break
