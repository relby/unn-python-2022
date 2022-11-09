import dis
import timeit
from string import printable
from random import choice


def test1(input_str: str):
    splits = []
    for char in (' ', ',', ';', ':', '.', '-', '_'):
         splits.append(input_str.split(char))
    return splits


def test2(input_str: str):
    splits = []
    append = splits.append
    split = input_str.split
    for char in (' ', ',', ';', ':', '.', '-', '_'):
         append(split(char))
    return splits

string = ''.join(choice(printable) for _ in range(400))

print('test1')
dis.dis(test1)
print(timeit.timeit(lambda: test1(string)))

print('test2')
dis.dis(test2)
print(timeit.timeit(lambda: test2(string)))
