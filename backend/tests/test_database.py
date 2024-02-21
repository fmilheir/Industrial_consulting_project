import unittest
from database import test_db_connection
from database import create_table_user_if_not_exists


class TestDatabase(unittest.TestCase):
    def test_test_db_connection(self):
        self.assertEqual("Database connection successful", test_db_connection())

    def test_create_table_user_if_not_exists(self):
        self.assertEqual("Table 'user' created successfully.",create_table_user_if_not_exists())


if __name__ == '__main__':
    unittest.main()