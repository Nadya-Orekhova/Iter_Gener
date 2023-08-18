

class FlatIterator():

    def __init__(self, list_of_list):
        self.my_list = list_of_list


    def __iter__(self):
        self.my_list_cursor = 0
        self.nested_list_cursor = -1
        return self


    def __next__(self):
        self.nested_list_cursor += 1
        if self.nested_list_cursor == len(self.my_list[self.my_list_cursor]):
            self.my_list_cursor += 1
            self.nested_list_cursor = 0
            if self.my_list_cursor == len(self.my_list):
                raise StopIteration
        return self.my_list[self.my_list_cursor][self.nested_list_cursor]


# list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
# print(list(FlatIterator(list_of_lists_1)))


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()




import types

def flat_generator(list_of_lists):
    for my_item in list_of_lists:
        for item in my_item:
            yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()

