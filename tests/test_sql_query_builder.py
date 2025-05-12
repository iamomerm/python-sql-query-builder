import unittest

from sql_query_builder import SQLQueryBuilder


class TestSQLQueryBuilder(unittest.TestCase):

    def test_select_specific_columns(self):
        query = SQLQueryBuilder().select('id', 'name', 'email').from_table('users').build()
        self.assertEqual(query, 'SELECT id, name, email FROM users')

    def test_select_with_where(self):
        query = SQLQueryBuilder().select('*').from_table('users').where("age > 21").build()
        self.assertEqual(query, 'SELECT * FROM users WHERE age > 21')

    def test_select_with_multiple_conditions(self):
        query = SQLQueryBuilder().select('*').from_table('users').where("age > 21").and_where("city = 'New York'").build()
        self.assertEqual(query, "SELECT * FROM users WHERE age > 21 AND city = 'New York'")

    def test_left_join_query(self):
        query = SQLQueryBuilder().select('name', 'email').from_table('users').left_join('orders', 'users.id = orders.user_id').build()
        self.assertEqual(query, 'SELECT name, email FROM users LEFT JOIN orders ON users.id = orders.user_id')

    def test_right_join_query(self):
        query = SQLQueryBuilder().select('name', 'email').from_table('users').right_join('orders', 'users.id = orders.user_id').build()
        self.assertEqual(query, 'SELECT name, email FROM users RIGHT JOIN orders ON users.id = orders.user_id')

    def test_inner_join_query(self):
        query = SQLQueryBuilder().select('name', 'email').from_table('users').inner_join('orders', 'users.id = orders.user_id').build()
        self.assertEqual(query, 'SELECT name, email FROM users INNER JOIN orders ON users.id = orders.user_id')

    def test_full_join_query(self):
        query = SQLQueryBuilder().select('name', 'email').from_table('users').full_join('orders', 'users.id = orders.user_id').build()
        self.assertEqual(query, 'SELECT name, email FROM users FULL JOIN orders ON users.id = orders.user_id')

    def test_group_by_query(self):
        query = SQLQueryBuilder().select('name', 'age').from_table('users').group_by('age').build()
        self.assertEqual(query, 'SELECT name, age FROM users GROUP BY age')

    def test_order_by_query(self):
        query = SQLQueryBuilder().select('name', 'age').from_table('users').order_by('age').build()
        self.assertEqual(query, 'SELECT name, age FROM users ORDER BY age')

    def test_limit_query(self):
        query = SQLQueryBuilder().select('*').from_table('users').limit(10).build()
        self.assertEqual(query, 'SELECT * FROM users LIMIT 10')

    def test_in_clause_query(self):
        query = SQLQueryBuilder().select('*').from_table('users').in_clause('age', 21, 22, 23).build()
        self.assertEqual(query, 'SELECT * FROM users WHERE age IN (21, 22, 23)')

    def test_drop_table_query(self):
        query = SQLQueryBuilder().drop("TABLE", "users").build()
        self.assertEqual(query, 'DROP TABLE users')

    # New tests for the remaining methods

    def test_create_table_query(self):
        query = SQLQueryBuilder().create_table('users', id='INT', name='VARCHAR(100)', email='VARCHAR(100)').build()
        self.assertEqual(query, 'CREATE TABLE users (id INT, name VARCHAR(100), email VARCHAR(100))')

    def test_create_index_query(self):
        query = SQLQueryBuilder().create_index('idx_name', 'users', 'name').build()
        self.assertEqual(query, 'CREATE INDEX idx_name ON users (name)')

    def test_grant_query(self):
        query = SQLQueryBuilder().grant('SELECT', 'users', 'admin').build()
        self.assertEqual(query, 'GRANT SELECT ON users TO admin')

    def test_revoke_query(self):
        query = SQLQueryBuilder().revoke('SELECT', 'users', 'admin').build()
        self.assertEqual(query, 'REVOKE SELECT ON users FROM admin')

    def test_commit_query(self):
        query = SQLQueryBuilder().commit().build()
        self.assertEqual(query, 'COMMIT')

    def test_rollback_query(self):
        query = SQLQueryBuilder().rollback().build()
        self.assertEqual(query, 'ROLLBACK')

    def test_savepoint_query(self):
        query = SQLQueryBuilder().savepoint('sp1').build()
        self.assertEqual(query, 'SAVEPOINT sp1')

    def test_union_query(self):
        query = SQLQueryBuilder().union('SELECT * FROM users').build()
        self.assertEqual(query, 'UNION SELECT * FROM users')

    def test_intersect_query(self):
        query = SQLQueryBuilder().intersect('SELECT * FROM users').build()
        self.assertEqual(query, 'INTERSECT SELECT * FROM users')

    def test_except_query(self):
        query = SQLQueryBuilder().except_clause('SELECT * FROM users').build()
        self.assertEqual(query, 'EXCEPT SELECT * FROM users')

    def test_add_column_query(self):
        query = SQLQueryBuilder().alter_table('users').add_column('age', 'INT').build()
        self.assertEqual(query, 'ALTER TABLE users ADD COLUMN age INT')

    def test_drop_column_query(self):
        query = SQLQueryBuilder().alter_table('users').drop_column('age').build()
        self.assertEqual(query, 'ALTER TABLE users DROP COLUMN age')

    def test_alter_table_query(self):
        query = SQLQueryBuilder().alter_table('users').build()
        self.assertEqual(query, 'ALTER TABLE users')

    def test_rename_table_query(self):
        query = SQLQueryBuilder().rename_table('users', 'customers').build()
        self.assertEqual(query, 'RENAME TABLE users TO customers')

    def test_rename_column_query(self):
        query = SQLQueryBuilder().rename_column('users', 'age', 'birthdate').build()
        self.assertEqual(query, 'ALTER TABLE users RENAME COLUMN age TO birthdate')

    def test_not_where_query(self):
        query = SQLQueryBuilder().select('*').from_table('users').not_where("age < 18").build()
        self.assertEqual(query, 'SELECT * FROM users WHERE NOT (age < 18)')

    def test_not_in_clause_query(self):
        query = SQLQueryBuilder().select('*').from_table('users').not_in_clause('age', 15, 16).build()
        self.assertEqual(query, "SELECT * FROM users WHERE age NOT IN ('15', '16')")

    def test_not_exists_query(self):
        query = SQLQueryBuilder().select('*').from_table('users').not_exists('SELECT 1 FROM banned WHERE banned.id = users.id').build()
        self.assertEqual(query, 'SELECT * FROM users WHERE NOT EXISTS (SELECT 1 FROM banned WHERE banned.id = users.id)')

    def test_and_not_query(self):
        query = SQLQueryBuilder().select('*').from_table('users').where("age > 18").and_not("verified = false").build()
        self.assertEqual(query, 'SELECT * FROM users WHERE age > 18 AND NOT (verified = false)')

    def test_or_not_query(self):
        query = SQLQueryBuilder().select('*').from_table('users').where("age > 18").or_not("verified = false").build()
        self.assertEqual(query, 'SELECT * FROM users WHERE age > 18 OR NOT (verified = false)')


if __name__ == '__main__':
    unittest.main()
