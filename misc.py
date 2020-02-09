def confirm(bit_arr, val):
    return int(''.join(str(b) for b in bit_arr), 2) == int(val[1:], 16)


def check_str_range(start, end):
    return lambda s: s.isnumeric() and start <= int(s) <= end


def ar(*args, **kwargs):
    return (args, kwargs)


def kw(**kwargs):
    return kwargs


def extract_val(val, *attrs):
    for attr in attrs:
        if hasattr(val, attr):
            return getattr(val, attr)
    return val


def tail_func(f):
    class ArgSaver:
        __slots__ = ['args', 'kwargs']

        def __init__(self):
            self.args = None
            self.kwargs = None

        def __call__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            return self

        def __iter__(self):
            yield self.args
            yield self.kwargs

    def inner(*args, **kwargs):
        res = ArgSaver()
        mounted_f = f(res)
        res = mounted_f(*args, **kwargs)
        while isinstance(res, ArgSaver):
            args, kwargs = res
            res = mounted_f(*args, **kwargs)
        return res
    return inner
