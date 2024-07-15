# feature/homework_10_1

## Цель проекта

Этот проект предназначен для обработки и маскировки номеров банковских карт и счетов, а также фильтрации и сортировки данных.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone <https://github.com/marishkabrovko/hw.git>
    cd project_name
    ```

2. Установите зависимости:
    ```bash
    poetry install
    ```

## Использование

### Функции маскировки

#### `get_mask_card_number(card_number: int) -> str`

Маскирует номер карты. Оставляет видимыми первые 6 и последние 4 цифры. Формат вывода: `XXXX XX** **** XXXX`.

```python
from src.masks import get_mask_card_number

print(get_mask_card_number(7000792289606361))  # 7000 79** **** 6361
get_mask_account(account_number: int) -> str
Маскирует номер счета. Оставляет видимыми только последние 4 цифры. Формат вывода: **XXXX.