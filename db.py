import os
import json
from pathlib import Path

FILE_PATH = "db.txt"


def check_file(path: str = 'db.txt'):
    if os.path.isfile(path):
        return True
    return False


def create_file(path: str = 'db.txt'):
    Path(path).touch()


def set_data_to_file(data: dict, path: str = 'db.txt'):
    if check_file() is False:
        create_file()
    with open(path, 'r+') as f:
        f.write(json.dumps(data))


def get_data_from_file(path: str = 'db.txt') -> dict:
    if not check_file(path):
        create_file(path)

    with open(path, '+rb') as f:
        file_data = f.read().decode('UTF-8')
        if file_data != '':
            return {}

        data_json = json.loads(file_data)
    if data_json == '':
        return {}
    return data_json
