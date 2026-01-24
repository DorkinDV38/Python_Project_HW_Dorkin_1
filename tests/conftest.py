from typing import Any
from typing import Dict
from typing import List

import pytest


@pytest.fixture
def date_f() -> str:
    return "2025-12-03"


@pytest.fixture
def operations_data_f_1() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2025-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226728, "state": "PENDING", "date": "2026-01-12T22:34:25.241689"},
        {"id": 615064591, "state": "FAILED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def operations_data_f_2() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 808087978, "state": "CANCELED", "date": "2025-06-30T02:08:58.425572"},
        {"id": 181819498, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226728, "state": "PENDING", "date": "2026-01-12T22:34:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def operations_data_no_status_f() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": "2025-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226728, "state": "FAILED", "date": "2026-01-12T22:34:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def operations_data_sort_des_f() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "CANCELED", "date": "2026-01-08T22:34:25.241689"},
        {"id": 939719570, "state": "CANCELED", "date": "2026-01-09T22:34:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2026-01-10T22:34:25.241689"},
        {"id": 594226728, "state": "FAILED", "date": "2026-01-11T22:34:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2026-01-12T22:34:25.241689"},
    ]


@pytest.fixture
def operations_data_equal_date_f() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2026-01-12T22:34:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2026-01-12T22:34:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2026-01-12T22:34:25.241689"},
    ]
