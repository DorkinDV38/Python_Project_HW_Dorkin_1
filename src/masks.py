from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску вида XXXX XX** **** XXXX"""

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
    masked_account = "**" + str(account)[-4:]
    return masked_account


# print(get_mask_card_number(2202560646780421))
# print(get_mask_card_number(7000792289606361))
# print(get_mask_account(73654108430135874305))
