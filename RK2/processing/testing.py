import unittest
from classes import conductor, orchestra, condOrch
from connections import one_to_many, many_to_many
from processing import task1, task2, task3


class RK_test(unittest.TestCase):
    def setUp(self):
        orchestras = [
            orchestra(1, 'Российский национальный оркестр'),
            orchestra(2, 'Ансамбль песни и пляски'),
            orchestra(3, 'Местные ребята')
        ]
        conductors = [
            conductor(1, 'Гончаренко', 15000, 1),
            conductor(2, 'Иванов', 38000, 2),
            conductor(3, 'Самонян', 12500, 3),
            conductor(4, 'Улепетов', 20000, 1),
            conductor(5, 'Бобер', 28500, 3)
        ]
        condOrchs = [
            condOrch(1, 1),
            condOrch(2, 1),
            condOrch(3, 2),
            condOrch(4, 2),
            condOrch(5, 1),
            condOrch(1, 2),
            condOrch(3, 3),
            condOrch(5, 3)
        ]
        self.one_to_many = one_to_many(conductors, orchestras)
        self.many_to_many = many_to_many(conductors, orchestras, condOrchs)

    def test_task1(self):
        expected_result = [
            ('Иванов', 38000, 'Ансамбль песни и пляски'),
            ('Улепетов', 20000, 'Российский национальный оркестр')
        ]
        result = task1(self.one_to_many)
        self.assertEqual(result, expected_result)

    def test_task2(self):
        expected_result = [
            ('Ансамбль песни и пляски', 38000),
            ('Местные ребята', 20500),
            ('Российский национальный оркестр', 17500)
        ]
        result = task2(self.one_to_many)
        self.assertEqual(result, expected_result)

    def test_task3(self):
        expected_result = [
            ('Российский национальный оркестр', ('Гончаренко', 'Иванов', 'Бобер'))
        ]
        result = task3(self.many_to_many)
        self.assertEqual(result, expected_result)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
