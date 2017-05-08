class Student(object):
    pass

def set_age(self, age):
    if not isinstance(age, int):
        raise ValueError('age must be integar')
    if age < 0 or age > 100:
        raise ValueError('age must between 0 -100')

    self.age = age

from types import MethodType
s = Student()
# s.set_age = MethodType(set_age, s)
Student.set_age = set_age
s.set_age(25.4)
s2 = Student()
s2.set_age(26)
print(s.age)
print(s2.age)