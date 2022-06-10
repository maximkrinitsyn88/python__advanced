import datetime
import markdown


class Person:
    def __init__(self, name, year_of_birth, address=''):
        self.name = name
        self.yob = year_of_birth
        self.address = address

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.yob

    def get_name(self):
        return self.name

    def set_name(self, name):
        if self.name == name:
            return True

    def set_address(self, address):
        if self.address == address:
            return True

    def get_address(self):
        return self.address

    def is_homeless(self):
        if self.address:
            return False
        else:
            return True


with open('errors.md', 'w', encoding='utf-8') as errors:
    text = """#Ошибки#
    
    Проделал следующие действия:
    
    ***
    
    * В методе `get_age()` поменял переменные местами
    * В методе `set_name()` возвращаю True, если имя корректное
    * В методе `set_address()` возвращаю True, если адрес корректный
    * В методе `is_homeless()` возвращаю True, если человек бездомный, в противном случае - False
    
    ***"""
    markdown_test = markdown.markdown(text)
    errors.write(markdown_test)
