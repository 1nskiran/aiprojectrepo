def bef(f):
    print('inside before')
    def wrapper():
        print('inside wrapper')
        f()
        print('inside after wrapper')
    return wrapper

@bef
def func():
    print('in main')

func()