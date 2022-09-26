import sys
import math
from math import sqrt

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
        coef = float(coef_str)
        cmd = True
    except:
        # Вводим с клавиатуры
        cmd = False
        print(prompt)
    if not cmd:
        flag = True
        while flag:
            try:
                coef = float(input())
                flag = False
            except:
                print('Повторите ввод коэффициента')

    # Переводим строку в действительное число
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(-(root ** 0.5))
        result.append((root ** 0.5))
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 > 0:
            result.append(-(root1 ** 0.5))
            result.append((root1 ** 0.5))
        if root2 > 0:
            result.append(-(root2 ** 0.5))
            result.append((root2 ** 0.5))
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    else:
        print(f'Количество корней: {len_roots}')
        print('Корни:', *roots)


    '''elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Один корень: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 4:
        print('Два корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))'''


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4