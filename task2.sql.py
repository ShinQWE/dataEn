import sqlite3
from typing import Any, Dict, Iterator

class TableData:
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.database_name)
        self.conn.row_factory = sqlite3.Row  
        self.cursor = self.conn.cursor()

    def __len__(self) -> int:
        self.cursor.execute(f'SELECT count(*) FROM {self.table_name}')
        return self.cursor.fetchone()[0]

    def __getitem__(self, name: str) -> Dict[str, Any]:
        self.cursor.execute(f'SELECT * FROM {self.table_name} WHERE name = :name', {'name': name})
        row = self.cursor.fetchone()
        if row is None:
            raise KeyError(f"запись по имени не найдена: {name}")
        return dict(row)  #еперь это работает, потому что row — это объект sqlite3.Row

    def __contains__(self, name: str) -> bool:
        self.cursor.execute(f'SELECT 1 FROM {self.table_name} WHERE name = :name', {'name': name})
        return self.cursor.fetchone() is not None

    def __iter__(self) -> Iterator[Dict[str, Any]]:
        self.cursor.execute(f'SELECT * FROM {self.table_name}')
        while row := self.cursor.fetchone():
            yield dict(row)  

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    presidents = TableData(database_name='example.sqlite', table_name='presidents')

    #кол-во записи
    print(f"кол-во записи: {len(presidents)}")

    #наличие президента
    name_to_check = 'Yeltsin'
    if name_to_check in presidents:
        print(f"{name_to_check} is in the database.")
        print(presidents[name_to_check]) #данные президента

    print("список президенто:")
    for president in presidents:
        print(president['name'])

    presidents.close()


# Number of presidents: 3
# Yeltsin is in the database.
# {'name': 'Yeltsin', 'age': 999, 'country': 'Russia'}
# List of presidents:
# Yeltsin
# Trump
# Big Man Tyrone