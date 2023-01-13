import csv
from typing import NamedTuple, List


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

