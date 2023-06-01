from src.utils import read_operations


def sorting_operations():
    '''
    Функция принимает список и сортирует по выполненным последним операциям. Последняя выполненная операция первая.
    '''
    operations_catd = [item for item in read_operations() if item.get("state") == "EXECUTED" and "date" in item]
    operations_catd.sort(key=lambda x: x["date"], reverse=True)
    return operations_catd


sorting_operations()
