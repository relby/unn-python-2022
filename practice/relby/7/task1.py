from sys import getsizeof

def print_func_name(func):
    def wrapper(*args, **kwargs):
        print('#' * 4, func.__name__, '#' * 4)
        return func(*args, **kwargs)
    return wrapper

@print_func_name
def size_of_tuples():
    for i in range(10):
        print('Size of tuple of length {0} is {1} bytes'.format(
            i,
            getsizeof(tuple(range(i))),
        ))

@print_func_name
def size_of_concated_tuples():
    tuple1 = tuple(range(3))
    tuple2 = tuple(range(10))
    print('Size of the first tuple of length {0} is {1} bytes'.format(
        len(tuple1),
        getsizeof(tuple1),
    ))
    print('Size of the second tuple of length {0} is {1} bytes'.format(
        len(tuple2),
        getsizeof(tuple2),
    ))
    print('Size of them concatenated is {0}'.format(
        getsizeof(tuple1 + tuple2)
    ))

@print_func_name
def size_of_concated_lists():
    list1 = list(range(3))
    list2 = list(range(10))
    print('Size of the first list of length {0} is {1} bytes'.format(
        len(list1),
        getsizeof(list1),
    ))
    print('Size of the second list of length {0} is {1} bytes'.format(
        len(list2),
        getsizeof(list2),
    ))
    print('Size of them concatenated is {0}'.format(
        getsizeof(list1 + list2)
    ))

@print_func_name
def size_of_concated_sets():
    set1 = set(range(1, 3))
    set2 = set(range(10, 51, 10))
    print('Size of the first set of length {0} is {1} bytes'.format(
        len(set1),
        getsizeof(set1),
    ))
    print('Size of the second set of length {0} is {1} bytes'.format(
        len(set2),
        getsizeof(set2),
    ))
    print('Size of them intersected is {0}'.format(
        getsizeof(set1 & set2)
    ))

@print_func_name
def size_of_concated_frozensets():
    frozenset1 = frozenset(range(1, 3))
    frozenset2 = frozenset(range(10, 51, 10))
    print('Size of the first frozenset of length {0} is {1} bytes'.format(
        len(frozenset1),
        getsizeof(frozenset1),
    ))
    print('Size of the second frozenset of length {0} is {1} bytes'.format(
        len(frozenset2),
        getsizeof(frozenset2),
    ))
    print('Size of them intersected is {0}'.format(
        getsizeof(frozenset1 & frozenset2)
    ))


@print_func_name
def size_of_class_instances():
    class Point1(object):
        x: int
        y: int

        def __init__(self, x, y):
            self.x = x
            self.y = y

    print('Size of object with two fields without slots is {0} bytes'.format(
        getsizeof(Point1(1, 2))
    ))

    class Point2(object):
        __slots__ = ('x', 'y')
        
        x: int
        y: int

        def __init__(self, x, y):
            self.x = x
            self.y = y

    print('Size of object with two fields with slots is {0} bytes'.format(
        getsizeof(Point2(1, 2))
    ))


def main():
    size_of_tuples()
    size_of_concated_tuples()
    size_of_concated_lists()
    size_of_concated_sets()
    size_of_concated_frozensets()
    size_of_class_instances()


if __name__ == '__main__':
    main()
