# DONE


from time import perf_counter
from contextlib import contextmanager


class cm_timer_1:

    def __init__(self):
        pass

    def __enter__(self):
        self.begin = perf_counter()

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print(perf_counter() - self.begin)


@contextmanager
def cm_timer_2():
    time_ = perf_counter()
    yield
    print(perf_counter() - time_)
