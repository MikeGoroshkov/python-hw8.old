from import_data import *

def to_console():
    for cl, students in all_classes.items():
        print('Класс ', cl, ':')
        for id, data in students.items():
             print(f'    id {id}: {data[0]} {data[1]} {data[2]}, д.р. {data[3]}, {data[4]}')
