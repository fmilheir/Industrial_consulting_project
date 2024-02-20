import unittest
from database import test_db_connection


class TestDatabase(unittest.TestCase):

    def test_table_user_if_not_exists(self):
        self.assertEqual("Database connection successful", test_db_connection())

if __name__ == '__main__':
    unittest.main()
