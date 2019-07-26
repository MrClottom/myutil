from os import path
from os import listdir
import json
from base64 import b64encode


def is_ext(file_name, ext, verbose=False):
    le_ext = get_ext(file_name)
    return le_ext == ext


def get_ext(file_name):
    return file_name[file_name.rfind('.')+1:] if '.' in file_name else None


def file_to_obj(file_path):
    with open(file_path, 'rb') as f:
        return {
            'name': path.split(file_path)[-1],
            'data': f.read()
        }


def dir_to_obj(dir_path, confirm_func=lambda path: True):
    def sub_dir(sub_path):
        whole_path = path.join(dir_path, sub_path)
        if path.isdir(whole_path):
            return dir_to_obj(whole_path)
        return file_to_obj(whole_path)

    return {
        'name': path.split(dir_path)[-1],
        'sub_dirs': [
            sub_dir(sub_path)
            for sub_path in listdir(dir_path)
            if confirm_func(path.join(dir_path, sub_path))
        ]
    }


def obj_to_json(obj, default=lambda s: b64encode(s).decode(), **kwargs):
    return json.dumps(
        obj, default=default, **kwargs
    )
