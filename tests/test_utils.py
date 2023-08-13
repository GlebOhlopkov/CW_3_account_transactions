from main.utils import create_transactions_list, format_date, number_mask


def test_format_date():
    assert format_date('2019-08-26T10:50:58.294041') == '26.08.2019'


def test_number_mask():
    assert number_mask('Счет 64686473678894779589') == 'Счет **9589'
    assert number_mask('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert number_mask('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'
    assert number_mask('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'
