from example_module.some_functions import (
    add_numbers,
    multiply_numbers,
    subtract_numbers
    ) 

def test_add_numbers():
    a = 1
    b = 2

    assert add_numbers(a,b) == 3

def test_multiply_numbers():
    a = 1
    b = 2

    assert multiply_numbers(a,b) == 2

def test_subtract_numbers():
    a = 1
    b = 2

    assert subtract_numbers(a,b) == -1
