from src.sorting import sorting_operations


def five_transaction():
    '''
    Функция принимает список и возвращает список из 5 элементов
    '''
    list_transaction = []
    count = 0
    for i in sorting_operations():
        count += 1
        if count == 6:
            break
        list_transaction.append(i)
    return list_transaction


five_transaction()
