from db import set_data_to_file, get_data_from_file


def hello():
    print('Привет друг')


def goodbye():
    print('Пока')
    exit()


data={}

    

def registry():
    global data
    dict_registry = {}
    while True:
        user_name = input('Введите логин:').strip().lower()
        if user_name in data:
            print('Такой пользователь уже зарегестрирован')
            continue
        dict_registry[user_name]={}

        dict_registry[user_name]['user_name'] = user_name
        break
    while True:   
        password = input('Введите пароль:').replace(' ','')
        if len(password)>=6:
            dict_registry[user_name]['password'] = password

            break
        else:
            print('Пароль должен быть больше 6 символов:')

    set_data_to_file({**dict_registry, **data})
    print('Регистрация прошла успешно')

    data=get_data_from_file()

commands={'/registry': ['Регистрация', registry], '/close': ['Выйти', goodbye]}  

def help():
    print('Комманды для рабботы с программой:')
    for i in commands:
        print(i,' - ', commands[i][0])

 

def start():
     global data
     data = get_data_from_file()
     print(data)
     print('Авторизоваться или регистрация\n')
     while True:
   
        command=input('-> ')
        if command in commands:
            commands[command][1]()
            

        if command == '/help':
            help()
    


