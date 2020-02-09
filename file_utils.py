from os import path, listdir, makedirs, remove, rmdir
import json
from base64 import b64encode, b64decode
from zlib import compress as zc, decompress as zd


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


def path_to_obj(target_path, confirm_func=lambda tp: (lambda sub_path: True)):
    if path.isdir(target_path):
        return {
            'name': path.split(target_path)[-1],
            'sub_dirs': [
                path_to_obj(path.join(target_path, sub_path),
                            confirm_func=confirm_func)
                for sub_path in filter(confirm_func(target_path),
                                       listdir(target_path))
            ]
        }
    elif path.isfile(target_path):
        return file_to_obj(target_path)
    else:
        raise FileNotFoundError('file/folder \'{}\' not found'
                                .format(target_path))


def obj_to_file(obj, target_path):
    if 'sub_dirs' in obj and 'name' in obj:
        dir_path = path.join(target_path, obj['name'])
        makedirs(dir_path)
        for sub_obj in obj['sub_dirs']:
            obj_to_file(sub_obj, dir_path)
    elif 'data' in obj and 'name' in obj:
        with open(path.join(target_path, obj['name']), 'wb') as f:
            f.write(obj['data'])
    else:
        raise ValueError('Invalid input obj must contain name and'
                         + ' (sub_dirs/data) field')


def obj_to_json(obj, default=lambda s: b64encode(s).decode(), **kwargs):
    return json.dumps(
        obj, default=default, **kwargs
    )


def rec_remove(fp):
    if path.isdir(fp):
        for sub_path in listdir(fp):
            rec_remove(path.join(fp, sub_path))
        rmdir(fp)
    else:
        remove(fp)


def compress_obj(data):
    data = obj_to_json(data, default=lambda s: b64encode(zc(s, 9)).decode())
    return zc(data.encode(), 9)


def rec_decompress(obj, return_orig=False):
    if isinstance(obj, dict):
        return {
            key: rec_decompress(value, key == 'name')
            for key, value in obj.items()
        }
    if isinstance(obj, list):
        return list(map(rec_decompress, obj))
    if isinstance(obj, str):
        if return_orig:
            return obj
        return zd(b64decode(obj.encode()))
    raise TypeError('unrecognized type: {}'.format(type(obj)))


def decompress_cobj(data):
    data = json.loads(zd(data).decode())
    return rec_decompress(data)
