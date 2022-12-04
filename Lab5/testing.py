import unittest
from math import *
from function import get_roots
from pytest_bdd import scenario, given, when, then


# TDD
class programm_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_roots(1, -5, 6), [-sqrt(3), sqrt(3), -sqrt(2),
                                               sqrt(2)])

    def test2(self):
        self.assertEqual(get_roots(1, -4, 4), [-sqrt(2), sqrt(2)])

    def test3(self):
        self.assertEqual(get_roots(1, 0, 10), [])

    def test4(self):
        self.assertEqual(get_roots(1, 0, 10), [1])


# BDD
@scenario("scenarios.feature", "4 roots")
def test0():
    print('Scenarios: 4 roots')

@given("Data for equation")
def test1():
    print("\nData for equation")
    print(f"Data: {[1, -5, 6]}\n")


@when('I want to solve the equation')
def test2():
    print('I want to solve the equation')

@then('I get roots')
def test3():
    print('I get roots')
    assert get_roots(1, -5, 6) == [-sqrt(3), sqrt(3), -sqrt(2), sqrt(2)]

@then('I get roots')
def test4():
    print('I get roots')
    assert get_roots(1, -5, 6) == [-sqrt(3), sqrt(3), -sqrt(2)]

def main():
    unittest.main()


if __name__ == '__main__':
    main()
