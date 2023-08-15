from main.utils import create_executed_transactions_list, format_date, number_mask, get_transaction_info


def test_create_executed_transactions_list():
    assert create_executed_transactions_list('tests/test_operations.json') == [
        {
            "id": 111,
            "state": "EXECUTED",
            "date": "1111-11-11T11:11:11.111111",
            "operationAmount": {
                "amount": "11111.11",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1234567812345678",
            "to": "Счет 12345123451234512345"
        },
        {
            "id": 222,
            "state": "EXECUTED",
            "date": "2222-12-22T22:22:22.222222",
            "operationAmount": {
                "amount": "22222.22",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 12345123451234512345"
        }
    ]


def test_format_date():
    assert format_date('2019-08-26T10:50:58.294041') == '26.08.2019'


def test_number_mask():
    assert number_mask('Счет 64686473678894779589') == 'Счет **9589'
    assert number_mask('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert number_mask('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'
    assert number_mask('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'


def test_get_transaction_info():
    assert get_transaction_info(create_executed_transactions_list('tests/test_operations.json'), 0) == ('''
11.11.1111 Перевод организации
Maestro 1234 56** **** 5678 -> Счет **2345
11111.11 руб.

''')
    assert get_transaction_info(create_executed_transactions_list('tests/test_operations.json'), 1) == ('''
22.12.2222 Открытие вклада
  -> Счет **2345
22222.22 руб.

''')
