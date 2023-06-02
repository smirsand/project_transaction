from src import utils


def test_read_operations():
    """
    Функция проводит тест на корректность чтения файла operations.json.
    Сравнивает типы функции read_operations() (файл utils.py) с типом результата.
    """
    result = [{'date': '2019-08-26T10:50:58.294041',
               'description': 'Перевод организации',
               'from': 'Maestro 1596837868705199',
               'id': 441945886,
               'operationAmount': {'amount': '31957.58',
                                   'currency': {'code': 'RUB', 'name': 'руб.'}},
               'state': 'EXECUTED',
               'to': 'Счет 64686473678894779589'}]

    assert type(utils.read_operations()) == type(result)
