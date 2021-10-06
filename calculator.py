

from math import pow, sqrt, pi


def get_one_input_as_int():
    a = int(input("A: "))
    return a


def get_two_inputs_as_int():
    a = int(input("A: "))
    b = int(input("B: "))
    return a, b


def add():
    a, b = get_two_inputs_as_int()
    return a+b


def sub():
    a, b = get_two_inputs_as_int()
    return a-b


def multiply():
    a, b = get_two_inputs_as_int()
    return a*b


def divide():
    a, b = get_two_inputs_as_int()
    return a/b


def power():
    a, b = get_two_inputs_as_int()
    return pow(a, b)


def square():
    a = get_one_input_as_int()
    return sqrt(a)


def circle():
    r = get_one_input_as_int()
    return pi*(r**2)


add.__name__ = 'Addition'
sub.__name__ = 'Sub'
multiply.__name__ = 'Multiply'
divide.__name__ = 'D'
power.__name__ = 'P'
square.__name__ = 'S'
circle.__name__ = 'C'


calc_operation = {
    1: add,
    2: sub,
    3: multiply,
    4: divide,
    5: power,
    6: square,
    7: circle
}
