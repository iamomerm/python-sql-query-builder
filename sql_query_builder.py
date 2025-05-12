from typing import List


class SQLQueryBuilder:
    def __init__(self):
        self.__query_segments: List[str] = []

    def build(self) -> str:
        return ' '.join(self.__query_segments)

    #  Basic Query Clauses  #

    def select(self, *columns: str, distinct: bool = False) -> 'SQLQueryBuilder':
        columns_str = ', '.join(columns) if columns else '*'
        prefix = 'SELECT DISTINCT' if distinct else 'SELECT'
        self.__query_segments.append(f'{prefix} {columns_str}')
        return self

    def from_table(self, table: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'FROM {table}')
        return self

    def group_by(self, *columns: str) -> 'SQLQueryBuilder':
        columns_str = ', '.join(columns)
        self.__query_segments.append(f'GROUP BY {columns_str}')
        return self

    def order_by(self, *columns: str) -> 'SQLQueryBuilder':
        columns_str = ', '.join(columns)
        self.__query_segments.append(f'ORDER BY {columns_str}')
        return self

    def limit(self, n: int) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'LIMIT {n}')
        return self

    def offset(self, n: int) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'OFFSET {n}')
        return self

    def having(self, condition: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'HAVING {condition}')
        return self

    def on_conflict_do_nothing(self) -> 'SQLQueryBuilder':
        self.__query_segments.append('ON CONFLICT DO NOTHING')
        return self

    #  Conditions / Filtering  #

    def where(self, condition: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'WHERE {condition}')
        return self

    def and_where(self, condition: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'AND {condition}')
        return self

    def or_where(self, condition: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'OR {condition}')
        return self

    def not_where(self, condition: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'WHERE NOT ({condition})')
        return self

    def and_not(self, condition: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'AND NOT ({condition})')
        return self

    def or_not(self, condition: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'OR NOT ({condition})')
        return self

    def in_clause(self, column: str, *values: str) -> 'SQLQueryBuilder':
        values_str = ', '.join(str(v) for v in values)
        self.__query_segments.append(f'WHERE {column} IN ({values_str})')
        return self

    def not_in_clause(self, column: str, *values: str) -> 'SQLQueryBuilder':
        values_str = ', '.join(f"'{v}'" for v in values)
        self.__query_segments.append(f'WHERE {column} NOT IN ({values_str})')
        return self

    def not_exists(self, subquery: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'WHERE NOT EXISTS ({subquery})')
        return self

    #  Joins  #

    def left_join(self, table: str, on_condition: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'LEFT JOIN {table} ON {on_condition}')
        return self

    def right_join(self, table: str, on_condition: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'RIGHT JOIN {table} ON {on_condition}')
        return self

    def inner_join(self, table: str, on_condition: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'INNER JOIN {table} ON {on_condition}')
        return self

    def full_join(self, table: str, on_condition: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'FULL JOIN {table} ON {on_condition}')
        return self

    #  Data Manipulation (DML)  #

    def insert_into(self, table: str, **columns: str) -> 'SQLQueryBuilder':
        column_names = ', '.join(columns.keys())
        values = ', '.join(f"'{v}'" for v in columns.values())
        self.__query_segments.append(f'INSERT INTO {table} ({column_names}) VALUES ({values})')
        return self

    def values(self, *rows: List[str]) -> 'SQLQueryBuilder':
        rows_str = ', '.join(f"({', '.join(row)})" for row in rows)
        self.__query_segments.append(f'VALUES {rows_str}')
        return self

    def update(self, table: str, **columns: str) -> 'SQLQueryBuilder':
        set_clause = ', '.join(f"{k} = '{v}'" for k, v in columns.items())
        self.__query_segments.append(f'UPDATE {table} SET {set_clause}')
        return self

    def delete_from(self, table: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'DELETE FROM {table}')
        return self

    #  Transactions  #

    def commit(self) -> 'SQLQueryBuilder':
        self.__query_segments.append('COMMIT')
        return self

    def rollback(self) -> 'SQLQueryBuilder':
        self.__query_segments.append('ROLLBACK')
        return self

    def savepoint(self, savepoint_name: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'SAVEPOINT {savepoint_name}')
        return self

    #  DDL (Data Definition)  #

    def create_table(self, table: str, **columns: str) -> 'SQLQueryBuilder':
        columns_str = ', '.join(f"{name} {datatype}" for name, datatype in columns.items())
        self.__query_segments.append(f'CREATE TABLE {table} ({columns_str})')
        return self

    def drop(self, object_type: str, object_name: str, if_exists: bool = False) -> 'SQLQueryBuilder':
        exists_clause = 'IF EXISTS' if if_exists else ''
        self.__query_segments.append(f'DROP {exists_clause + " " if exists_clause else ""}{object_type} {object_name}')
        return self

    def alter_table(self, table: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'ALTER TABLE {table}')
        return self

    def add_column(self, column_name: str, column_definition: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'ADD COLUMN {column_name} {column_definition}')
        return self

    def drop_column(self, column_name: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'DROP COLUMN {column_name}')
        return self

    def rename_table(self, old_name: str, new_name: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'RENAME TABLE {old_name} TO {new_name}')
        return self

    def rename_column(self, table: str, old_name: str, new_name: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'ALTER TABLE {table} RENAME COLUMN {old_name} TO {new_name}')
        return self

    def create_index(self, index_name: str, table: str, *columns: str) -> 'SQLQueryBuilder':
        columns_str = ', '.join(columns)
        self.__query_segments.append(f'CREATE INDEX {index_name} ON {table} ({columns_str})')
        return self

    #  Permissions  #

    def grant(self, permission: str, table: str, user: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'GRANT {permission} ON {table} TO {user}')
        return self

    def revoke(self, permission: str, table: str, user: str) -> 'SQLQueryBuilder':
        self.__query_segments.append(f'REVOKE {permission} ON {table} FROM {user}')
        return self

    #  Set Operations  #

    def union(self, query: str, union_all: bool = False) -> 'SQLQueryBuilder':
        all_clause = 'ALL' if union_all else ''
        self.__query_segments.append(f'UNION {all_clause + " " if all_clause else ""}{query}')
        return self

    def intersect(self, query: str, intersect_all: bool = False) -> 'SQLQueryBuilder':
        all_clause = 'ALL' if intersect_all else ''
        self.__query_segments.append(f'INTERSECT {all_clause + " " if all_clause else ""}{query}')
        return self

    def except_clause(self, query: str, except_all: bool = False) -> 'SQLQueryBuilder':
        all_clause = 'ALL' if except_all else ''
        self.__query_segments.append(f'EXCEPT {all_clause + " " if all_clause else ""}{query}')
        return self

    #  Utility  #

    def __str__(self) -> str:
        return self.build()

    def __repr__(self) -> str:
        return self.__str__()
