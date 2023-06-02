from src.utils import read_operations


def sorting_operations():
    """
    Функция принимает список с данными и сортирует по успешно выполненным последним операциям,
    и сортирует по дате. Последняя выполненная операция первая в списке.
    """
    operations_catd = [item for item in read_operations() if item.get("state") == "EXECUTED" and "date" in item]
    operations_catd.sort(key=lambda x: x["date"], reverse=True)
    return operations_catd


sorting_operations()
