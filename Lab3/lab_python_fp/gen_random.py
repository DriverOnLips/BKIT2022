# DONE


from random import randrange


def gen_random(num_count, begin, end):
    return [randrange(begin, end + 1) for _ in range(num_count)]
