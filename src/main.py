from src.analysis import count_transactions_by_category
from src.analysis import search_transactions_by_description
from src.file_readers import read_transactions_from_csv
from src.file_readers import read_transactions_from_excel


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")
    transactions = []

    if choice == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = read_transactions_from_csv("data/transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = read_transactions_from_excel("data/transactions_excel.xlsx")

    if not transactions:
        print("Не удалось загрузить транзакции.")
        return

    status = input("Программа: Введите статус, по которому необходимо выполнить фильтрацию: ").upper()
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while status not in valid_statuses:
        print(f'Статус операции "{status}" недоступен.')
        status = input("Программа: Введите статус, по которому необходимо выполнить фильтрацию: ").upper()

    transactions = [t for t in transactions if t.get("status", "").upper() == status]
    print(f'Операции отфильтрованы по статусу "{status}"')

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    sort_choice = input("Программа: Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_choice == "да":
        order = input("Программа: Отсортировать по возрастанию или по убыванию?: ").lower()
        reverse = order == "по убыванию"
        transactions.sort(key=lambda x: x.get("date", ""), reverse=reverse)

    currency_filter = input("Программа: Выводить только рублевые транзакции? Да/Нет: ").lower()
    if currency_filter == "да":
        transactions = [t for t in transactions if t.get("currency") == "RUB"]

    search_filter = input(
        "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет: "
    ).lower()
    if search_filter == "да":
        search_word = input("Пользователь: Введите слово для поиска: ")
        transactions = search_transactions_by_description(transactions, search_word)

    print("Распечатываю итоговый список транзакций...")
    if transactions:
        for transaction in transactions:
            print(transaction)
        print(f"Всего банковских операций в выборке: {len(transactions)}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
