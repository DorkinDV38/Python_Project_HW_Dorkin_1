from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску вида XXXX XX** **** XXXX"""
    if not isinstance(card_number, str) or len(card_number.strip()) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр.")
    masked_card_number = (
        str(card_number)[0:4]
        + " "
        + str(card_number)[4:6]
        + "** "
        + "*" * len(str(card_number)[8:-4])
        + " "
        + str(card_number)[-4:]
    )
    return masked_card_number


def get_mask_account(account: Union[str, int]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску вида **XXXX"""
    if len(str(account)) < 4:
        raise ValueError("Номер счета должен содержать хотя бы 4 цифры.")
    masked_account = "**" + str(account)[-4:]
    return masked_account


# print(get_mask_card_number(2202560646780421))
# print(get_mask_card_number(7000792289606361))
# print(get_mask_account(73654108430135874305))
