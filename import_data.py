all_classes = {}
all_students = {}
id_student = 1

def load_base():
    global all_classes
    class_name = ''
    with open('base.txt', 'r') as file:
        for line in file:
            l = line
            if l[0] != ' ':
                class_name = l.replace('\n', '')
                all_classes[class_name] = {}
            else:
                l = l.split(':')
                all_classes[class_name][l[0].replace(' ', '')] = [l[1], l[2], l[3], l[4], l[5], l[6].replace('\n', '')]

def create_student():
    global id_student
    global all_classes
    global all_students
    surname = input("Введите фамилию ученика: ")
    name = input("Введите имя ученика: ")
    otch = input("Введите отчество ученика: ")
    birth = input("Введите дату рождения ученика: ")
    tel = input("Введите телефон ученика: ")
    adress = input("Введите адрес ученика: ")
    class_name = input("Введите номер класса ученика: ")
    if class_name not in all_classes:
        create_cl(class_name)
    st_data = [surname, name, otch, birth, tel, adress, class_name]
    for cl, students in all_classes.items():
        for id in students.keys():
            if str(id_student) == str(id):
                id_student += 1
    all_classes[class_name][id_student] = st_data

def create_cl(name_class=False):
    if not name_class:
        name_class = input("Введите номер класса: ")
    all_classes[name_class] = {}

def edit_student():
    id_student = input("Введите id ученика: ")
    surname = input("Введите фамилию ученика: ")
    name = input("Введите имя ученика: ")
    otch = input("Введите отчество ученика: ")
    birth = input("Введите дату рождения ученика: ")
    tel = input("Введите телефон ученика: ")
    adress = input("Введите адрес ученика: ")
    class_name = input("Введите класс ученика: ")
    for cl, students in all_classes.items():
        for id in students.keys():
            if str(id_student) == str(id):
                old_class = cl
                old_id = id
    del all_classes[old_class][old_id]
    new_st_data = [surname, name, otch, birth, tel, adress, class_name]
    all_classes[class_name][id_student] = new_st_data

def delete_student():
    global all_classes
    global all_students
    id_student = int(input("Введите id студента: "))
    for cl, students in all_classes.items():
        for id in students.keys():
            if str(id_student) == str(id):
                old_class = cl
                old_id = id
    del all_classes[old_class][old_id]
