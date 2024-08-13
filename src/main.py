# src/main.py

from analysis import count_transactions_by_category
from analysis import search_transactions_by_description
from file_readers import read_transactions_from_csv
from file_readers import read_transactions_from_excel
from utils import read_json


def main():
    """
    Основная функция программы. Обеспечивает взаимодействие с пользователем и связывает
    функциональные модули для работы с банковскими транзакциями.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        file_path = "data/transactions.json"
        transactions = read_json(file_path)
    elif choice == "2":
        file_path = "data/transactions.csv"
        transactions = read_transactions_from_csv(file_path)
    elif choice == "3":
        file_path = "data/transactions_excel.xlsx"
        transactions = read_transactions_from_excel(file_path)
    else:
        print("Неверный выбор.")
        return

    if not transactions:
        print("Не удалось прочитать транзакции из файла.")
        return

    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    # Запрашиваем статус и проверяем его валидность
    while True:
        status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию. "
                "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\nСтатус: "
            )
            .strip()
            .upper()
        )
        if status in valid_statuses:
            break
        print(f'Статус операции "{status}" недоступен. Попробуйте снова.')

    print(f'Операции отфильтрованы по статусу "{status}"')

    filtered_transactions = [txn for txn in transactions if txn.get("status", "").upper() == status]

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    sort_by_date = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_by_date == "да":
        ascending = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        filtered_transactions.sort(key=lambda x: x["date"], reverse=(ascending == "по убыванию"))

    only_rubles = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if only_rubles == "да":
        filtered_transactions = [txn for txn in filtered_transactions if txn.get("currency", "").upper() == "RUB"]

    filter_description = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    )
    if filter_description == "да":
        search_string = input("Введите строку для поиска: ").strip()
        filtered_transactions = search_transactions_by_description(filtered_transactions, search_string)

    print("Распечатываю итоговый список транзакций...")
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
    for txn in filtered_transactions:
        print(f"{txn['date']} {txn['description']}")
        print(f"Сумма: {txn['amount']} {txn['currency']}")


if __name__ == "__main__":
    main()
