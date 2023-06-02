from datetime import datetime
from src.five_transaction import five_transaction


def output():
    """
    Функция принимает список данных из 5 последних успешных операций и выводит информацию на экран.
    """
    for i in five_transaction():
        # Дата операции в формате число.месяц.год.
        transfer_date = (datetime.strptime(i['date'], "%Y-%m-%dT%H:%M:%S.%f")).strftime("%d.%m.%Y")
        # Описание типа перевода.
        translation_description = i['description']
        # Находит ключ 'from', если его нет, то заменяет на ''.
        transfer_from = i.get('from', '')
        # Счет зачисления (куда).
        transfer_to = i['to']
        # Наименование счета отправления.
        payment = (transfer_from.split(' '))[0]
        # Наименование счета получения.
        receiving = (transfer_to.split(' '))[0]
        # Если нет счета отправления, то заменяет на "".
        account_number = (transfer_from.split(' '))[1] if len(transfer_from) > 1 else ''
        # Скрытие номера счета '****'.
        hide_outgoing_number = account_number[0:6] + ('*' * (len(account_number) - 10)) + account_number[-4:]
        # Разделение номера счета на блоки по 4 цифры.
        number_bloc = ' '.join([hide_outgoing_number[i:i + 4] for i in range(0, len(hide_outgoing_number), 4)])

        print(f"{transfer_date} {translation_description}")
        print(f"{payment} {number_bloc} -> {receiving} **{transfer_to[-4:]}")
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")


output()
