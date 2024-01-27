# создание переменных, импорт библиотек
from os import name, system
import datetime
oneTime = datetime.datetime.now()
stop = False
listMess = []

# функция для очистки консоли
def clear_console():
    operating_system = name
    if operating_system == 'posix':
        _ = system('clear')
    elif operating_system == 'nt' or operating_system == 'dos':
        _ = system('cls')
    else:
        print("Очистка консоли не поддерживается на данной операционной системе.")

# две функции для редактирования текста
def capitalize_after_dot(string):
    words = string.split('. ')
    new_string = []
    for word in words:
        if word:
            new_word = word[0].upper() + word[1:]
            new_string.append(new_word)
    return '. '.join(new_string)

def capitalize_after_space(word):
    if word.strip():
        word = word.replace(".", ". ")
        word = word.replace(' .', '.')
        word = word.replace(' ,', ',')
        word = word.replace(' что ', ', что')
        word = word.replace(' то ', ', то')
        word = " ".join(word.replace(" ", " ").split())
        word = capitalize_after_dot(word)
        if word and word[-1] not in ['.', '!', '?']:
            word = word[0].upper() + word[1:]
    return word

# вывод приветствия
clear_console()
print('Эта программа создана, чтобы вы могли побеседовать с самим собой')
print()
a = input('Продолжить? ')
clear_console()

# вывод всех сообщений
def printAllMess():
    clear_console()
    for index, mess in enumerate(listMess):
        if index % 2 == 0:
            print(f'\033[92m {mess}\033[0m')
        else:
            print(f'\033[93m {mess}\033[0m')

# основной код
while not stop:
    message = input(' В: ')
    if message.lower() in ['стоп', 'exit']:
        stop = True
        printAllMess()
        print()
    elif not message.strip():
        while not message.strip():
            printAllMess()
            message = input(' В: ')
    else:
        listMess.append(capitalize_after_space(message))
        printAllMess()

# определяем время
twoTime = datetime.datetime.now()
allSecond = round((twoTime - oneTime).total_seconds())
minutes = allSecond // 60
remaining_seconds = allSecond % 60

# вывоим время разговора
print(" Время разговора:")
print("     Минут:", minutes)
print("     Секунд:", remaining_seconds)