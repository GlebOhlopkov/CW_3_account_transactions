import json
from datetime import datetime


def create_executed_transactions_list(filename: str) -> list:
    """
    Метод для экспорта списка выполненных транзакций из файла
    :param filename: наименования файла для чтения
    :return: список выполненных транзакций
    """
    with open(filename, 'r', encoding='utf-8') as file:
        transactions_list = json.load(file)
        executed_transactions_list = []
        for transaction in transactions_list:
            if transaction['state'] == "EXECUTED":
                executed_transactions_list.append(transaction)
    return executed_transactions_list


def format_date(date_iso: str) -> str:
    """
    Метод для перевода даты в формат ДД.ММ.ГГГГ
    :param date_iso: дата в формате ISO 8601
    :return: дата в формате ДД.ММ.ГГГГ
    """
    transaction_date = datetime.strptime(date_iso, '%Y-%m-%dT%H:%M:%S.%f')
    return transaction_date.strftime('%d.%m.%Y')


def number_mask(number: str) -> str:
    """
    Метод для наложения маски на метод оплаты/приема транзакций
    :param number: номер счета/банковской карты
    :return: номер счета/банковской карты с шифрованным числовым значением
    """
    list_number = number.split(' ')
    if list_number[0] == "Счет":
        result_number = ' '.join(list_number)
        return f'{list_number[0]} **{result_number[-4:]}'
    if list_number[0] == "Maestro":
        result_number = ' '.join(list_number)
        return f'{list_number[0]} {result_number[-16:-12]} {result_number[-12:-10]}** **** {result_number[-4:]}'
    if list_number[0] == "MasterCard":
        result_number = ' '.join(list_number)
        return f'{list_number[0]} {result_number[-16:-12]} {result_number[-12:-10]}** **** {result_number[-4:]}'
    if list_number[0] == "Visa":
        result_number = ' '.join(list_number)
        return (f'{list_number[0]} {list_number[1]} {result_number[-16:-12]} '
                f'{result_number[-12:-10]}** **** {result_number[-4:]}')
