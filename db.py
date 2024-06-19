import os, json
from pathlib import Path


def check_file(path: str='db.txt'):
    if os.path.isfile(path):
        return True
    return False


def create_file(path: str='db.txt'):
    Path(path).touch()


def set_data_to_file(data: dict, path: str='db.txt'):
    if check_file()==False:
        create_file()
    with open(path,'a') as f:
        f.write(json.dumps(data))

