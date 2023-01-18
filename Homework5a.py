# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# text1 = 'фбтуцк абв окцлджлжэ аб фабв ?ываб абв.ыва фабвуцк'
# text2 = 'абв'
# path = 'Lesson5add_Homework\TextInput.txt'
# with open (path, 'r', encoding='utf-8') as file:
#     text1 = file.readlines()[0]
# with open (path, 'r', encoding='utf-8') as file:    
#     text2 = file.readlines()[1]

# my_list = list(map(str, text1.split()))

# def findText(t1, t2):
#     if len(t1) >= len(t2):
#         count = 0
#         for i in range(len(t1)):
#             if t2 == t1[i:i+len(t2)]:
#                 count += 1
#     else:
#         count = 0
        
#     return count 

# for item in my_list:
#     if findText(item, text2) > 0:
#         my_list.remove(item)

# my_text = ''
# for item in my_list:
#     my_text += item + ' '

# with open ('Lesson5add_Homework\TextOutput.txt', 'w', encoding='utf-8') as file:
#     file.write(my_text)

# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?

# a) 2 игрока
# b) Подумайте как сделать бота с ""интеллектом""
# 2021 % 29 = 69 * 29 + 20
# Бота с интеллектом делать бесполезно, т.к. он в любом случае проиграет первому игроку со стратегией %29.
# По сути бот с возможностью первого хода со стратегией %29 и есть этот самый бот с интеллектом
# import random
# numSweets = 2021
# numSweetsForTime = 28

# secondMove = 0
# i = 1
# while numSweets > numSweetsForTime:
#     firstMove = numSweets % (numSweetsForTime + 1)
#     print(f'{i}-ый ход первого игрока - {firstMove} конфет')
#     secondMove = random.randint(1, 28)
#     print(f'{i}-ый ход второго игрока - {secondMove} конфет')
#     numSweets -= secondMove + firstMove
#     i += 1
# print(f'Последний ход первого игрокa - {numSweets} конфет')

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример: WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW => 9W3B24W1B14W

# path = 'Lesson5add_Homework\TextInput.txt'
# with open (path, 'r', encoding='utf-8') as file:
#     my_text = file.readlines()[2]

# new_text = ''
# i = 0
# while i < len(my_text):
#     simbol = my_text[i]
#     count = 0
#     for j in range(i + 1, len(my_text)):
#         if simbol == my_text[j]:
#             if my_text[j] == my_text[j - 1]:
#                 count += 1
#         else:
#             break
#     new_text += str(count + 1) + simbol
#     i = i + count + 1

# fig = 0
# for item in new_text:
#     if item.isdigit():
#         fig += 1

# my_text = ''
# i = 0
# while i < len(new_text):
#     if new_text[i].isdigit() and not new_text[i + 1].isdigit():
#         my_text += new_text[i + 1] * int(new_text[i])
#         i += 2
#     else:
#         flag = 2
#         for j in range(i + 2, i + fig):
#             if new_text[j].isdigit():
#                 flag += 1
#             else:
#                 flag1 = ''
#                 for k in range(i, i + flag):
#                     flag1 += new_text[k]
#                 my_text += new_text[i + flag] * int(flag1)
#                 break
#         i += flag + 1

# with open ('Lesson5add_Homework\TextOutput.txt', 'w', encoding='utf-8') as file:
#     file.write(new_text + '\n' + my_text)
    
