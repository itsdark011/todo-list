from db import set_data_to_file, get_data_from_file
from datetime import datetime





def hello():
    print('Привет друг')


def goodbye():
    print('Пока')
    exit()

data = {}
current_user = ''


def registry():
    global data
    dict_registry = {}
    while True:
        user_name = input('Введите логин:').strip().lower()
        if user_name in data:
            print('Такой пользователь уже зарегестрирован')
            continue
        dict_registry[user_name] = {}

        dict_registry[user_name]['user_name'] = user_name
        break
    while True:
        password = input('Введите пароль:').replace(' ', '')
        if len(password) >= 6:
            dict_registry[user_name]['password'] = password
            break
        else:
            print('Пароль должен быть больше 6 символов:')

    dict_registry[user_name]['todo_list'] = {}

    set_data_to_file({**dict_registry, **data})
    print('Регистрация прошла успешно')

    data = get_data_from_file()


def auth():
    global data
    global current_user
    while True:
        user_name = input('Введите логин: ').strip().lower()
        password = input('Введите пароль: ').strip()
        if user_name == '/close':
            break

        if user_name in data:
            if data[user_name]['password'] == password:
                print('Вы успешно зашли')
                current_user = user_name
                break
            else:
                print('Ошибка: неверный пароль')
        else:
            print('Ошибка: неверный логин')


def add_new_do():
    global data
    global current_user

    if current_user == '':
        print('Пользователь не авторизован:')
        return
    
    while True:
        date = input('Введите дату на которое хотите указать дело:').replace(' ', '-')
        try:
            date_object = datetime.strptime(date, '%Y-%m-%d')
            break
        except ValueError:
            print('Неверный формат строки даты')

    while True:
        action = input('Введите заметку:').lower().strip()
        if action == '':
            continue
        break

    if date in data[current_user]['todo_list']:
        data[current_user]['todo_list'][date].append(action)
    else:
        data[current_user]['todo_list'][date] = [action]

    set_data_to_file(data)
    data = get_data_from_file()


commands = {'/registry': ['Регистрация', registry], '/auth': ['Войти в систему',auth], '/close': ['Выйти', goodbye], '/add_new': ['Дата работ', add_new_do]}


def help():
    print('Комманды для рабботы с программой:')
    for i in commands:
        print(i, ' - ', commands[i][0])


def start():
    global data
    data = get_data_from_file()
    print(data)
    help()
    while True:

        command = input('-> ')
        if command in commands:
            commands[command][1]()

        if command == '/help':
            help()
