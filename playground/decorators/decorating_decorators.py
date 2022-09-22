# METHOD 1

# def hello():
#     return "Hello world"


# def decorate(func):
#     def wrap():
#         print("I am a before decorator")
#         print(func())
#         print("I am after decorator")
#     return wrap


# hello = decorate(hello)()
# print(hello())

# METHOD 2:
# def decorate(func):
#     def wrap(*arg, **kwargs):
#         print("I am a before decorator")
#         print(func(*arg, **kwargs))
#         print("I am after decorator")
#
#     return wrap
#
#
# @decorate
# def hello(name):
#     return f"Hello {name}"
#
# @decorate
# def add(x,y):
#     return x + y
#
#
# hello("Banke")
# add(2,3)




# METHOD 3

# def decorate(func):
#     @functools.wraps(func)
#     def wrap(*arg, **kwargs):
#         print("I am a before decorator")
#         print(func(*arg, **kwargs))
#         print("I am after decorator")

#     return wrap


# @decorate
# def hello(name):
#     return f"Hello {name}"

# @decorate
# def add(x,y):
#     """
#     adds two numbers
#
#     """
#     return x + y
#
#
# hello("Banke")
# add(2,3)


# print(add.__name__)
# print(add.__doc__)

# METHOD 4
import functools
import time


def decorate(func):
    @functools.wraps(func)
    def wrap(*arg, **kwargs):
        print("I am a before decorator")
        f = func(func(*arg, **kwargs))
        print("I am after decorator")
        return f

    return wrap


def performance_counter(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"the function {f.__name__} took {end - start} to run")
        return func

    return wrapper


@decorate
def hello(name):
    return f"Hello {name}"


@performance_counter
@decorate
def add(x, y):
    """
    adds two numbers

    """
    return x + y


print(hello("Banke"))
print(add(2, 3))

print(add.__name__)
print(add.__doc__)


def multiply(a, b):
    return a * b


multiply_by_5 = functools.partial(multiply, 5)

print(multiply_by_5(6))
