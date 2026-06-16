from src.bank_widget.utils import load_transactions
from src.bank_widget.finance_utils import load_transactions_from_csv, load_transactions_from_excel
from src.bank_widget.processing import filter_by_state, sort_by_date
from src.bank_widget.re_counter import process_bank_search


def main():
    """Отвечает за основную логику проекта и связывает функциональности между собой"""

    transactions_data = []
    filtered_transactions = []

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        user_format_file = int(input("Выберите необходимый пункт меню:\n"
                                 "1. Получить информацию о транзакциях из JSON-файла\n"
                                 "2. Получить информацию о транзакциях из CSV-файла\n"
                                 "3. Получить информацию о транзакциях из XLSX-файла\n"))

        if user_format_file == 1:
            print("Для обработки выбран JSON-файл.")
            transactions_data = load_transactions(r"..\..\data\operations.json")
            break
        elif user_format_file == 2:
            print("Для обработки выбран CSV-файл.")
            transactions_data = load_transactions_from_csv(r"..\..\data\transactions.csv")
            break
        elif user_format_file == 3:
            print("Для обработки выбран XLSX-файл.")
            transactions_data = load_transactions_from_excel(r"..\..\data\transactions_excel.xlsx")
            break
        else:
            continue

    while True:
        user_state = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                           "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")

        if user_state.lower() not in ["executed", "canceled", "pending"]:
            print(f'Статус операции "{user_state}" недоступен.')
            continue
        else:
            filtered_transactions = filter_by_state(data=transactions_data, state=user_state.lower())
            print(f'Операции отфильтрованы по статусу "{user_state.upper()}"')
            break

    user_sort_date = input("Отсортировать операции по дате? Да/Нет\n")
    if user_sort_date.lower() == "да":
        user_reverse = input("Отсортировать по возрастанию или по убыванию?\n")

        if user_reverse.lower() == "по возрастанию":
            descending = False
        else:
            descending = True

        filtered_transactions = sort_by_date(filtered_transactions, descending)

    filter_by_currency_code = input("Выводить только рублевые транзакции? Да/Нет\n")
    if filter_by_currency_code.lower() == "да":
        filtered_transactions = [transaction for transaction in filtered_transactions if transaction.get("operationAmount").get("currency").get("code") == "RUB"]

    filter_by_word_in_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    if filter_by_word_in_description.lower() == "да":
        filter_word = input("Введите слово: ")
        filtered_transactions = process_bank_search(filtered_transactions, search=filter_word)

    print("Распечатываю итоговый список транзакций...")

    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")










if __name__ == '__main__':
    main()
