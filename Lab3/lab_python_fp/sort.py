# DONE


def sort_array(list_):
    return sorted(list_, key=abs, reverse=True)


def sort_array_lambda(list_):
    return sorted(list_, key=lambda n: abs(n), reverse=True)
