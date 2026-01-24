import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [("Maestro 1596837868705198", "Maestro 1596 83** **** 5198"),
     ("Счет 64686473678894779589", "Счет **9589"),
     ("MasterCard 5555666677778888", "MasterCard 5555 66** **** 8888"),
     ("Visa 4674222255554747", "Visa 4674 22** **** 4747"),
     ("Счёт 11111222223333345678", "Счёт **5678")],
)
def test_mask_account_card(value, expected):
    """Тестирование на правильную отработку маскирования"""
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [("Счет", "Invalid input type"),
     ("Счёт 123", "Invalid input type"),
     ("Счет 123456789012345678900", "Invalid input type"),
     ("MasterCard 55556666777788889999", "Invalid input type"),
     ("MasterCard 1234", "Invalid input type")],
)
def test_invalid_type_mask_account_card(value, expected):
    """Тестирование на неверный формат, тип, пустоту"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(value)
    assert str(exc_info.value) == expected



def test_get_date(date_f):
    assert get_date("2025-12-01T02:26:18.671407") == "01.12.2025"
    assert get_date(date_f) == "03.12.2025"
    assert get_date("1999-12-31") == "31.12.1999"
    assert get_date("2024-02-29") == "29.02.2024"

    with pytest.raises(ValueError):  # Проверка некорректного ввода
        get_date("123")

    with pytest.raises(ValueError):
        get_date("2023-02-29")

    with pytest.raises(ValueError):
        get_date("01.01.2026")

    with pytest.raises(ValueError):
        get_date("")

    with pytest.raises(ValueError):
        get_date("abc")

    with pytest.raises(ValueError):
        get_date("2026-13-01")

    with pytest.raises(ValueError):
        get_date("2026-01-32")