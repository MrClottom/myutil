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
