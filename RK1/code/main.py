from processing.classes import conductor, orchestra, condOrch
from processing.connections import one_to_many, many_to_many
from processing.processing import task1, task2, task3

# Окрестры
orchestras = [
    orchestra(1, 'Российский национальный оркестр'),
    orchestra(2, 'Ансамбль песни и пляски'),
    orchestra(3, 'Большой симфонический оркестр'),
    orchestra(4, 'Русская филармония'),
    orchestra(5, 'Виртуозы Москвы'),
    orchestra(6, 'Местные ребята')
]

# Дирижеры
conductors = [
    conductor(1, 'Гончаренко', 15000, 1),
    conductor(2, 'Иванов', 38000, 2),
    conductor(3, 'Самонян', 12500, 4),
    conductor(4, 'Улепетов', 20000, 6),
    conductor(5, 'Бобер', 28500, 3),
    conductor(6, 'Мамонтов', 17500, 5),
    conductor(7, 'Галыгин', 6000, 6),
    conductor(8, 'Кенчур', 30000, 4),
    conductor(9, 'Сергеев', 10000, 2),
    conductor(10, 'Тополев', 18000, 1),
    conductor(11, 'Мамик', 37000, 5),
    conductor(12, 'Везучий', 22000, 3),
    conductor(13, 'Концов', 20500, 3)
]

# Для связи многие-ко-многим
condOrchs = [
    condOrch(1, 1),
    condOrch(2, 1),
    condOrch(3, 2),
    condOrch(4, 2),
    condOrch(5, 1),
    condOrch(6, 3),
    condOrch(7, 4),
    condOrch(8, 4),
    condOrch(9, 5),
    condOrch(10, 5),
    condOrch(11, 5),
    condOrch(12, 6),
    condOrch(13, 6),
    condOrch(7, 1),
    condOrch(8, 2),
    condOrch(2, 3),
    condOrch(3, 4),
    condOrch(4, 5),
    condOrch(5, 6)
]

# Установка связей
one_to_many = one_to_many(conductors, orchestras)
many_to_many = many_to_many(conductors, orchestras, condOrchs)


print(*one_to_many, sep='\n', end='\n\n')
print(*many_to_many, sep='\n', end='\n\n')


def main():
    print('Task 1', task1(one_to_many), sep='\n', end='\n\n')
    print('Task 2', task2(one_to_many), sep='\n', end='\n\n')
    print('Task 3', task3(many_to_many), sep='\n', end='\n\n')


if __name__ == '__main__':
    main()
