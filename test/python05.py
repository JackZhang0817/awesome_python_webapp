class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

s = Student('mr')

class Fib(object):
    # def __init__(self,a,b):
    #     self.a, self.b = a, b
    #
    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     self.a, self.b = self.b, self.a + self.b
    #     if self.a > 100:
    #         raise StopIteration()
    #     return self.a
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
# for n in Fib():
#     print(n)
f = Fib()
# for n in f:
#     print(n)
print(f[10])
print(f[0:6])
