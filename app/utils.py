import csv
from typing import NamedTuple, List, Callable, Union, Any

import requests


class Table(NamedTuple):
    header: List[str]
    body: List[List[str]]


def parse_data(path) -> Table:
    with open(path, 'r', encoding='utf-8-sig') as file:
        data = csv.reader(file)
        header, body = [], []
        for row in data:
            if not header:
                header = [*row]
                continue
            body.append([*row])

    return Table(header=header, body=body)


class FuncTools(NamedTuple):
    key: str
    func: Union[Callable, None]
    default: Any
    name: str | bool


parse_functions = [
    FuncTools('name', None, False, False),
    FuncTools('description', None, False, 'Описание'),
    FuncTools('key_skills', lambda row: ", ".join([i.get('name') for i in row]), False, 'Навыки'),
    FuncTools('salary',
              lambda row: ("{} {}".format((row.get('to') or row.get('from')), row.get('currency')) if row else ''),
              False, 'Зарплата'),
    FuncTools('employer', lambda row: row.get('name') if row else '', False, 'Компания'),
    FuncTools('area_name', None, False, 'Регион'),
    FuncTools('published_at', lambda row: row.split('T')[0], False, 'Дата'),
]


def get_vacancies(profession):
    r = requests.get(f'https://api.hh.ru/vacancies?text={profession}')
    if r.status_code != 200:
        return []
    result = r.json()

    items = result.get('items', [])
    data = []
    items = items[:10] if len(items) > 9 else items
    for item in items:
        r = requests.get(f'https://api.hh.ru/vacancies/{item.get("id")}')

        if r.status_code != 200:
            continue

        vacancy: dict = r.json()
        clean = {}
        for parse_function in parse_functions:
            field = vacancy.get(parse_function.name, parse_function.default)
            result = parse_function.func(result) if parse_function.func else field
            clean[parse_function.name] = f'{parse_function.name}: {result}' if parse_function.name and result else result
        data.append([clean.pop('name'), (clean.values())])
    return data
