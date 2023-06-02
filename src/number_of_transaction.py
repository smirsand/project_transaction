from datetime import datetime
from src.five_transaction import five_transaction


def output():
    for i in five_transaction():
        transfer_date = (datetime.strptime(i['date'], "%Y-%m-%dT%H:%M:%S.%f")).strftime("%d.%m.%Y")  # Дата операции
        translation_description = i['description']  # Описание операции
        transfer_from = i.get('from', '')  # Находит ключ, если его нет, то заменяет на ""
        transfer_to = i['to']  # Счет зачисления
        payment = (transfer_from.split(' '))[0]  # Имя счета отправления
        receiving = (transfer_to.split(' '))[0]  # Имя счета получения
        account_number = (transfer_from.split(' '))[1] if len(
            transfer_from) > 1 else ''  # Если нет счета отправления, то заменяет на ""
        hide_outgoing_number = account_number[0:6] + ('*' * (len(account_number) - 10)) + account_number[
                                                                                          -4:]  # Скрытие номера счета
        number_bloc = ' '.join([hide_outgoing_number[i:i + 4] for i in
                                range(0, len(hide_outgoing_number), 4)])  # Разделение номера по 4 цифры
        print(f"{transfer_date} {translation_description}")
        print(f"{payment} {number_bloc} -> {receiving} **{transfer_to[-4:]}")
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")


output()
