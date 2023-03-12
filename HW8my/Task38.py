# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def all_contacts():
    with open('phone_number.txt', 'r', encoding='utf8') as data:
        for line in data:
            print(line)


#all_contacts()

def find_contact(name):
    with open('phone_number.txt', 'r', encoding='utf8') as data:
        for line in data:
            if name in line:
                print(line)
                #break позволяет вывести первое попавшее значение


# find_contact('Иван')


def add_contact(new_contact):
    with open('phone_number.txt', 'a', encoding='utf8') as data:
        data.write('\n'+ new_contact)


def main_menu(numb):
    if numb == 1:
        all_contacts()
    elif numb == 2:
        name = input('Введите искомое имя: ')
        find_contact(name)
    elif numb == 3:
        data = input('Введите новый контакт: ')
        add_contact(data)

while True:
    numb = int(input('Введите 1 - для печати всего справочника;'
                     '2 - для поиска контакта; '
                     '3 - для записи новового контакта;'
                     '4 - выход из записной книжки'))
    if numb == 4:
        break
    main_menu(numb)










