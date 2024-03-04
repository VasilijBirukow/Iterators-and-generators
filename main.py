class FlatIterator:
    def __init__(self, nested_list):
        self.flatten_list = self.flatten(nested_list)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.flatten_list):
            item = self.flatten_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def flatten(self, nested_list):
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(self.flatten(item))
            else:
                result.append(item)
        return result


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    # for item in FlatIterator(list_of_lists_1):
    #     print(item)
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
