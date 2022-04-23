import unittest

from module_03_ci_culture_beginning.homework.person import Person

person = Person('Ivan', 1999, 'Saint-Petersburg')


class TestPerson(unittest.TestCase):

    def test_age(self):
        age = person.get_age()
        self.assertEqual(age, 23)

    def test_get_name(self):
        name = person.get_name()
        self.assertEqual(name, 'Ivan')

    def test_set_name(self):
        name = person.set_name('Ivan')
        self.assertEqual(name, True)

    def test_set_address(self):
        address = person.set_address('Saint-Petersburg')
        self.assertEqual(address, True)

    def test_get_address(self):
        address = person.get_address()
        return self.assertEqual(address, 'Saint-Petersburg')

    def test_is_homeless(self):
        address = person.is_homeless()
        self.assertEqual(address, False)
