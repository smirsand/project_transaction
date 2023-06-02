from src.number_of_transaction import output


def test_number_of_transaction():
    """
    Функция проверяет, является ли “value” None или строкой
    :return:
    """
    value = output()
    assert value is None or isinstance(value, str)
