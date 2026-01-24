from typing import Any
from typing import Dict
from typing import List

import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state(
    operations_data_f_1: List[Dict[str, Any]],
    operations_data_f_2: List[Dict[str, Any]],
    operations_data_no_status_f: List[Dict[str, Any]],
) -> None:
    """Тестирование фильтрации разных списков словарей"""
    assert filter_by_state(operations_data_f_1) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2025-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(operations_data_f_2) == [
        {"id": 181819498, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert filter_by_state(operations_data_no_status_f) == []
    assert filter_by_state([]) == []


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2025-06-30T02:08:58.425572"},
            ],
        ),
        ("CANCELED", [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]),
        ("FAILED", [{"id": 615064591, "state": "FAILED", "date": "2018-10-14T08:21:33.419441"}]),
        ("SuperState", []),
    ],
)
def test_filter_by_state_parametr(
    value: str, expected: List[Dict[str, Any]], operations_data_f_1: List[Dict[str, Any]]
) -> None:
    """Тестирование на правильную отработку фильтра"""
    assert filter_by_state(operations_data_f_1, value) == expected


def test_sort_by_date(
    operations_data_sort_des_f: List[Dict[str, Any]], operations_data_equal_date_f: List[Dict[str, Any]]
) -> None:
    """Тестирование фильтрации разных списков словарей"""
    assert sort_by_date(operations_data_sort_des_f) == [
        {"id": 615064591, "state": "CANCELED", "date": "2026-01-12T22:34:25.241689"},
        {"id": 594226728, "state": "FAILED", "date": "2026-01-11T22:34:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2026-01-10T22:34:25.241689"},
        {"id": 939719570, "state": "CANCELED", "date": "2026-01-09T22:34:25.241689"},
        {"id": 41428829, "state": "CANCELED", "date": "2026-01-08T22:34:25.241689"},
    ]
    assert sort_by_date(operations_data_sort_des_f, False) == [
        {"id": 41428829, "state": "CANCELED", "date": "2026-01-08T22:34:25.241689"},
        {"id": 939719570, "state": "CANCELED", "date": "2026-01-09T22:34:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2026-01-10T22:34:25.241689"},
        {"id": 594226728, "state": "FAILED", "date": "2026-01-11T22:34:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2026-01-12T22:34:25.241689"},
    ]
    assert sort_by_date(operations_data_equal_date_f) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2026-01-12T22:34:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2026-01-12T22:34:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2026-01-12T22:34:25.241689"},
    ]

    assert sort_by_date(operations_data_equal_date_f, False) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2026-01-12T22:34:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2026-01-12T22:34:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2026-01-12T22:34:25.241689"},
    ]
    assert sort_by_date([]) == []

    with pytest.raises(KeyError):
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED"},
                {"id": 939719570, "state": "EXECUTED", "date": "2026-01-11T22:34:25.241689"},
                {"id": 594226727, "state": "CANCELED", "date": "2026-01-12T22:34:25.241689"},
            ]
        )

    with pytest.raises(ValueError):
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "01.01.2026"},
                {"id": 939719570, "state": "EXECUTED", "date": "2026-01-11T22:34:25.241689"},
                {"id": 594226727, "state": "CANCELED", "date": "2026-01-12"},
            ]
        )
