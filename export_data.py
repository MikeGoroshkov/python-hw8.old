from import_data import *

def to_txt():
    with open('base.txt', 'w') as file:
        for key, value in all_classes.items():
            file.write(f'{key}\n')
            for id, data in value.items():
                file.write(f' {id}:{data[0]}:{data[1]}:{data[2]}:{data[3]}:{data[4]}:{data[5]}\n')