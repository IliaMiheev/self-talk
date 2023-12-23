from os import name, system
import datetime
oneTime = datetime.datetime.now()

def clear_console():
    operating_system = name
    if operating_system == 'posix':
        _ = system('clear')
    elif operating_system == 'nt' or operating_system == 'dos':
        _ = system('cls')
    else:
        print("Очистка консоли не поддерживается на данной операционной системе.")

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
        word = " ".join(word.replace(" ", " ").split())
        word = capitalize_after_dot(word)
        if word and word[-1] not in ['.', '!', '?']:
            word = word[0].upper() + word[1:]
        
    return word

def printAllMess():
    clear_console()
    for index, mess in enumerate(listMess):
        if index % 2 == 0:
            print(f'\033[92m {mess}\033[0m')
        else:
            print(f'\033[93m {mess}\033[0m')

stop = False
listMess = []

clear_console()
print('Эта программа создана, чтобы вы могли побеседовать с самим собой')
print()

a = input('Продолжить? ')
clear_console()

while not stop:
    message = input(' Введите сообщение: ')

    if message.lower() in ['стоп', 'exit']:
        stop = True
        printAllMess()
        print()
    elif not message.strip():
        while not message.strip():
            printAllMess()
            message = input(' Введите сообщение: ')
    else:
        listMess.append(capitalize_after_space(message))
        printAllMess()
twoTime = datetime.datetime.now()
allSecond = round((twoTime - oneTime).total_seconds())
minutes = allSecond // 60
remaining_seconds = allSecond % 60

print(" Ты разговаривал:")
print("     Минут:", minutes)
print("     Секунд:", remaining_seconds)



