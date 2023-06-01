import json


def read_operations():
    with open("C:/Users/Сергей/PycharmProjects/project_transaction/src/operations.json", "r", encoding="utf-8") as f:
        operations_catd = json.load(f)
    return operations_catd


read_operations()
