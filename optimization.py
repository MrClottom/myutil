import cProfile
import pstats
import io


def profile(fnc):
    """A decorator that uses cProfile to profile a function"""
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner


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


def tail_func(f):
    def inner(*args, **kwargs):
        res = ArgSaver()
        mounted_f = f(res)
        res = mounted_f(*args, **kwargs)
        while isinstance(res, ArgSaver):
            args, kwargs = res
            res = mounted_f(*args, **kwargs)
        return res
    return inner
