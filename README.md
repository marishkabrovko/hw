# Проект по обработке данных о банковских операциях

## Цель проекта

Этот проект предназначен для обработки и маскировки номеров банковских карт и счетов, а также фильтрации и сортировки данных.

## Установка

1. Клонируйте репозиторий:
    
    git clone <https://github.com/marishkabrovko/hw>

    

2. Установите зависимости:
    
    poetry install
    

## Использование

### Функции маскировки

#### `get_mask_card_number(card_number: int) -> str`

Маскирует номер карты. Оставляет видимыми первые 6 и последние 4 цифры. Формат вывода: `XXXX XX** **** XXXX`.


#### `from src.masks import get_mask_card_number`

#### `print(get_mask_card_number(7000792289606361))  # 7000 79** **** 6361`
`get_mask_account(account_number: int) -> str`

Маскирует номер счета. Оставляет видимыми только последние 4 цифры. Формат вывода: **XXXX.


#### `from src.masks import get_mask_account`

`print(get_mask_account(73654108430135874305))  # **4305`

### Функции для обработки данных

`filter_by_state(data: List[Dict], state: Optional[str] = 'EXECUTED') -> List[Dict]`

Фильтрует список словарей по значению ключа state.


`from src.processing import filter_by_state`

`data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]`

`executed = filter_by_state(data)
canceled = filter_by_state(data, 'CANCELED')
sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]`

Сортирует список словарей по дате.

`from src.processing import sort_by_date
sorted_data = sort_by_date(data)
sorted_data_asc = sort_by_date(data, descending=False)`

### Тестирование
Запуск тестов

Запустите тесты с отчетом покрытия:


`poetry run pytest --cov=src --cov-report=html`

Отчет покрытия тестами
Отчет покрытия тестами будет сгенерирован в папке htmlcov. Откройте index.html в браузере для просмотра.

### Требования к оформлению кода
Проект настроен для использования flake8, mypy, black и isort. Убедитесь, что ваш код соответствует требованиям:

`
poetry run flake8
poetry run mypy src
poetry run black src tests
poetry run isort src tests
`

### Новый модуль generators

#### filter_by_currency

Функция фильтрует транзакции по указанной валюте.

Пример использования:

`from src.generators import filter_by_currency
transactions = [# список транзакций]
usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)`

#### transaction_descriptions

Функция-генератор возвращает описание каждой транзакции.
#### card_number_generator

Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.

Пример использования:

`from src.generators import card_number_generator
for card_number in card_number_generator(1, 5):
    print(card_number)`

### Новый модуль `decorators`

#### Декоратор `log`

Декоратор `log` автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.

Пример использования:


`from decorators.log import log
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y
my_function(1, 2)`
### Новая функциональность

#### Считывание финансовых операций из CSV и Excel файлов

Добавлена возможность считывания финансовых операций из CSV- и Excel-файлов с использованием библиотеки `pandas`.
Реализованы функции `read_transactions_from_csv` и `read_transactions_from_excel` в модуле `file_readers.py`.
По умолчанию функции считывают данные из файлов `data/transactions.csv` и `data/transactions_excel.xlsx` и возвращают список словарей с транзакциями.
Если файл не найден или пустой, функция возвращает пустой список.

#### Тестирование

- Написаны тесты для новых функций с использованием `pytest` и `unittest.mock`.
