from db import set_data_to_file
def hello():
    print('Привет друг')
    print('/help')
    print('/registry')
    print('/login')


def start():
    set_data_to_file({'Kirill':123})
    

def registry():
    user_name = input('Введите логин:')
    password = input('Введите пароль:')



