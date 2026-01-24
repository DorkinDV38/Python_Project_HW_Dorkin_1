import pytest
from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [("73654108430135874305", "**4305"),
     ("73654108430135874959", "**4959"),
     ("1234567890", "**7890")],
)
def test_get_mask_account(value, expected):
    """Тестирование на правильную маску номера счёта"""
    assert get_mask_account(value) == expected


@pytest.mark.parametrize(
    "short_account,error_message",
    [
        ("123", "Номер счета должен содержать хотя бы 4 цифры."),
        ("", "Номер счета должен содержать хотя бы 4 цифры."),
    ],
)
def test_short_accounts(short_account, error_message):
    """Обработка входных данных меньшей длины"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(short_account)
    assert str(exc_info.value) == error_message



@pytest.mark.parametrize(
    "value, expected",
    [("2202560646780421", "2202 56** **** 0421"),
     ("7000792289606361", "7000 79** **** 6361"),
     ("3782822463100405", "3782 82** **** 0405"),
     ("4567890123456789", "4567 89** **** 6789"),
     ],
)
def test_get_mask_card_number(value, expected):
    """Тестирование на правильную маску номера карты"""
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "input_card,error_message",
    [
        ("1234", "Номер карты должен содержать ровно 16 цифр."),
        ("", "Номер карты должен содержать ровно 16 цифр."),
        ("abcde", "Номер карты должен содержать ровно 16 цифр."),
        (None, "Номер карты должен содержать ровно 16 цифр."),  # Некорректный тип данных
        (" ", "Номер карты должен содержать ровно 16 цифр."),
        ("12345678901234567890", "Номер карты должен содержать ровно 16 цифр."),  # Длина больше 16 символов
        ("1234 5678 9012 3456", "Номер карты должен содержать ровно 16 цифр.")
    ],
)
def test_get_mask_card_number_invalid_inputs(input_card, error_message):
    """Тесты на различные форматы и границы"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(input_card)
    assert str(exc_info.value) == error_message

