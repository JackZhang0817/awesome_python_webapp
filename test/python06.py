class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        # if path == 'users':
        #     return lambda name:Chain('%s/users/%s' % (self._path,  name))
        return Chain('%s/%s' % (self._path, path))
    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain().status.users('ling').timeline.list('zhang'))

class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s' % self.name)
        return 'My class is %s' % self.name

s = Student('Ling')
# print(s.name)
print(s())
print(Chain().status)
