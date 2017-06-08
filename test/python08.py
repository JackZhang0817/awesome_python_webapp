import time

# def deco(func):
#     startTime = time.time()
#     func()
#     endTime = time.time()
#     msecs = (endTime - startTime) * 1000
#     print("elapsed time %s" % msecs)

def deco(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print("elapsed time %s" %msecs)
    return wrapper

@deco
def myfunc():
    print("start myfunc")
    time.sleep(0.6)
    print("end myfunc")

print("myfunc is:", myfunc.__name__)

print("myfunc is:", myfunc.__name__)
myfunc()