# an example of a decorator function:
# that takes a function and returns a new function
# that wraps the original function
#
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        r = original_function(*args, **kwargs)
        print('after {}'.format(original_function.__name__))
        return r
    return wrapper_function


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))
    return 1


r1 = display_info('John', 25)
print(r1)

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")