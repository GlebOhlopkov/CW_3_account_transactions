import json
from datetime import datetime


def create_executed_transactions_list(filename: str) -> list:
    """
    Метод для экспорта списка выполненных транзакций из файла
    :param filename: наименования файла для чтения
    :return: список выполненных транзакций
    """
    with open(filename, 'r', encoding='utf-8') as file:
        executed_transactions_list = []
        for transaction in json.load(file):
            if transaction['state'] == 'EXECUTED':
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


def get_transaction_info(transactions: list, number: int) -> str:
    """
    Метод получает на входе список транзакций и номер необходимой транзакции и возвращает
    информацию о транзакции (дата, тип перевода, откуда, куда, сколько)
    :param transactions: список транзакций
    :param number: числовое значение
    :return: краткая информация о транзакции (дата, тип перевода, откуда, куда, сколько)
    """
    date = format_date(transactions[number]['date'])
    description = transactions[number]['description']
    if 'from' in transactions[number]:
        money_from = number_mask(transactions[number]['from'])
    else: money_from = ' '
    money_to = number_mask(transactions[number]['to'])
    money_amount = transactions[number]['operationAmount']['amount']
    money_name = transactions[number]['operationAmount']['currency']['name']

    return (f'\n'
            f'{date} {description}\n'
            f'{money_from} -> {money_to}\n'
            f'{money_amount} {money_name}')
