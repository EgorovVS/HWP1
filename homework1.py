# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.7

# print("Введите число N")
# N = int(input())
# result = []
# for i in range(N):
#     result.append(3**i)
# for i in range(0,N-1,2):
#     result[i+1] = -(result[i+1])
# print(result)


# Для натурального n создать словарь индекс-значение, состоящий из элементов 
# # последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# def new_dictionary(number):
#     dictionary = {}
#     for i in range(number):
#         values = (3*(i+1)+1)
#         dictionary[f'{i+1}'] = f'{values}'
#     return dictionary

# print("Введите N ")
# N = int(input())
# dictionary = new_dictionary(N)
# print(dictionary)


# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# string_one = input("Введите первую строку ")
# string_two = input("Введите вторую строку ")
# count = string_one.count(string_two)
# if count > 0:
#     print(f"Вторая строка входит {count} раз в первую строку")
# else:
#     print("Вторая строка не входит в первую строку")

# Подсчитать сумму цифр в вещественном числе.
# def DigitToInt(digit):
#     digit = digit.replace(",",".")
#     digit = digit.replace(".","")
#     digit = int(digit) 
#     return digit 

# print("Введите вещественное число ")
# digit = input()
# digit = DigitToInt(digit)
# sum = 0
# while digit!=0:
#     sum = sum + digit%10
#     digit = digit//10
# print(sum)


# Написать программу получающую набор произведений чисел от 1 до N. 
# # Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

# print("Введите N ")
# N = int(input())
# power = 1
# result = []
# for i in range(1,N+1):
#    power*=i
#    result.append(power)
# print(result)


# Азбука Морзе

# char_to_dots = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#     'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#     'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#     'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#     '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#     '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#     '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#     ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#     '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
# }

# def in_morse(user_string):
#     user_string = user_string.upper()
#     user_string_morse = ""
#     for i in range(len(user_string)):
#         for key in char_to_dots.keys():
#             if(user_string[i]) == key:
#                 user_string_morse = user_string_morse+char_to_dots.get(key)+" "
#     return user_string_morse

# text = input("please, write something ")
# text = in_morse(text)
# print(text)


# Палиндром Не понятно -> Если при обратном чтении числа (124 - 421) 
# # не получается то же самое, то они складываются (124+421) и проверяются вновь. В таком случае все числа всегда будут 
# # палиндромами.

# def is_palindrom(digit):
#     sum = str(int(digit+digit[::-1]))
#     if(digit != digit[::-1]):
#             print("Ваше число - не палиндром")
#     else:
#             print("Ваше число - палиндром")


# number = input("Введите число ")
# is_palindrom(number)


# Игра Угадайка
# import random
# from random import randint

# print('Вас приветствует игра Угадайка. Попробуйте угадать случайное число от 1 до 100')
# number = randint(1,101)
# answer = int(input("Введите число от 1 до 100 "))
# count = 1
# while True:
#     if(answer == number):
#         print(f"Поздравляю, Вы отгадали число с {count} попыток ")
#         break
#     else:
#         count+=1
#         if(answer<number):
#             answer = int(input("Ваше число меньше, чем загаданное. Попробуйте снова "))
#         else:
#             answer = int(input("Ваше число больше, чем загаданное. Попробуйте снова "))


# Игра Угадайка 2


# import time
# import random
# from random import randint

# print('Вас приветствует игра Угадайка 2. ')
# print('Напишите число от 1 до 100. Компьютер попробует его отгадать ')
# answer = int(input())
# count = 1
# min = 1
# max = 101
# ibm_answer = randint(min,max)
# while True:
#     if(ibm_answer==answer):
#         print(ibm_answer)
#         print(f"Ваше число {ibm_answer} было отгадано с {count} попыток ")
#         break
#     else:
#         print(ibm_answer)
#         print()
#         count+=1
#         time.sleep(0.1)

#         if(ibm_answer<answer):
#             min = ibm_answer
#             ibm_answer = randint(min,max)
#         else: 
#             max = ibm_answer
#             ibm_answer = randint(min,max)

        
# Квест
import time
quest_dict = {
    '1': 'Человек улыбается и проходит мимо ', '2': 'Человек в недоумении останавливается и смотрит Вам вслед ', 
    '3': 'За поворотом Вы видите небольшой киоск с мороженым ', '4': 'За поворотом вы видите огромную лужу',
    '5': 'Вы видите небольшой киоск с мороженым '
}
def pause(time_in_sec):
    print()
    time.sleep(time_in_sec)

print()
print('Вам навстречу идет человек и говорит Вам "Доброе утро". Вы в ответ: ')
pause(1)
print("1 => отвечаете 'Доброе утро'")
print('2 => молчите и проходите мимо')
print()
answer = input()

while True:
        if(answer == '1'):
            print()
            print(quest_dict.get('1'))
            break
        if(answer == '2'):
            print()
            print(quest_dict.get('2'))
            break
        else:
            print(' выберите 1 или 2 ') 
            answer = input()
            pause(1)
            
if(answer == '1'):
    print('Вы идете по залитой солнцем улице и слушаете пение птиц')
    pause(1)
else: 
        print('Вы идете по серой от туч улице и дуетесь сами на себя')
pause(1)

print('И все же какой прекрасный летний день. Вы продолжаете свой путь и доходите до развилики. Как быть дальше: ')
print()
print('1 => Пойти налево ')
print('2 => Пойти направо ')
pause(1)
answer2 = input()
pause(1)
while True:
        if(answer2 == '1'):
            print()
            print(quest_dict.get('3'))
            break
        if(answer2 == '2'):
            print()
            print(quest_dict.get('4'))
            break
        else:
            print('выберите 1 или 2 ') 
            answer2 = input()
            pause(1)
if(answer2 == '1'):
    print('В Вашей голове мелькает мысль: "А почему бы и нет?" И вот Вы уже выбираете какое мороженое взять: ')
    print()
    print('1 => шоколадное ')
    print('2 => ванильное ')
    print('3 => клубничное ')
    print()
    answer3 = input()
    if(answer3=='1'):
        choise = 'шоколадное'
    if(answer3=='2'):
        choise = 'ванильное'
    if(answer3=='3'):
        choise = 'клубничное'
    pause(1)
else:
    if(answer == '2'):
        print('Вы думаете про себя: "Наверное хуже быть не может. И в ту же секунду из-за поворота с ревом появляется машина ')
        print('и мчится прямо в середину этой огромной лужи ')
        pause(1)
    
    else: 
        print('Вы думаете про себя: "Пожалуй пойду в другую сторону" ')
        print()
        print(quest_dict.get('5'))
        print()
        print('В Вашей голове мелькает мысль: "А почему бы и нет?" И вот Вы уже выбираете какое мороженое взять: ')
        print()
        print('1 => шоколадное ')
        print('2 => ванильное ')
        print('3 => клубничное ')
        print()
        answer3 = input()
        if(answer3=='1'):
            choise = 'шоколадное'
        if(answer3=='2'):
            choise = 'ванильное'
        if(answer3=='3'):
            choise = 'клубничное'
        pause(1)
if(answer == '2' and answer2 == '2'):
    print('Очевидно дальше продолжать нет смысла. Ну что за настрой!! Расслабьтесь и думайте о хорошем ')
    pause(1)
else:
    print(f'Лето, солнце, пение птиц и {choise} мороженое. Что может быть лучше этого? ')
    print('Закройте глаза, постарайтесь запомнить эту картинку, эти неподдельные эмоции')
    print('Вспомните эту маленькую историю, если вдруг Вам взгрустнется. Ребенок внутри Вас всегда найдет повод для улыбки ')
    pause(1)
