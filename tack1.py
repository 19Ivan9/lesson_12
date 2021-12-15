class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def hello(self):
        print(f'Hallo {self.name} {self.surname}, you age -  {self.age} !')


class Student(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.homework = 10
        self.create = 7

    def home_works(self):
        print(f'You must complete at least {self.homework} tasks')
        print(f'you did {self.create} tasks')


class Teacher(Student):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 10000

    def home_works(self, ):
        print(f'you did examination a {self.create} tasks')
        print(f'you salary {self.salary}')
