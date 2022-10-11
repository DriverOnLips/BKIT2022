from time import sleep
from lab_python_fp.gen_random import gen_random
from lab_python_fp.sort import sort_array, sort_array_lambda
from lab_python_fp.field import field
from lab_python_fp.print_result import print_result
from lab_python_fp.unique import Unique
from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2
import json
import sys
from lab_python_fp.process_data import f1, f2, f3, f4


def main():
    """ gen_random + sort
    list_ = gen_random(5, -15, 15)
    print(*list_)
    list1 = sort_array(list_)
    list2 = sort_array_lambda(list_)
    print(*list1)
    print(*list2)"""

    """ field
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    field(goods, 'title', 'price')"""

    """ print_result
    @print_result
    def test_1():
        return 1

    @print_result
    def test_3():
        return {'a': 1, 'b': 2}

    test_1()
    print()
    test_3()"""


    """ unique 
    #data = [1, 1, 1, 1, 1, 2, 2, 2, 3, 2]
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(data)
    print(*Unique(data).filling(), sep=', ')
    """


    """ cm_timer 
    with cm_timer_1():
        sleep(5.5)"""

    #data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    path = "data_light.json"

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    with cm_timer_1():
        f4(f3(f2(f1(data))))


if __name__ == "__main__":
    main()
