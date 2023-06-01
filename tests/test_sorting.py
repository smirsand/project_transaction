from src import utils, sorting


def test_sorting():
    a = type(utils.read_operations())
    b = type(sorting.sorting_operations())
    assert a == b
