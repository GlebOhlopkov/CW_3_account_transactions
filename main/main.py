from utils import create_executed_transactions_list, get_transaction_info


def get_last_transactions(number: int):
    """
    Основная логика работы программы, забирает из файла список транзакций,
    сортирует по дате (сверху - последние), выводит последние операции
    :param number: необходимое количество последних операций (по дате)
    :return: последние операции по счетам в необходимом количестве
    """
    transactions_list = create_executed_transactions_list('operations.json')
    transactions_list_sort = sorted(transactions_list, key=lambda d: d['date'], reverse=True)
    for operation in range(0, number):
        print(get_transaction_info(transactions_list_sort, operation))


if __name__ == '__main__':
    get_last_transactions(5)
