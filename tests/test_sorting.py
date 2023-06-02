from src import utils, sorting


def test_sorting():
    """
    Функция проверяет, что типы функций read_operations() и sorting_operations() совпадают.
    """
    a = type(utils.read_operations())
    b = type(sorting.sorting_operations())
    assert a == b
