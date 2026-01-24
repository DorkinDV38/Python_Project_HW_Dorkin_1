from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

# from typing import Union


def filter_by_state(operations_list: List[Dict[str, Any]], state: Optional[str] = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует словари операции из списка по заданному состоянию."""
    filtered_operations_list = []
    for operation in operations_list:
        if operation.get("state") == state:
            filtered_operations_list.append(operation)

    return filtered_operations_list


# # Пример функции:
# data = [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2020-01-12T22:34:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]
#
# print("Операции с состоянием EXECUTED:")
# print(filter_by_state(data, 'EXECUTED'))
#
# print("\nОперации с нулевым состоянием:")
# print(filter_by_state(data))
#
# print("\nОперации с состоянием CANCELED:")
# print(filter_by_state(data, 'CANCELED'))


def sort_by_date(operations_list: List[Dict[str, Any]], reverse: Optional[bool] = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей операций по дате."""
    sorted_list = sorted(operations_list, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
    return sorted_list


# # Пример использования:
# data = [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2020-01-12T22:34:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#
# print("\nОтсортированные по убыванию:")
# sorted_descending = sort_by_date(data)
# print(sorted_descending)
#
# print("\nОтсортированные по возрастанию:")
# sorted_ascending = sort_by_date(data, reverse=False)
# print(sorted_ascending)
