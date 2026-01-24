from datetime import datetime
from typing import Union

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(card_or_account: Union[str, int]) -> str:
    """Функция принимает на вход вид карты и номер карты и возвращает ее маску вида <ВИД> XXXX XX** **** XXXX.
    Или функция принимает на вход слово <Счет> и номер счета и возвращает его маску вида <Счет> **XXXX"""

    # Деление строки на части по пробелам
    parts = str(card_or_account).split()

    # Берём последнюю часть (номер карты/счёта)
    card_account_number = parts[-1]

    # Инициализируем переменную для итога
    masked_card_account = ""

    # Через условный оператор в зависимости от длины номера маскируем как номер карты или номер счета
    if len(card_account_number) == 16:
        masked_card_account = str(card_or_account)[0:-16] + get_mask_card_number(card_account_number)
    elif len(card_account_number) == 20 and (parts[0].lower() == "счет" or parts[0].lower() == "счёт"):
        masked_card_account = str(card_or_account)[0:-20] + get_mask_account(card_account_number)
    else:
        raise ValueError("Invalid input type")

    return masked_card_account


def get_date(date_string: str) -> str:
    """Функция принимает на вход дату и конвертирует её в ДД.ММ.ГГГГ"""

    # Парсим дату из строки в объект datetime
    dt_object = datetime.fromisoformat(date_string)

    # конвертируем в нужный формат
    formatted_date = dt_object.strftime("%d.%m.%Y")

    return formatted_date


# asd ="Счёт 11111222223333345678"
#
# parts1 = str(asd).split()
# print(parts1[0].lower())
# print(len(parts1[1]))
#
# if len(parts1[1]) == 20 and (parts1[0].lower() == "счет" or parts1[0].lower() == "счёт"):
#     print('Условие верно')
#
# print(mask_account_card(asd))

# input_date = "2024-03-11T02:26:18.671407"
# formatted_date = get_date(input_date)
# print(formatted_date)  # Выведет: 11.03.2024
#
# input_date = "2026-02-28"
# formatted_date = get_date(input_date)
# print(formatted_date)  # Выведет: 28.02.2026
#
#
# print(mask_account_card("Maestro 1596837868705199"))
# print(mask_account_card("Счет 64686473678894779589"))
# print(mask_account_card("MasterCard 7158300734726758"))
# print(mask_account_card("Счет 35383033474447895560"))
# print(mask_account_card("Visa Classic 6831982476737658"))
# print(mask_account_card("Visa Platinum 8990922113665229"))
# print(mask_account_card("Visa Gold 5999414228426353"))
