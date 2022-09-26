from random import randrange

def gen_random_(num_count, begin, end):
    list_int = [randrange(begin, end) for _ in range(num_count)]
    print(*list_int)
    print()