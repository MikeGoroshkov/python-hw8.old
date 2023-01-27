from export_data import *
from import_data import *
from view import *

def user_choose():
    print('''Добро пожаловать в справочник школы! 
                Выберите действие:  
                1.Добавить
                2.Редактировать
                3.Удалить ученика из справочника
                4.Вывести в консоль справочник
                5.Экспорт базы в файл
                6.Выход''')
    choose = input("Введите цифру выбора: ")
    if choose == '1':
        print('''Выберите действие:
                1. Добавить ученика
                2. Добавить класс''')
        add_choose = input("Введите цифру выбора: ")
        if add_choose == '1':
            create_student()
        elif add_choose == '2':
            create_cl()
    elif choose == '2':
        print('''Выберите действие:
                1. Редактировать ученика''')
        edit_choose = input("Введите цифру выбора: ")
        if edit_choose == '1':
            edit_student()
        elif edit_choose == '2':
            change_class()
    elif choose == '3':
        delete_student()
    elif choose == '4':
        to_console()
    elif choose == '5':
        to_txt()
    elif choose == '6':
        return
    else:
        print("Вы ввели некорректное значение, повторите ввод!")
    user_choose()
