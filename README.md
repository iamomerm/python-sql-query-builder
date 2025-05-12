## SQLQuery

A simple Python class that enables you to build SQL queries using a fluent, chainable interface. This tool is perfect for developers who want to generate SQL statements programmatically without writing raw SQL strings manually.

---

### <ins> Features </ins>

- Intuitive, chainable API for building SQL queries
- Supports:
  - SELECT: SELECT, SELECT DISTINCT
  - Data Manipulation: INSERT INTO, UPDATE, DELETE FROM
  - Conditions: WHERE, AND, OR, IN, HAVING
  - Grouping & Ordering: GROUP BY, ORDER BY, LIMIT, OFFSET
  - Joins: LEFT JOIN, RIGHT JOIN, INNER JOIN, FULL JOIN
  - Transactions & Savepoints: COMMIT, ROLLBACK, SAVEPOINT
  - Table Operations: CREATE TABLE, DROP TABLE, ALTER TABLE, RENAME TABLE, ADD COLUMN, DROP COLUMN
  - Index Operations: CREATE INDEX
  - Permissions: GRANT, REVOKE 
  - Set Operations: UNION, INTERSECT, EXCEPT 
  - Conflict Handling: ON CONFLICT DO NOTHING 
  - Value Operations: VALUES, IN CLAUSE

---

### <ins> Installation </ins>

You can install this package via PIP: _pip install python=sql-query-builder_

### <ins> Usage </ins>

```python
from sql_query_builder import SQLQueryBuilder

query = (
    SQLQueryBuilder()
    .select('id', 'name', 'email', distinct=True)
    .from_table('users')
    .where("age > 21")
    .and_where("city = 'New York'")
    .order_by('name')
    .limit(10)
)

print(query.build())
# Output:
# SELECT DISTINCT id, name, email FROM users WHERE age > 21 AND city = 'New York' ORDER BY name LIMIT 10
```