# TODO

from time import sleep
from lab_python_fp.gen_random import gen_random
from lab_python_fp.sort import sort_array, sort_array_lambda
from lab_python_fp.field import field
from lab_python_fp.print_result import print_result
from lab_python_fp.unique import Unique
from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2
from lab_python_fp.print_result import print_result
# Сделаем другие необходимые импорты

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк


# Функция f1 должна вывести отсортированный список профессий без повторений (строки в разном
# регистре считать равными). Сортировка должна игнорировать регистр.
@print_result
def f1(data):
    return Unique(field(data, "job-name")).filling()


# Функция f2 должна фильтровать входной массив и возвращать только те элементы, которые
# начинаются со слова “программист”. Для фильтрации используйте функцию filter.
@print_result
def f2(data):
    return list(filter(lambda param: param.startswith("программист"), data))



# Функция f3 должна модифицировать каждый элемент массива, добавив строку “с опытом Python”
# (все программисты должны быть знакомы с Python). Пример: Программист C# с опытом Python.
# Для модификации используйте функцию map
@print_result
def f3(data):
    return list(map(lambda add: add + " с опытом Python", data))


# Функция f4 должна сгенерировать для каждой специальности зарплату от 100 000 до 200 000 рублей
# и присоединить её к названию специальности. Пример: Программист C# с опытом Python, зарплата 137287 руб.
# Используйте zip для обработки пары специальность — зарплата.
@print_result
def f4(data):
    res = list(zip(data, gen_random(len(data), 100000, 200000)))
    return [i[0] + ", зарплата " + str(i[-1]) + " руб." for i in res]
